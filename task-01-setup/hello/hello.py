import sys
import platform


def main() -> None:
    print("Привет, мир!")
    print(f"Python: {sys.version.split()[0]}")
    print(f"Платформа: {platform.system()} {platform.release()}")
    print(f"Аргументы: {sys.argv[1:]}")


if __name__ == "__main__":
    main()
