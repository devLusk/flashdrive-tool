# USB Formatter and Bootable Creator

This Python application provides a command-line interface for formatting USB flash drives and creating bootable USB drives from ISO files. It is designed to work on Linux systems and requires administrative privileges for certain operations.

## Features
- **List Devices**: Displays all detected disks and partitions using `lsblk`.
- **Format Flash Drive**: Formats a USB drive with a choice of FAT32, NTFS, or EXT4 file systems, allowing the user to set a custom volume label.
- **Create Bootable USB**: Writes an ISO image to a USB drive to create a bootable device using the `dd` command.

## Prerequisites
- **Python 3.x**: Ensure Python is installed on your system.
- **Linux System**: The script is designed for Linux environments.
- **Required Packages**:
  - `lsblk` for listing devices.
  - `parted` for creating partition tables.
  - `wipefs` for wiping disk signatures.
  - `mkfs.vfat`, `mkfs.ntfs`, `mkfs.ext4` for formatting in FAT32, NTFS, or EXT4.
- **Administrative Privileges**: The script uses `sudo` for operations that modify disk data.

## Installation
1. Clone or download the repository to your local machine.
2. Ensure the required Linux packages are installed:
   ```bash
   sudo apt update
   sudo apt install parted ntfs-3g dosfstools e2fsprogs
   ```
3. Place the scripts in a directory with the following structure:
   ```
   project_directory/
   ├── main.py
   └── utils/
       ├── bootable.py
       ├── devices.py
       └── format.py
   ```

## Usage
1. Navigate to the project directory:
   ```bash
   cd path/to/project_directory
   ```
2. Run the main script:
   ```bash
   ./run.sh
   ```
3. Follow the interactive menu to:
   - **Option 1**: Format a USB drive by selecting a disk, partition, file system, and volume label.
   - **Option 2**: Create a bootable USB by providing the path to an ISO file and selecting a disk.
   - **Option 3**: List all detected disks and partitions.
   - **Option 4**: Exit the program.

## Important Notes
- **Data Loss Warning**: Formatting or creating a bootable USB will erase all data on the selected disk. Always double-check the disk identifier before confirming operations.
- **Safety Checks**: The script requires explicit confirmation (`YES`) before performing destructive operations.
- **ISO File**: Ensure the ISO file path is valid when creating a bootable USB.
- **Partition Number**: When formatting, specify the partition number (e.g., `1` for `/dev/sda1`).
- **File System Options**:
  - FAT32: High compatibility across systems.
  - NTFS: Optimized for Windows.
  - EXT4: Preferred for Linux systems.

## Limitations
- The script is Linux-specific due to its reliance on `lsblk`, `parted`, `wipefs`, and `dd`.
- No support for non-Linux systems or advanced partition schemes.
- Requires manual input of disk identifiers and partition numbers, which can be error-prone if the user is not familiar with their system’s disk layout.

## Contributing
Feel free to submit issues or pull requests to improve the script, such as adding error handling, support for other operating systems, or additional features.
