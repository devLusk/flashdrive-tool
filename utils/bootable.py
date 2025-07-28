import customtkinter as ctk
import subprocess
import os

def create_bootable():
    ctk.set_appearance_mode("system")

    window = ctk.CTkToplevel()
    window.title("USB Toolkit")
    window.geometry("500x460")
    window.maxsize(width=600, height=350)
    window.minsize(width=500, height=460)

    # UI Widgets
    ctk.CTkLabel(window, text="Create Bootable USB", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=10)

    # Bootable frame
    bootable_frame = ctk.CTkFrame(window)
    bootable_frame.pack(fill="x", padx=20, ipady=10)
    bootable_frame.columnconfigure(0, weight=1)

    # ISO Path
    ctk.CTkLabel(bootable_frame, text="ISO file:").grid(row=0, column=0, padx=20, pady=5)
    iso_entry = ctk.CTkEntry(bootable_frame, placeholder_text="e.g., ~/Downloads/kubuntu.iso")
    iso_entry.grid(row=1, column=0, padx=20, ipadx=10, ipady=5, sticky="ew")

    # Target Disk
    ctk.CTkLabel(bootable_frame, text="Target disk:").grid(row=2, column=0, padx=20, pady=5)
    disk_entry = ctk.CTkEntry(bootable_frame, placeholder_text="e.g., sdb")
    disk_entry.grid(row=3, column=0, padx=20, ipadx=10, ipady=5, sticky="ew")

    # Confirmation
    ctk.CTkLabel(bootable_frame, text="Type YES to confirm").grid(row=4, column=0, padx=20, pady=5)
    confirm_entry = ctk.CTkEntry(bootable_frame, placeholder_text="YES")
    confirm_entry.grid(row=5, column=0, padx=20, ipadx=10, ipady=5, sticky="ew")

    # Action Button
    start_button = ctk.CTkButton(bootable_frame, text="Create Bootable USB")
    start_button.grid(row=6, column=0, padx=20, pady=10, ipadx=10, ipady=5, sticky="ew")

    # Output Frame
    output_frame = ctk.CTkFrame(window)
    output_frame.pack(fill="x", padx=20, pady=10, ipady=10)

    output_label = ctk.CTkLabel(output_frame, text="Status: Waiting for user input...")
    output_label.pack(pady=10)

    # iso_path = input("Path of ISO file (e.g. ~/Downloads/Kubuntu.iso): ")
    # iso_path = os.path.expanduser(iso_path)

    # disk_raw = input(f"\nEnter the disk identifier (e.g. sda): ")
    # disk = f"/dev/{disk_raw}"

    # print(f"\nWarning: all data on {disk} will be deleted.")
    # confirmation = input("To proceed, type 'YES' to confirm: ")

    # if confirmation in ("yes", "YES"):
    #     subprocess.run(f'sudo umount {disk}* 2>/dev/null', shell=True)

    #     if not os.path.isfile(iso_path):
    #         print(f"Error: ISO file not found in {iso_path}")
    #     else:
    #         print(f"\nRecording ISO, please wait...")
    #         subprocess.run(f'sudo dd if={iso_path} of={disk} bs=4M status=progress oflag=sync', shell=True)
    #         print("Finished. USB created with the image.")
    # else:
    #     print("Canceled...")

    # input("Press ENTER to return to the menu...")