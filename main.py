import customtkinter as ctk
from utils.bootable import create_bootable
from utils.devices import list_devices
from utils.format import format_flashdrive

def main():
    ctk.set_appearance_mode("system")

    app = ctk.CTk()
    app.title("USB Toolkit")
    app.geometry("500x370")
    app.maxsize(width=600, height=350)
    app.minsize(width=500, height=370)

    def format_drive():
        format_flashdrive()

    def create_boot():
        create_bootable()

    def list_device():
        list_devices()

    ctk.CTkLabel(app, text="USB Management Menu", font=ctk.CTkFont(size=24, weight="bold")).pack(pady=20)

    btn_frame = ctk.CTkFrame(app)
    btn_frame.pack(fill="x", padx=20)

    btn_format = ctk.CTkButton(btn_frame, text="Format USB Drive", command=format_drive)
    btn_format.pack(padx=20, pady=10, ipadx=10, ipady=5, fill="x", expand=True)

    btn_bootable = ctk.CTkButton(btn_frame, text="Create Bootable USB", command=create_boot)
    btn_bootable.pack(padx=20, pady=10, ipadx=10, ipady=5, fill="x", expand=True)

    btn_list = ctk.CTkButton(btn_frame, text="Show Connected Devices", command=list_device)
    btn_list.pack(padx=20, pady=10, ipadx=10, ipady=5, fill="x", expand=True)

    btn_exit = ctk.CTkButton(btn_frame, text="Exit", command=app.destroy)
    btn_exit.pack(padx=20, pady=10, ipadx=10, ipady=5, fill="x", expand=True)

    ctk.CTkLabel(app, text="© 2025 • devLusk", font=ctk.CTkFont(size=12, slant="italic")).pack(pady=20)

    app.mainloop()

if __name__ == "__main__":
    main()