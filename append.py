import sys
import os
from util.record import is_record, record

if len(sys.argv) == 3:
    if is_record(sys.argv[1]):
        if not os.path.exists(record(sys.argv[1])):
            print("[INFO] Creating file...")
            with open(record(sys.argv[1]), "w") as file:
                file.write(sys.argv[2])
                file.close()
            print("[INFO] File created with initial string.")
        else:
            print("[INFO] Opening file...")
            with open(record(sys.argv[1]), "a") as file:
                file.write(sys.argv[2])
                file.close()
            print("[INFO] File appended with new string.")
    else:
        print("[ERROR 3] ILLEGAL FILENAME")
else:
    print("[ERROR 1] ILLEGAL ARGUMENTS")
