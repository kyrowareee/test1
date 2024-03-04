import os
import platform
import psutil
import datetime
from colorama import init, Fore

init(autoreset=True)

def get_system_info():
    system_name = platform.uname()[1]
    system_version = platform.version()

    install_date = ""
    if platform.system() == "Windows":
        try:
            install_date = os.popen('systeminfo | find /i "install date"').read().strip()
            install_date = install_date.split(":", 1)[1].strip() if "install date" in install_date.lower() else "Not available"
        except Exception as e:
            print(Fore.RED + f"An error occurred while retrieving the install date: {e}")
            install_date = "Not available"
    else:
        install_date = "Not available"

    is_virtual_machine = "Yes" if "vbox" in system_version.lower() or "vmware" in system_version.lower() else "No"

    boot_time = psutil.boot_time()
    boot_time = datetime.datetime.fromtimestamp(boot_time).strftime("%m/%d/%Y, %H:%M:%S")

    reset_status = "Yes" if boot_time > install_date else "No"

    return {
        "System Name": system_name,
        "System Version": system_version,
        "Virtual Machine": is_virtual_machine,
        "Install Date": install_date,
        "Boot Time": boot_time,
        "Reset Status": reset_status,
    }

def print_system_info(info):
    for key, value in info.items():
        print(Fore.GREEN + f"{key}: {value}\n")

if __name__ == "__main__":
    print(Fore.GREEN + "\nVACBAN Checker made by: daddyprog\n")
    info = get_system_info()
    print_system_info(info)

print(Fore.GREEN + "\nPress Enter to exit...")
input()