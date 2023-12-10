#!/usr/bin/python3
"""Programm contains the entry point of the command interpreter."""
import cmd
import re
import json

class HBNBCommand(cmd.Cmd):
    """The class for the commande interperter of our app."""

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
         """Prints all string representation of all instances based or not on the class name.
         """
         if arg != "":
             wrd = arg.split(' ')
             if wrd[0] not in storage.classes():
                  print("** class doesn't exist **")
             else:
                  alls = [str(obj) for name, obj in storage.all().items()
                          if type(obj).__name__ == wrd[0]]
                  print(alls)
         else:
                  nw_list = [str(obj) for name, obj in storage.all().items()]
                  print(nw_list)

    def do_update(self, arg):
          """Updates an instance based on the class name and id and save.
          """
          wrd = shlex.split(arg)

          if arg == "" or arg is None:
                print("** class name missing **")
                return
          elif wrd[0] not in self.valid_classes:
                print("** class doesn't exist **")
          elif len(wrd) < 2:
                 print("** instance id missing **")
          else:
                 objects = storage.all()

                 name = "{}.{}".format(wrd[0], wrd[1])
                 if name not in objects:
                      print("** no instance found **")
                 elif len(wrd) < 3:
                          print("** attribute name missing **")
                 elif len(wrd) < 4:
                          print("** value missing **")
                 else:
                          obj = objects[name]

                          att_name = wrd[2]
                          att_value = wrd[3]

                          try:
                              att_value = eval(att_value)
                          except Exception:
                              pass
                          setattr(obj, att_name, att_value)

                          obj.save()

    def do_count(self, arg):
         """Count and retrieves the instance of a class.
         """

         objects = storage.all()

         wrd = arg.split(' ')
         if not wrd[0]:
            print("** class name missing **")
         elif words[0] not in storage.classes():
             print("** class doesn't exist **")
         else:
             match = [
                     j for j in objects if j.startswith(wrd[0]+ '.')]
             print(len(match))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
