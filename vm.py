""" You need to comment more, sucker!  Now you can't read your code.
"""

class VM:
    def __init__(self, session):
        self._session = session

    def create(self, instance, kernel, ramdisk, pv_kernel=False):
        """ Create a VM record."""
        memory = str(long(instance._memory) * 1024 * 1024)
        vcpus = str(instance._vcpus)
        rec = {
            'name_label': instance._name,
            'name_description': '',
            'is_a_template': False,
            'memory_static_min': '0',
            'memory_static_max': memory,
            'memory_dynamic_min': memory,
            'memory_dynamic_max': memory,
            'VCPUs_at_startup': vcpus,
            'VCPUs_max': vcpus,
            'VCPUs_params': {},
            'actions_after_shutdown': 'destroy',
            'actions_after_reboot': 'restart',
            'actions_after_crash': 'destroy',
            'PV_bootloader': 'pygrub',
            'PV_kernel': '',
            'PV_ramdisk': '',
            'PV_args': 'root=/dev/xvda',
            'PV_bootloader_args': '',
            'PV_legacy_args': '',
            'HVM_boot_policy': '',
            'HVM_boot_params': {},
            'platform': {
                'acpi': 'true',
                'apic': 'true',
                'pae': 'true',
                'viridian': 'true',
                },
            'PCI_bus': '',
            'recommendations': '',
            'affinity': '',
            'user_version': '0',
            'other_config': {},
            }

        self._vm_ref = self._session.xenapi.VM.create(rec)
        return self._vm_ref


