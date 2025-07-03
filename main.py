import subprocess

def list_devices():
    print("\nDetected disks and partitions:")
    subprocess.run('lsblk -o NAME,SIZE,TYPE,MOUNTPOINT | grep -E "disk|part"', shell=True)

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
    label_name = input(f"\nSet volume label (default: USB_Drive): ")
    if not label_name:
        label_name = "USB_Drive"

    print(f"Volume label set to: {label_name}")

    # Ask the user for confirmation
    print(f"\nWarning: all data on {disk} will be deleted.")
    confirmation = input("To continue, confirm typing 'YES': ")
    if confirmation not in ("yes", "YES"):
        print("Canceled...")
        input("Press ENTER to return to the menu...")
        return
    
    print(f"\nConfirmation received")

    # Umount partition
    print(f"\nTrying to umount the partition (if in use)...")
    subprocess.run(f'sudo umount {partition} 2>/dev/null', shell=True)
    print("Partition umounted (if mounted)")

    # Deleting data
    print(f"\nDeleting old subscriptions and data...")
    subprocess.run(f'sudo wipefs -a {disk}', shell=True)
    print("Old data deleted")

    # New partition table
    print(f"\nDefining new partition table (msdos)...")
    subprocess.run(f'sudo parted -s {disk} mklabel msdos', shell=True)
    print("Partition table created")

    # Volumn format options
    print(f"\nSelect the volumn format:")
    print("1) FAT32 - high compatibility")
    print("2) NTFS - Otimizated for Windows")
    print("3) EXT4 - LInux sistem")
    volumn_option = input("Choose an option: ")

def create_bootable():
    # TODO: This feature is not implemented yet.
    input("Press ENTER to return to the menu...")

def main():
    while True:
        print("\n=== MENU ===")
        print("1) Format flash drive")
        print("2) Create bootable flash drive")
        print("3) List devices")
        print("4) Exit")

        option = input("Choose an option: ")

        match option:
            case "1":
                format_flashdrive()
            case "2":
                create_bootable()
            case "3":
                list_devices()
            case "4":
                print("Exiting...")
                break
            case _:
                print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()