"""
Instance details
"""

class Instance:
    """ Instance represents a Xen VM comprised of memory, cpu, and disk.

    Keyword Arguments:
        name
    """
    INSTANCE_TYPES = {
        'level1': dict(memory=512, vcpus=1, storage_gb=10),
        'level2': dict(memory=1024, vcpus=1, storage_gb=20),
        'level3': dict(memory=2048, vcpus=2, storage_gb=40),
        }

    def __init__(self, **kwargs):
        self._name = kwargs.get('name', None)
        self._memory = kwargs.get('memory', None)
        self._vcpus = kwargs.get('vcpus', None)
        self._storage_gb = kwargs.get('storage_gb', None)
        self._state = kwargs.get('state', None)
        self._instance_type = kwargs.get('instance_type', None)
        self._init_instance()

    def _init_instance(self):
        if not self._instance_type:
            return

        self._instance_type = self.INSTANCE_TYPES[self._instance_type]
        self._memory = self._instance_type['memory']
        self._vcpus = self._instance_type['vcpus']
        self._storage_gb = self._instance_type['storage_gb']

