# Update Clover Script

This Python script automates the process of updating your Clover bootloader to the latest version available in the [YBronst/CloverBootloader](https://github.com/YBronst/CloverBootloader) repository. It was developed to simplify and speed up the update process, making it more accessible for Hackintosh community users.

---

## Features

- **Automatic Language Detection:** Automatically detects the system language (Portuguese or English) and displays messages accordingly. Messages are stored in JSON files in the `translations` folder to make adding other languages easier.
- **Interactive Menu:** Allows choosing what to update:
  - Update **BOOTX64.efi** and **CLOVERX64.efi**
  - Update **UEFI Drivers**
  - Perform a **Full Update**
  - Exit
- **Environment Check:** Ensures the script is running on macOS.
- **Dependency Check:** Verifies that the required commands are installed:
  - `curl`
  - `unzip`
  - `/usr/libexec/PlistBuddy`
  - `installer`
- **Smart Download:** Downloads the Clover release once and reuses it for all operations.
- **Bootloader Detection:** Confirms Clover is installed on the selected EFI partition and aborts if OpenCore or Windows Boot Manager is detected.
- **Mount Wait:** If the EFI partition is not mounted, the script waits until you mount it manually.
- **EFI Backup:** Creates a full backup before making changes. Backups are stored in `~/EFI_BACKUPS`, named by date and time.
- **Safe Update:** Ensures EFI is mounted read/write before updating.
- **Error Handling:** Uses a custom `CloverUpdateError` exception for clear and informative error reporting.
- **Detailed Logging:** Saves an `update_clover_[timestamp].log` file with all actions.
- **Cleanup:** Removes temporary downloaded files.
- **Internationalization:** Supports Portuguese (pt-BR) and English (en-US). Falls back to Portuguese if language detection fails.

---

## Prerequisites

- **macOS**
- **Python 3**
- Uses only Python’s standard library (no external modules required)
- Required macOS utilities installed:
  - `curl`
  - `unzip`
  - `/usr/libexec/PlistBuddy`
  - `installer`
- **Internet connection**
- **Mounted EFI Partition**
  - Mount with:
    ```bash
    diskutil mount <partition_identifier>
    ```
    Example:
    ```bash
    diskutil mount disk0s1
    ```

---

## How to Run

1. **Download the Script**
   Download:
   - `main.py`
   - `clover_updater.py`
   - `config.py`
   - `efi_handler.py`
   - `logger.py`
   - `menu.py`
   - `utils.py`
   - `translations` folder

2. **Place Files**
   Extract everything into a single folder, for example:
   ```
   update_clover
   ```

3. **Make Executable**
   ```bash
   chmod +x main.py
   ```

4. **Run with Administrator Privileges**
   ```bash
   sudo python3 main.py
   ```

5. **Follow On-Screen Instructions**
   - Select the EFI partition
   - Ensure it is mounted
   - EFI backup is created
   - Choose update options
   - Track progress in Terminal and in:
     ```
     update_clover_[timestamp].log
     ```

---

## Interactive Menu

1. Update BOOTX64.efi and CLOVERX64.efi  
2. Update UEFI Drivers  
3. Full Update  
4. Exit  

---

## Important Notes

- **Always back up EFI manually as well**
- Only **updates existing UEFI drivers**
- Does **not** install new drivers
- Preserves original Clover file modification dates
- Tested on: macOS Ventura 13.6.3

---

## Troubleshooting

- **Permission Errors**
  - Run using `sudo`
- **Download Failure**
  - Check internet connection
- **EFI Partition Not Mounted**
  ```bash
  diskutil mount <partition_identifier>
  ```
- **EFI Partition Read-Only**
  - Unmount and remount
  - If problem persists, seek Hackintosh community support

---

## Contributions

Contributions are welcome!  
Submit a Pull Request with improvements or fixes.

---

## Credits

- **Clover Developers / Slice** — Clover Bootloader  
- **Hackintosh Community** — Shared knowledge and support  
- **Henrique / hnanoto** — Script creator  

---

## Disclaimer

This script is provided **“as is”**, without warranty of any kind.  
Use at your own risk.  
Always make a full system backup before modifying EFI.

---

## Automatic Language Detection Update

The script now supports multilingual messages via JSON translation files.  
Currently supports:
- Portuguese
- English

## Credits
- [Thanks to hnanoto!](https://github.com/hnanoto)
