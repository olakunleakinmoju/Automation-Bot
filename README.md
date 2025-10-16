Hi,
This Python project automates browser actions using Playwright and monitors the Downloads and Bot files folder using Watchdog.  
It detects when new `.xlsx` files are downloaded, moves or copies them to target directories, and cleans up temporary files.

Features
- Automates data downloads with Playwright
- Detects new `.tmp` and `.xlsx` files in real-time
- Automatically renames, copies, and deletes completed files

Technologies Used
- Python 3.10+
- Playwright
- Watchdog
- OS & Shutil
