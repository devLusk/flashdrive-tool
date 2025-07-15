import customtkinter as ctk
import subprocess

def format_flashdrive():
    ctk.set_appearance_mode("system")

    app = ctk.CTk()
    app.title("FORMAT FLASH DRIVE")
    app.geometry("500x460")
    app.maxsize(width=600, height=350)
    app.minsize(width=500, height=460)

    def on_format_click():
        disk = disk_entry.get().lower()
        partition = partition_entry.get().lower()
        label = label_entry.get()
        volume = format_volume.get().lower()
        confirmation = confirm_entry.get().lower()

        if not disk:
            output_label.configure(text="Error: Please specify a disk.", text_color="red")
            return
        
        if not label:
            label = "USB_Drive"

        if confirmation != "yes":
            output_label.configure(text="Operation cancelled by user.", text_color="red")
            return
        
        disk = f"/dev/{disk}"
        partition = f"{disk}{partition}"

        try:
            output_label.configure(text="Preparing to format...", text_color="green")

            subprocess.run(f'sudo umount {partition}', shell=True)
            subprocess.run(f'sudo wipefs -a {disk}', shell=True)
            subprocess.run(f'sudo parted -s {disk} mklabel msdos', shell=True)

            if volume == "fat32":
                subprocess.run(f'sudo parted -s -a optimal {disk} mkpart primary fat32 0% 100%', shell=True)
                subprocess.run(f'sudo mkfs.vfat -F 32 -n {label} {partition}', shell=True)
            elif volume == "ntfs":
                subprocess.run(f'sudo parted -s -a optimal {disk} mkpart primary ntfs 0% 100%', shell=True)
                subprocess.run(f'sudo mkfs.ntfs -f -L {label} {partition}', shell=True)
            elif volume == "ext4":
                subprocess.run(f'sudo parted -s -a optimal {disk} mkpart primary ext4 0% 100%', shell=True)
                subprocess.run(f'sudo mkfs.ext4 -L {label} {partition}', shell=True)

            output_label.configure(text="Formatting complete.", text_color="green")

        except subprocess.CalledProcessError as e:
            output_label.configure(text=f"Command failed: {e}", text_color="red")
        except Exception as e:
            output_label.configure(text=f"Unexpected error: {e}", text_color="red")

    # UI Widgets
    ctk.CTkLabel(app, text="Flash Drive Formatter", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=10)

    # Create input frame
    format_frame = ctk.CTkFrame(app)
    format_frame.pack(fill="x", padx=20, ipady=10)
    format_frame.columnconfigure(0, weight=1)
    format_frame.columnconfigure(1, weight=1)

    # Disk Identifier
    ctk.CTkLabel(format_frame, text="Disk Identifier (e.g., sda):").grid(row=0, column=0, padx=20, pady=5)
    disk_entry = ctk.CTkEntry(format_frame, placeholder_text="Example: sda")
    disk_entry.grid(row=1, column=0, padx=20, ipadx=10, ipady=5, sticky="ew")

    # Partition Number
    ctk.CTkLabel(format_frame, text="Partition Number (e.g., 1):").grid(row=0, column=1, padx=20, pady=5)
    partition_entry = ctk.CTkEntry(format_frame, placeholder_text="E.G. 1")
    partition_entry.grid(row=1, column=1, padx=20, ipadx=10, ipady=5, sticky="ew")

    # Volume Label
    ctk.CTkLabel(format_frame, text="Volume Label (optional):").grid(row=2, column=0, padx=20, pady=5)
    label_entry = ctk.CTkEntry(format_frame, placeholder_text="Default: USB_Drive")
    label_entry.grid(row=3, column=0, padx=20, ipadx=10, ipady=5, sticky="ew")

    # File System Option
    ctk.CTkLabel(format_frame, text="File System:").grid(row=2, column=1, padx=20, pady=5)
    format_volume = ctk.CTkComboBox(format_frame, values=["FAT32", "NTFS", "EXT4"])
    format_volume.set("FAT32")
    format_volume.grid(row=3, column=1, padx=20, ipadx=10, ipady=5, sticky="ew")

    # Confirmation
    ctk.CTkLabel(format_frame, text="Confirmation (type YES to proceed):").grid(row=4, column=0, columnspan=2, padx=20, pady=5)
    confirm_entry = ctk.CTkEntry(format_frame, placeholder_text="Type YES to confirm")
    confirm_entry.grid(row=5, column=0, columnspan=2, padx=20, ipadx=10, ipady=5, sticky="ew")

    # Action Buttons
    start_button = ctk.CTkButton(format_frame, text="Format Drive", command=on_format_click)
    start_button.grid(row=6, column=0, columnspan=2, padx=20, pady=10, ipadx=10, ipady=5, sticky="ew")

    devices_button = ctk.CTkButton(format_frame, text="Show Available Disks")
    devices_button.grid(row=7, column=0, columnspan=2, padx=20, ipadx=10, ipady=5, sticky="ew")

    # Output Frame
    output_frame = ctk.CTkFrame(app)
    output_frame.pack(fill="x", padx=20, pady=10, ipady=10)

    output_label = ctk.CTkLabel(output_frame, text="Status: Waiting for user input...")
    output_label.pack(pady=10)

    app.mainloop()

if __name__ == "__main__":
    format_flashdrive()