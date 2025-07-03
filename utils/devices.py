import subprocess

def list_devices():
    print("\nDetected disks and partitions:")
    subprocess.run('lsblk -o NAME,SIZE,TYPE,MOUNTPOINT | grep -E "disk|part"', shell=True)