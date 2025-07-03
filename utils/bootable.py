import subprocess
import os

from utils.devices import list_devices # Provides direct access to operating system features

def create_bootable():
    iso_path = input("Path of ISO file: ")
    iso_path = os.path.expanduser(iso_path)

    list_devices()

    disk_raw = input(f"\nEnter the disk identifier (e.g. sda): ")
    disk = f"/dev/{disk_raw}"

    print(f"\nWarning: all data on {disk} will be deleted.")
    confirmation = input("To proceed, type 'YES' to confirm: ")

    if confirmation in ("yes", "YES"):
        subprocess.run(f'sudo umount {disk} 2>/dev/null', shell=True)

        if not os.path.isfile(iso_path):
            print(f"Eror: ISO file not found in {iso_path}")
        else:
            print("Recording ISO, please wait...")
            subprocess.run(f'sudo dd if={iso_path} of={disk} bs=4M status=progress oflag=sync', shell=True)
            print("Finished. USB created with the image.")
    else:
        print("Canceled...")
        input("Press ENTER to return to the menu...")
        return

    input("Press ENTER to return to the menu...")