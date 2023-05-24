import os
import shutil
import schedule
import time

def delete_folder():
    folder_path = "C:/Test" # замените на путь к нужной папке
    shutil.rmtree(folder_path)

schedule.every().day.at("16:42").do(delete_folder)

while True:
    schedule.run_pending()
    time.sleep(1)
    print ('я работаю')
    print ('чекаю готовность')