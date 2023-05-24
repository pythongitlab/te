import shutil
import os
import datetime
import time

folder_path = 'C:/Test' # замените на путь к нужной папке

while True:
    now = datetime.datetime.now()
    if now.hour == 10 and now.minute == 46:
        try:
            shutil.rmtree(folder_path)
            print(f"Папка {folder_path} удалена в {now}")
        except Exception as e:
            print(f"Ошибка при удалении папки: {e}")
    time.sleep(60)