import os
import sys
from util.record import is_record, record

if len(sys.argv) == 2:
    if is_record(sys.argv[1]):
        if os.path.exists(record(sys.argv[1])):
            os.remove(record(sys.argv[1]))
            print("[INFO] Record removed from storage.")
        else:
            print("[WARNING] Record was not found.")
    else:
        print("[ERROR 3] ILLEGAL FILENAME")
else:
    print("[ERROR 1] ILLEGAL ARGUMENTS")
