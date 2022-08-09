import os.path
import sys
from sort import arrange_folder
def main():
    try:
        target_folder = sys.argv[1]
    except IndexError:
        print("Target folder doesn't defined!")
        return
    if not os.path.exists(target_folder):
        print("Bad path")
    arrange_folder(target_folder, target_folder)

if __name__ == "__main__":
    main()