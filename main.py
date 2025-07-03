import subprocess

def list_devices():
    subprocess.run(['sblk', '-o', 'NAME,SIZE,TYPE,MOUNTPOINT'])

def main():
    while True:
        print("=== MENU ===")
        print("1) Format flash drive")
        print("2) Create bootable flash drive")
        print("3) List devices")
        print("4) Exit")
        option = input("Choose an option: ")

if __name__ == "__main__":
    main()