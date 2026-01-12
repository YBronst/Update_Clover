#!/usr/bin/env python3

import os
from config import LOGFILE, SCRIPT_DIR
from utils import check_environment, check_dependencies, cleanup, CloverUpdateError
from efi_handler import list_all_efi, backup_efi
from utils import download_ocbinarydata
from clover_updater import download_clover
from logger import logger, GREEN, load_translations
from menu import exibir_menu

def main():
    """Main function of the script."""
    try:
        # Loads translations based on system language or uses English as default
        load_translations("")

        check_environment()
        check_dependencies()

        # Downloads Clover only once and obtains the ZIP file path
        clover_zip_path = os.path.join(SCRIPT_DIR, "Clover.zip")
        download_clover(clover_zip_path)
        ocbinarydata_dir = download_ocbinarydata()

        efi_dir = list_all_efi()  # Gets the EFI_DIR value returned by list_all_efi

        # If EFI_DIR is defined, proceed with backup and menu
        if efi_dir:
            backup_efi()
            exibir_menu(efi_dir, clover_zip_path)
            logger("update_successful", GREEN)  # Success message
        else:
            logger("error_efi_dir_not_defined", RED)  # Error message

    except SystemExit as se:
        if se.code != 0:
            logger("script_error", RED)
    except CloverUpdateError as e:
        logger("error", RED, error=e)  # Formatted error message
    except Exception as e:
        logger("unexpected_error", RED, error=e)  # Formatted error message
    finally:
        cleanup()
        logger("logs_saved", None, logfile=LOGFILE)  # Log message

if __name__ == "__main__":
    main()
