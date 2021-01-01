import sys
import os
from util.filename import filename

if len(sys.argv) == 3:
    if filename(sys.argv[1]):
        if not os.path.exists(sys.argv[1]):
            print("[INFO] Creating file...")
            # TODO: create file
        else:
            print("[INFO] Opening file...")
            # TODO: append to file
    else:
        print("[ERROR 3] ILLEGAL FILENAME")
else:
    print("[ERROR 1] ILLEGAL ARGUMENTS")
