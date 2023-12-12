#!/usr/bin/python3
"""Programm contains the entry point of the command interpreter.
"""
import cmd
import re
import json
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.city import City

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
    def do_create(self, arg):
        """Creates a new instance of BaseModel and save it.
        """
    if arg == "" or arg is None:
        print("** class name missing **")
    elif arg not in storage.classes():
        print("** class doesn't exist **")
    else:
        d =  storage.classes()[arg]()
        d.save()
        print(b.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id.
        """
        if arg == "" or arg is None:
            print("** class name missing **")
        else:
            wrd = arg.split(' ')
        if wrd[0] not in storage.classes():
            print("** class doesn't exist **")
        elif len(wrd) < 2:
            print("** instance id missing **")
        else:
            name = "{}.{}".format(wrd[0], wrd[1])
            if name not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[name])

    def do_destroy(self, arg):
        """ Deletes an instance based on the class name and save it.
        """
        if arg == "" or arg is None:
             print("** class name missing **")
        else:
             wrd = arg.split(' ')
             if wrd[0] not in storage.classes():
                 print("** class doesn't exist **")
             elif len(wrd) < 2:
                 print("** instance id missing **")
             else:
                 name = "{}.{}".format(wrd[0], wrd[1])
                 if name not in storage.all():
                      print("** no instance found **")
                 else:
                      del storage.all()[name]
                      storage.save()

    def do_all(self, arg):
         """Method Print all string representation  all instance
         """
         if arg != "":
             wrd = arg.split(' ')
             if wrd[0] not in storage.classes():
                  print("** class doesn't exist **")
             else:
                  als = [str(obj) for key, obj in storage.all().items()
                  if type(obj).__name__ == wrd[0]]
                  print(als)
         else:
                  nw_list = [str(obj) for key, obj in storage.all().items()]
                  print(nw_list)

    def do_update(self, arg):
          """Updates an instance based on the class name and id and save.
          """
          wrd = shlex.split(arg)
          if arg == "" or arg is None:
            print("** class name missing **")
            return

          rex = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(?:(\S)+)))?)?)?'
          mat = re.search(rex, arg)
          classename = mat.grp(1)
          uid = mat.grp(2)
          attribute = mat.grp(3)
          value = mat.grp(4)
          if not mat:
              print("** class name missing **")
          elif classename not in storage.classes():
              print("** class doesn't exist **")
          elif uid is None:
              print("** instance id missing **")
          else:
              key = "{}.{}".format(classename, uid)
              if name not in storage.all():
                  print("** no instance found **")
              elif not attribute:
                  print("** attribute name missing **")
              elif not value:
                  print("** value missing **")
              else:
                  ct = None
              if not re.search('^".*"$', value):
                  if '.' in value:
                      ct = float
                  else:
                      ct = int
              else:
                      value = value.replace('"', '')
                      attributs = storage.attributs()[classename]
                      if attribute in attributs:
                          value = attributs[attribute](value)
                      elif ct:
                          try:
                              value = ct(value)
                          except ValueError:
                              pass
                          setattr(storage.all()[key], attribute, value)
                          storage.all()[key].save()

def do_count(self, arg):
    """Counts the numbers of instances
    """
    wrd = arg.split(' ')
    if not wrd[0]:
        print("** class name missing **")
    elif wrd[0] not in storage.classes():
        print("** class doesn't exist **")
    else:
        mat = [
                j for j in storage.all() if j.startswith(
                    wrd[0] + '.')]
        print(len(mat))

def default(self, line):
        """check commands if nothing else matche """
        self._precmd

if __name__ == '__main__':
    HBNBCommand().cmdloop()
