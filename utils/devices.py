import customtkinter as ctk
import subprocess

def list_devices():
    ctk.set_appearance_mode("system")   

    window = ctk.CTkToplevel()
    window.title("USB Toolkit")
    window.geometry("450x300")
    window.maxsize(width=600, height=350)
    window.minsize(width=500, height=370)

    ctk.CTkLabel(window, text="Detected Devices", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=10)

    result = subprocess.run(
        'lsblk -o NAME,SIZE,TYPE,MOUNTPOINT | grep -E "disk|part"',
        shell=True,
        capture_output=True,
        text=True
    )

    text_box = ctk.CTkTextbox(window, width=400, height=250)
    text_box.pack(padx=10, pady=10)
    text_box.insert("1.0", "Detected Devices:\n\n" + result.stdout)
    text_box.configure(state="disabled")