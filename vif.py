"""
"""

class VIF:
    def __init__(self, session, network_ref=None):
        self._session = session

    def create(self, vm_ref, mac_address=''):
        rec = {
            'device': '0',
            'network': 'OpaqueRef:605866ff-7037-83c4-80fc-64bac014aab9',
            'VM': vm_ref,
            'MAC': mac_address,
            'MTU': '1500',
            'other_config': {},
            'qos_algorithm_type': '',
            'qos_algorithm_params': {},
            }
        self._vif_ref = self._session.xenapi.VIF.create(rec)
        return self._vif_ref
