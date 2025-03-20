import os
import platform

# Устанавливаем переменные окружения
if platform.system() == "Windows":
    os.system("set DADATA_API_KEY=22c19a422cfd50cd909e399e33698ce7ccd29421")
    os.system("set DADATA_SECRET_KEY=a38d4f3165359b6afc57968bf0d08c5ba6ec9490")
else:
    os.system("export DADATA_API_KEY=22c19a422cfd50cd909e399e33698ce7ccd29421")
    os.system("export DADATA_SECRET_KEY=a38d4f3165359b6afc57968bf0d08c5ba6ec9490")

# Очистка терминала
if platform.system() == "Windows":
    os.system("cls")
else:
    os.system("clear")

# Удаление старой версии metelity (если установлена)
os.system("python3 -m pip uninstall -y metelity")

# Очистка кеша pip
os.system("python3 -m pip cache purge")

# Установка metelity
os.system("python3 -m pip install .")

# Очистка терминала
if platform.system() == "Windows":
    os.system("cls")
else:
    os.system("clear")

print("[!] Metelity Installed!")