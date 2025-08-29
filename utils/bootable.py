import customtkinter as ctk
import subprocess
import os
from utils.devices import list_devices

def create_bootable():
    ctk.set_appearance_mode("system")

    window = ctk.CTkToplevel()
    window.title("USB Toolkit")
    window.geometry("500x460")
    window.maxsize(width=600, height=350)
    window.minsize(width=500, height=460)

    def on_create_bootable_click():
        iso = iso_entry.get()
        target = disk_entry.get().lower()
        confirm = confirm_entry.get().lower()

        iso_path = os.path.expanduser(iso)
        disk = f"/dev/{target}"

        if not os.path.isfile(iso_path):
            output_label.configure(text=f"Error: ISO not found")
            return
        
        if not target:
            output_label.configure(text="Error: Please specify a target.", text_color="red")
            return


        if confirm != "yes":
            output_label.configure(text="Operation cancelled by user.", text_color="red")
            return
        
        try:
            output_label.configure(text="Unmounting disk...")
            window.update_idletasks()
            subprocess.run(f'sudo umount {disk}* 2>/dev/null', shell=True)

            output_label.configure(text="Recording ISO, please wait...")
            window.update_idletasks()
            process = subprocess.run(f'sudo dd if={iso_path} of={disk} bs=4M status=progress oflag=sync', shell=True, check=True)

            if process.returncode == 0:
                output_label.configure(text="Finished! USB created with the image.")

            else:
                output_label.configure(text="Error during USB creation.")
        
        except subprocess.CalledProcessError as e:
            output_label.configure(text=f"Command failed: {e}", text_color="red")
        except Exception as e:
            output_label.configure(text=f"Unexpected error: {e}", text_color="red")

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
    start_button = ctk.CTkButton(bootable_frame, text="Create Bootable USB", command=on_create_bootable_click)
    start_button.grid(row=6, column=0, padx=20, pady=10, ipadx=10, ipady=5, sticky="ew")

    devices_button = ctk.CTkButton(bootable_frame, text="Show Available Disks", command=list_devices)
    devices_button.grid(row=7, column=0, columnspan=2, padx=20, ipadx=10, ipady=5, sticky="ew")

    # Output Frame
    output_frame = ctk.CTkFrame(window)
    output_frame.pack(fill="x", padx=20, pady=10, ipady=10)

    output_label = ctk.CTkLabel(output_frame, text="Status: Waiting for user input...")
    output_label.pack(pady=10)