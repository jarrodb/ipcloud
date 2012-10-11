"""
"""

class VBD:
    def __init__(self, session, vm_ref, vdi_ref):
        self._session = session
        self._vm_ref = vm_ref
        self._vdi_ref = vdi_ref

    def create(self):
        rec = {
            'VM': self._vm_ref,
            'VDI': self._vdi_ref,
            'userdevice': 'autodetect',
            'bootable': True,
            'mode': 'RW',
            'type': 'disk',
            'unpluggable': True,
            'empty': False,
            'other_config': {},
            'qos_algorithm_type': '',
            'qos_algorithm_params': {},
            'qos_supported_algorithms': [],
            }
        self._vbd_ref = self._session.xenapi.VBD.create(rec)
        return self._vbd_ref

    def plug(self):
        self._session.xenapi.VBD.plug(self._vbd_ref)
        orig_dev = self._session.xenapi.VBD.get_device(self._vbd_ref)

