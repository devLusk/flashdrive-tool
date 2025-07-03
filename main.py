from utils.bootable import create_bootable
from utils.devices import list_devices
from utils.format import format_flashdrive

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