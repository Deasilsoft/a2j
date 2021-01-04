import sys

from a2j.help import print_help
from a2j.parse import parse

READ = "help"

functions = {
    "help": print_help,
}

if len(sys.argv) == 1:
    sys.argv.append(READ)

elif len(sys.argv) > 3:
    functions = {
        "help": print_help,
        "parse": parse,
    }

functions.get(sys.argv[1] if sys.argv[1] in functions else READ)(sys.argv)
