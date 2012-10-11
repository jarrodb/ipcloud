"""
"""

SECTOR_SIZE = 512
MBR_SIZE_SECTORS = 63
MBR_SIZE_BYTES = MBR_SIZE_SECTORS * SECTOR_SIZE

class VDI:
    def __init__(self, session):
        self._session = session

        sr = self._session.xenapi.SR.get_by_name_label('Local storage')
        if sr:
            self._sr_ref = sr[0]
        else:
            raise ValueError('Cannot determine local storage')

    def create(self, name_label, virtual_size):
        virtual_size *= (1024 * 1024)
        rec = {
            'name_label': name_label,
            'name_description': '',
            'SR': self._sr_ref,
            'virtual_size': '10737418240',
            'type': 'User',
            'sharable': False,
            'read_only': False,
            'xenstore_data': {},
            'other_config': {},
            'sm_config': {},
            'tags': []
            }
        self._vdi_ref = self._session.xenapi.VDI.create(rec)
        return self._vdi_ref
