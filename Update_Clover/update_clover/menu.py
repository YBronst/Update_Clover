#!/usr/bin/env python3
from efi_handler import EFI_DIR, is_efi_read_only
from logger import logger, YELLOW, RED, GREEN
from clover_updater import (
    update_bootx64,
    update_cloverx64,
    update_clover_drivers,
)
import sys

def exibir_menu(efi_dir, clover_zip_path):
    """Exibe o menu principal e obtém a escolha do usuário."""
    while True:
        # Exibe o menu com as mensagens traduzidas
        print("\n=== " + logger("clover_update_menu", YELLOW, return_message=True) + " ===")
        print(logger("option_update_boot_clover", YELLOW, return_message=True))
        print(logger("option_update_drivers", YELLOW, return_message=True))
        print(logger("option_update_all", YELLOW, return_message=True))
        print(logger("option_exit", YELLOW, return_message=True))

        escolha = input("\n" + logger("choose_option", YELLOW, return_message=True) + " ")

        # Verify that the EFI partition is mounted before proceeding.
        if not is_efi_read_only(efi_dir):
            logger("efi_ready", GREEN, efi_dir=efi_dir)
        else:
            logger("efi_not_writable", RED, efi_dir=efi_dir)
            continue

        if escolha == "1":
            atualizar_boot_clover(efi_dir, clover_zip_path)
        elif escolha == "2":
            atualizar_drivers(efi_dir, clover_zip_path)
        elif escolha == "3":
            atualizar_tudo(efi_dir, clover_zip_path)
        elif escolha == "4":
            logger("exiting", YELLOW)
            sys.exit(0)
        else:
            logger("invalid_option", RED)

def atualizar_bootx64(efi_dir, clover_zip_path):
    """Update the BOOTX64.efi file on the EFI partition."""
    logger("start_update_bootx64", YELLOW)
    try:
        update_bootx64(efi_dir, clover_zip_path)
        logger("success_update_bootx64", GREEN)
    except Exception as e:
        logger("error_updating_bootx64", RED, error=e)

def atualizar_cloverx64(efi_dir, clover_zip_path):
    """Update the CLOVERX64.efi file on the EFI partition."""
    logger("start_update_cloverx64", YELLOW)
    try:
        update_cloverx64(efi_dir, clover_zip_path)
        logger("success_update_cloverx64", GREEN)
    except Exception as e:
        logger("error_updating_cloverx64", RED, error=e)

def atualizar_drivers(efi_dir, clover_zip_path):
    """Update the UEFI drivers on the EFI partition."""
    logger("start_update_drivers", YELLOW)
    try:
        update_clover_drivers(efi_dir, clover_zip_path)
        logger("uefi_drivers_update_success", GREEN)
    except Exception as e:
        logger("error_updating_drivers", RED, error=e)

def atualizar_tudo(efi_dir, clover_zip_path):
    """Update all Clover components (BOOTX64.efi, CLOVER X64.uefi, and drivers)."""
    logger("start_full_update", YELLOW)
    try:
        atualizar_boot_clover(efi_dir, clover_zip_path)
        atualizar_drivers(efi_dir, clover_zip_path)
        logger("full_update_success", GREEN)
    except Exception as e:
        logger("error_updating_clover", RED, error=e)

def atualizar_boot_clover(efi_dir, clover_zip_path):
    """Updates the BOOTX64.efi and CLOVERX64.efi files on the EFI partition."""
    logger("start_update_boot_clover", YELLOW)
    try:
        update_bootx64(efi_dir, clover_zip_path)
        update_cloverx64(efi_dir, clover_zip_path)
        logger("boot_clover_update_success", GREEN)
    except Exception as e:
        logger("boot_clover_update_error", RED, error=e)
