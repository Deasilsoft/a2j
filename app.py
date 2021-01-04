import sys

from a2j.append import append
from a2j.help import print_help
from a2j.parse import parse
from a2j.remove import remove

default = "help"

functions = {
    "help": print_help,
}

if len(sys.argv) == 1:
    sys.argv.append(default)

elif len(sys.argv) == 3:
    functions = {
        "help": print_help,
        "remove": remove,
    }

elif len(sys.argv) == 4:
    functions = {
        "help": print_help,
        "append": append,
        "parse": parse,
    }

elif len(sys.argv) > 4:
    functions = {
        "help": print_help,
        "parse": parse,
    }

functions.get(sys.argv[1] if sys.argv[1] in functions else default)(sys.argv)
