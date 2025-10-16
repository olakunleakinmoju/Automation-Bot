import shutil
import time
from watchdog.events import FileSystemEvent, FileSystemEventHandler
from watchdog.observers import Observer
import os
import subprocess
filepath = r'C:\Users\WGG\Documents\BOTFILES'
download_dc = r'C:\Users\WGG\Downloads'
MAIN_SHOP_SALES= r"C:\Users\WGG\Downloads\salesbyshop.xlsx"
MAIN_BRANCH_SALES = r"C:\Users\WGG\Downloads\salesbybranch.xlsx"


class Watcher(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory and event.src_path.endswith('.tmp'):
            print(event.src_path, "tmp File Created")
            path_to_file = event.src_path
            print(path_to_file)
            time.sleep(5)
            self.check_for_new_excel_file()

    def check_for_new_excel_file(self):
        files = [f for f in os.listdir(filepath) if f.endswith(".xlsx")]
        print(files)
        if not files:
            print("File not found")
            return
        latest_file = max([os.path.join(filepath, f) for f in files], key=os.path.getctime)
        print(f"Found Latest Excel File{latest_file}")
        if "shop_export" in latest_file:
            shutil.copy(latest_file, MAIN_SHOP_SALES)
            print("The change has been made for shop_export")
            if os.path.exists(latest_file):
                os.remove(latest_file)
                print("The shop file has been deleted")
        elif "branch_export" in latest_file:
            shutil.copy(latest_file, MAIN_BRANCH_SALES)
            print("The change has been made for branch_export")
            if os.path.exists(latest_file):
                os.remove(latest_file)
                print("The branch file has been deleted")
    def on_moved(self, event):
        if not event.is_directory:
            print(event.dest_path, "File Moved")
            path_to_file = event.dest_path
            print(path_to_file)
            if path_to_file.endswith("shop_export.xlsx"):
                 time.sleep(5)
                 print(path_to_file)
                 path_to_file = fr'{path_to_file}'
                 print("This is the new file")
                 shutil.copy(path_to_file, MAIN_SHOP_SALES)
                 print("The change has been made for shop_export")
                 if os.path.exists(path_to_file):
                    os.remove(path_to_file)
                    print("The file has been deleted")
                 else:
                     print("The file doesn't exist")
            elif event.src_path.endswith(".xlsx") and event.src_path.startswith(r'C:\Users\WGG\Documents\BOTFILES\branch_export'):
                time.sleep(5)
                path_to_file = event.src_path[:-11]
                print(path_to_file)
                path_to_file = fr'{path_to_file}'
                print("This is the new file")
                shutil.copy(path_to_file, MAIN_BRANCH_SALES)
                print("The change has been made for branch_export")
                if os.path.exists(path_to_file):
                    os.remove(path_to_file)
                    print("The file has been deleted")
                else:
                    print("The file doesn't exist")
    def on_deleted(self, event):
        if not event.is_directory:
            print(event.src_path, "File Deleted")
event_handler = Watcher()
observer = Observer()
observer.schedule(event_handler, path=filepath, recursive=True)
observer.schedule(event_handler, download_dc, recursive=True)
observer.start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
