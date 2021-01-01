import os
import sys
from util.filename import filename

if len(sys.argv) == 2:
    if filename(sys.argv[1]):
        if os.path.exists(sys.argv[1]):
            os.remove(sys.argv[1])
            print("[INFO] Record removed from storage.")
        else:
            print("[WARNING] Record was not found.")
    else:
        print("[ERROR 3] ILLEGAL FILENAME")
else:
    print("[ERROR 1] ILLEGAL ARGUMENTS")
