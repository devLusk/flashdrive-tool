import subprocess

def list_devices():
    print("Detected disks and partitions:")
    subprocess.run('lsblk -o NAME,SIZE,TYPE,MOUNTPOINT | grep -E "disk|part"', shell=True)

def format_flashdrive():
    list_devices()
    disk_raw = input("Enter the disk identifier (e.g. sda): ")

    if not disk_raw:
        print("Error: no device specified.")
        input("Press ENTER to return to the menu...")
        return

    disk = f"/dev/{disk_raw}"
    print(f"Selected device: {disk}")

    label_name = input("Set volume label (default: USB_Drive): ")
    if not label_name:
        label_name = "USB_Drive"

    print(f"Volume label set to: {label_name}")


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