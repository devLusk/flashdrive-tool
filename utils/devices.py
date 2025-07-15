import subprocess

def list_devices():
    print("\nDetected disks and partitions:")
    completed_process = subprocess.run('lsblk -o NAME,SIZE,TYPE,MOUNTPOINT | grep -E "disk|part"', shell=True, capture_output=True)

    # aa = completed_process.stdout
    # aa = aa.decode('utf-8')

    # print(aa)