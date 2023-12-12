#!/usr/bin/python3
"""Programm contains the entry point of the command interpreter.
"""
import cmd
import re
import json


class HBNBCommand(cmd.Cmd):
    """The class for the commande interperter of our app"""

    prompt = "(hbnb)"

    def do_EOF(self, arg):
        """Command that handle the End of file.
        """
        print()
        return True

    def do_quit(self, arg):
        """Quit command that exit the program.
        """
        return True

    def emptyline(self):
        """Command shouldn’t execute anything on ENTER.
        """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
