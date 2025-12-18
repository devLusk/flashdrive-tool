#!/usr/bin/env bash

echo "========================================"
echo " Flashdrive Tool - Setup & Launch Script "
echo "========================================"
echo
echo "This script will perform the following actions:"
echo
echo "  • Install required system packages (python3, python3-venv, python3-tk)"
echo "  • Create a Python virtual environment (venv) if it does not exist"
echo "  • Install Python dependencies from requirements.txt"
echo "  • Launch the application with administrator privileges"
echo
echo "⚠️  This tool requires administrator (sudo) access"
echo "    because it performs operations that can modify system devices."
echo
read -p "Do you want to continue? [y/N]: " CONFIRM

case "$CONFIRM" in
  y|Y|yes|YES)
    echo "Proceeding with setup..."
    ;;
  *)
    echo "Aborted by user."
    exit 0
    ;;
esac

echo

if [[ "$EUID" -ne 0 ]]; then
  echo "Re-running script with sudo..."
  exec sudo "$0" "$@"
fi

echo "Installing system dependencies..."
apt update
apt install -y python3 python3-venv python3-tk

if [ ! -d "venv" ]; then
  echo "Creating virtual environment..."
  python3 -m venv venv
else
  echo "Virtual environment already exists."
fi

echo "Activating virtual environment..."
source venv/bin/activate

echo "Installing Python dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo
echo "Starting Flashdrive Tool..."
echo "----------------------------------------"
python main.py
