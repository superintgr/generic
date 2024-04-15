from pyVim.connect import SmartConnect, Disconnect
from pyVmomi import vim, vmodl
import atexit

class VirtualMachineManager:
    def __init__(self, host, user, password, vm_name):
        self.host = host
        self.user = user
        self.password = password
        self.vm_name = vm_name
        self.service_instance = None
        self.vm = None

    def connect(self):
        self.service_instance = SmartConnect(
            host=self.host,
            user=self.user,
            pwd=self.password
        )
        atexit.register(Disconnect, self.service_instance)

    def find_vm(self):
        content = self.service_instance.content
        container = content.viewManager.CreateContainerView(
            content.rootFolder, [vim.VirtualMachine], True
        )
        for vm in container.view:
            if vm.name == self.vm_name:
                self.vm = vm
                break
        container.Destroy()

    def start_vm(self):
        if not self.vm:
            raise RuntimeError("VM not found. Please call find_vm() first.")
        if self.vm.runtime.powerState == vim.VirtualMachinePowerState.poweredOff:
            self.vm.PowerOn()

    def stop_vm(self):
        if not self.vm:
            raise RuntimeError("VM not found. Please call find_vm() first.")
        if self.vm.runtime.powerState == vim.VirtualMachinePowerState.poweredOn:
            self.vm.PowerOff()

    def execute_terminal_code(self, code):
        if not self.vm:
            raise RuntimeError("VM not found. Please call find_vm() first.")
        if self.vm.runtime.powerState != vim.VirtualMachinePowerState.poweredOn:
            raise RuntimeError("VM is not powered on.")
        
        # Code execution logic here
        # Example: Use SSH to execute code remotely on the VM
        # Replace the following with your preferred method
        ssh_client.execute_command(code)

if __name__ == "__main__":
    # Example usage
    host = "vSphere_server_address"
    user = "username"
    password = "password"
    vm_name = "virtual_machine_name"

    vm_manager = VirtualMachineManager(host, user, password, vm_name)
    vm_manager.connect()
    vm_manager.find_vm()
    vm_manager.start_vm()
    vm_manager.execute_terminal_code("ls -l")
    vm_manager.stop_vm()
