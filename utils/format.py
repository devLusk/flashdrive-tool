import subprocess
import time

from utils.devices import list_devices

def format_flashdrive():
    list_devices()

    # Ask the user for the disk identifier (e.g., sda)
    disk_raw = input(f"\nEnter the disk identifier (e.g. sda): ")

    if not disk_raw:
        print("Error: no device specified.")
        input("Press ENTER to return to the menu...")
        return

    disk = f"/dev/{disk_raw}"
    print(f"Selected device: {disk}")
    
    # Ask the user for the partition number
    partition_raw = input(f"\nEnter the partition number: ")
    partition = f"{disk}{partition_raw}"
    print(f"Selected partition: {partition}")

    # Ask the user to set a volume label
    label_name = input(f"\nEnter volume label (default: USB_Drive): ")
    if not label_name:
        label_name = "USB_Drive"

    print(f"Volume label set to: {label_name}")

    # Ask the user for confirmation
    print(f"\nWarning: all data on {disk} will be deleted.")
    confirmation = input("To proceed, type 'YES' to confirm: ")
    if confirmation not in ("yes", "YES"):
        print("Canceled...")
        input("Press ENTER to return to the menu...")
        return
    
    print(f"\nConfirmation received")

    # Umount partition
    print(f"\nTrying to unmount the partition (if in use)...")
    subprocess.run(f'sudo umount {partition} 2>/dev/null', shell=True)
    print("Partition unmounted (if it was mounted)")

    # Deleting data
    print(f"\nDeleting old data and signatures...")
    subprocess.run(f'sudo wipefs -a {disk}', shell=True)
    print("Old data deleted")

    # New partition table
    print(f"\nDefining new partition table (msdos)...")
    subprocess.run(f'sudo parted -s {disk} mklabel msdos', shell=True)
    print("Partition table created")

    # Volume format options
    print(f"\nSelect the volume format:")
    print("1) FAT32 - High compatibility")
    print("2) NTFS - Optimized for Windows")
    print("3) EXT4 - Linux system")
    volume_option = input("Choose an option: ")

    match volume_option:
        case "1":
            print("Partitioning for FAT32 system...")
            subprocess.run(f'sudo parted -s -a optimal {disk} mkpart primary fat32 0% 100%', shell=True)
            time.sleep(2)
            print(f"Formatting to FAT32 with the label: {label_name}")
            subprocess.run(f'sudo mkfs.vfat -F 32 -n {label_name} {partition}', shell=True)
        case "2":
            print("Partitioning for NTFS system...")
            subprocess.run(f'sudo parted -s -a optimal {disk} mkpart primary ntfs 0% 100%', shell=True)
            time.sleep(2)
            print(f"Formatting to NTFS with the label: {label_name}")
            subprocess.run(f'sudo mkfs.ntfs -f -L {label_name} {partition}', shell=True)
        case "3":
            print("Partitioning for EXT4 system...")
            subprocess.run(f'sudo parted -s -a optimal {disk} mkpart primary ext4 0% 100%', shell=True)
            time.sleep(2)
            print(f"Formatting to EXT4 with the label: {label_name}")
            subprocess.run(f'sudo mkfs.ext4 -L {label_name} {partition}', shell=True)
        case _:
            print("Invalid format option selected.")
            input("Press ENTER to return to the menu...")
            return

    print(f"\nFormatting complete. Volume named {label_name}.")
    input("Press ENTER to return to the menu...")