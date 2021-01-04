from a2j.version import version
from a2j.commands import get_commands


def print_help(arguments):
    print("aoe2record-to-json version: " + version)
    print("\nAvailable functions:\n")
    print("\tappend <record> <content>")
    print("\thelp")
    print("\tparse <record> <command> [...]")
    print("\tremove <record>")

    print("\nAvailable commands:\n")
    length = 0

    for key in get_commands().keys():
        length += len(key)
        if length > 80:
            print(key)
            length = 0
        else:
            if length == len(key):
                print("\t", end="")
            print(key + ", ", end="")
