import os
import time

# Colors for visual feedback
RED = "\033[0;31m"
GREEN = "\033[0;32m"
YELLOW = "\033[0;33m"
NC = "\033[0;m"  # Sem cor

# Absolute path to the script directory
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Log file with timestamp
LOGFILE = os.path.join(SCRIPT_DIR, f"update_clover_{time.strftime('%Y%m%d%H%M%S')}.log")

# Base directory for EFI backups
BACKUP_BASE_DIR = os.path.expanduser("~")

# --- Clover settings ---
# Base URL of the Clover repository (GitHub API)
CLOVER_REPO_URL = "https://api.github.com/repos/YBronst/CloverBootloader/releases/latest"

# Direct download URL (if you want to force a specific version, uncomment below and comment out CLOVER_REPO_URL)
# CLOVER_DOWNLOAD_URL = "https://github.com/hnanoto/CloverBootloader-Hackintosh-and-Beyond/releases/download/5161/CloverV2-5161.zip"

# Minimum acceptable size for the Clover.zip file (in bytes)
MIN_CLOVER_ZIP_SIZE = 1000000  # 1 MB

# Expected SHA256 hash for the Clover.zip file (for integrity verification)
# You will need to calculate the hash of the downloaded file and put it here.
# Example: CLOVER_SHA256 = "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855" # (SHA256 hash of an empty file)
CLOVER_SHA256 = ""  # Leave blank if you do not wish to verify integrity.
