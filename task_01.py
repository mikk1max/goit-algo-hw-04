import sys
from pathlib import Path
import shutil
import os


def find_and_sort_files(source_dir, dest_dir="dist"):
    source_path = Path(source_dir)
    dest_path = Path(dest_dir)

    try:
        dest_path.mkdir(parents=True, exist_ok=True)
    except Exception as e:
        print(f"Не вдалося створити директорію призначення {dest_path}: {e}")
        return

    try:
        for el in source_path.iterdir():
            if el.is_dir():
                find_and_sort_files(el, dest_path)
            elif el.is_file():
                if os.access(el, os.R_OK):
                    try:
                        ext = el.suffix.lower().replace(".", "") or "other"
                        ext_dir = dest_path / ext
                        ext_dir.mkdir(parents=True, exist_ok=True)

                        shutil.copy2(el, ext_dir / el.name)
                        print(f"Скопійовано: {el} -> {ext_dir / el.name}")
                    except Exception as e:
                        print(f"Помилка при копіюванні {el}: {e}")
                else:
                    print(f"Файл {el} недоступний для копіювання (немає прав на читання).")
    except Exception as e:
        print(f"Помилка при читанні директорії {source_path}: {e}")


if __name__ == "__main__":
    try:
        source = sys.argv[1]
    except IndexError:
        print("❌ Помилка: не вказано шлях до вихідної директорії.")
        print("Приклад використання: python script.py \"source_dir\" \"destination_dir\"")
        sys.exit(1)

    dest = sys.argv[2] if len(sys.argv) > 2 else "dist"
    source_path = Path(source)

    if not source_path.exists():
        print(f"❌ Помилка: вихідна директорія {source} не існує.")
        sys.exit(1)

    if not source_path.is_dir():
        print(f"❌ Помилка: {source} не є директорією.")
        sys.exit(1)

    find_and_sort_files(source, dest)
