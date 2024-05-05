import os
import shutil
import sys

def main():
    # Перевірка кількості переданих аргументів
    if len(sys.argv) < 2:
        print("Використання: python script.py <шлях_до_вихідної_директорії> [шлях_до_директорії_призначення]")
        sys.exit(1)
    
    source_dir = sys.argv[1]
    dest_dir = sys.argv[2] if len(sys.argv) > 2 else 'dist'

    if not os.path.isdir(source_dir):
        print(f"Помилка: Вихідна директорія '{source_dir}' не існує.")
        sys.exit(1)

    try:
        # Створення директорії призначення, якщо вона не існує
        os.makedirs(dest_dir, exist_ok=True)
        # Виклик функції для копіювання файлів
        copy_files(source_dir, dest_dir)
    except Exception as e:
        print(f"Виникла помилка: {e}")
        sys.exit(1)

def copy_files(current_dir, dest_dir):
    # Рекурсивний обхід всіх елементів у директорії
    for item in os.listdir(current_dir):
        path = os.path.join(current_dir, item)
        if os.path.isdir(path):
            # Рекурсивний виклик функції для директорії
            copy_files(path, dest_dir)
        elif os.path.isfile(path):
            # Отримання розширення файлу і створення піддиректорії
            ext = os.path.splitext(item)[1][1:] if os.path.splitext(item)[1] else 'no_extension'
            ext_dir = os.path.join(dest_dir, ext)
            os.makedirs(ext_dir, exist_ok=True)
            # Копіювання файлу в цільову директорію
            shutil.copy(path, ext_dir)

if __name__ == "__main__":
    main()

