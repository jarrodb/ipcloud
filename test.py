import XenAPI
import pycurl
from instance import Instance
from vbd import VBD
from vif import VIF
from vdi import VDI
from vm import VM
from pif import get_network, get_public_pif

XENAPI_URL = 'http://65.183.54.10'

IMAGE_PATH = '/Users/jarrod/Dev/ipcloud/ubuntu.10-04.x86-64.20100927.img.gz'

import XenAPI
session = XenAPI.Session('https://65.183.54.10/')
session.login_with_password('root','')
xenapi = session.xenapi

i = Instance(name='Ubuntu 10.04', instance_type='level2')

v = VM(session)
vm_ref = v.create(i, '', '')
print "vm_ref - %s" % vm_ref

di = VDI(session)
vdi_ref = di.create('%s-vdi' % i._name, i._storage_gb)
print "vdi_ref - %s" % vdi_ref
# This is where the img should be attached to disk?
c = pycurl.Curl()
c.setopt(c.POST, True)
c.setopt(c.ENCODING, 'gzip')
c.setopt(c.HTTPAUTH, c.HTTPAUTH_BASIC)
c.setopt(c.USERPWD, "%s:%s" % ('root', ''))
c.setopt(c.URL, "%s/import_raw_vdi?vdi=%s" % (XENAPI_URL, vdi_ref))
c.setopt(c.HTTPPOST, [
    ("filename", (c.FORM_FILE, IMAGE_PATH)),
    ] )
c.setopt(c.VERBOSE, 1)
c.perform()
c.close()

vb = VBD(session, vm_ref, vdi_ref)
vbd_ref = vb.create()
print "vbd_ref - %s" % (vbd_ref)

vi = VIF(session)
vif_ref = vi.create(vm_ref)
print "vif_ref - %s" % (vif_ref)

session.xenapi.VM.start(vm_ref, False, False)

