#!/bin/bash

# Path to the script directory
cd "$(dirname "$0")"

# Checks if Python 3 is installed
if ! command -v python3 &> /dev/null; then

echo "Python 3 not found. Please install it before continuing."
exit 1
fi

# Installs dependencies automatically (if necessary)
echo "Checking dependencies..."
python3 -m pip install --quiet -r requirements.txt

# Executes the main script
echo "Starting Clover Updater..."
python3 main.py

import os
from config import LOGFILE, SCRIPT_DIR
from utils import check_environment, check_dependencies, cleanup, CloverUpdateError
from efi_handler import list_all_efi, backup_efi
from clover_updater import download_clover
from logger import logger, GREEN, load_translations
from menu import exibir_menu

def main():

""Main function of the script."""

try:

# Loads system language translations or uses English as default
load_translations("")

check_environment()

check_dependencies()

# Downloads the Clover only once and gets the file path

clover_zip_path = os.path.join(SCRIPT_DIR, "Clover.zip")

download_clover(clover_zip_path)

efi_dir = list_all_efi() # Get the value of EFI_DIR returned by list_all_efi

# If EFI_DIR is set, proceed with backup and menu

if efi_dir:
backup_efi()
display_menu(efi_dir, clover_zip_path)

logger("update_successful", GREEN) # Success message

else:

logger("error_efi_dir_not_defined", RED) # Error message

except SystemExit as se:

if se.code != 0:

logger("script_error", RED)

except CloverUpdateError as e:

logger("error", RED, error=e) # Formatted error message

except Exception as e:

logger("unexpected_error", RED, error=e) # Formatted error message

finally:

cleanup()

logger("logs_saved", None, logfile=LOGFILE) # Log message

if __name__ == "__main__":
main()