#!/usr/bin/python3
"""
Module for console
"""
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.amenty import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand console class
    """
    prompt = "(hbnb) "
    # storage = FileStorage()
    valid_classnames = [
        "BaseModel", "User", "Place",
        "State", "City", "Amenity", "Review"
    ]

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """
        EOF (Ctrl+D) signal to exit the program.
        """
        return True

    def emptyline(self):
        """
        Do nothing when an empty line is entered.
        """
        pass

    def do_create(self, arg):
        """
        Create a new instance of BaseModel and save it to the JSON file.
        Usage: create <class_name>
        """
        arg = arg.split()
        # print(arg)
        if not arg:
            print("** class name missing **")
            return
        if arg[0] in HBNBCommand.valid_classnames:
            new_instance = eval(f"{arg[0]}()")
            new_instance.save()
            print(new_instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Show the string representation of an instance.
        Usage: show <class_name> <id>
        """
        arg = arg.split()
        # print(arg)
        if not arg:
            print("** class name missing **")
            return
        if arg[0] in HBNBCommand.valid_classnames:
            if len(arg) > 1:
                storage = FileStorage()
                objs = storage.all()
                for key, value in objs.items():
                    class_name, obj_id = key.split(".")
                    if (arg[0] == class_name) and (arg[1] == obj_id):
                        print(value)
                        return
                print("** no instance found **")

            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """
        Delete an instance based on the class name and id.
        Usage: destroy <class_name> <id>
        """
        arg = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if arg[0] in HBNBCommand.valid_classnames:
            if len(arg) > 1:
                storage = FileStorage()
                objs = storage.all()
                for key, value in objs.items():
                    class_name, obj_id = key.split(".")
                    if (arg[0] == class_name) and (arg[1] == obj_id):
                        del objs[key]
                        storage.save()
                        return
                print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """
        Print the string representation of all instances or a specific class.
        Usage: <User>.all()
                <User>.show()
        """
        arg = arg.split()
        storage = FileStorage()
        objs_list = []
        objs = storage.all()
        if len(arg) == 0:
            for key, value in objs.items():
                print(str(value))
            # print(objs_list)
        else:
            for key, value in objs.items():
                class_name, obj_id = key.split(".")
                if arg[0] == class_name:
                    print(str(value))
            # print(objs_list)

    def do_update(self, arg):
        """
        Update an instance by adding or updating an attribute.
        Usage: update <class_name> <id> <attribute_name> "<attribute_value>"
        """
        storage = FileStorage()
        arg = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if arg[0] in HBNBCommand.valid_classnames:
            if len(arg) > 1:
                storage = FileStorage()
                objs = storage.all()
                for key, value in objs.items():
                    class_name, obj_id = key.split(".")
                    if (arg[0] == class_name) and (arg[1] == obj_id):
                        if len(arg) > 2:
                            if len(arg) <= 3:
                                print("** value missing **")
                                return
                            try:
                                atttribute_name = arg[2]
                                attribute_value = arg[3]
                            except Exception:
                                pass

                            try:
                                attribute_value = eval(attribute_value)
                            except:
                                pass
                            setattr(value, atttribute_name, attribute_value)
                            return
                        else:
                            print("** attribute name missing **")
                            return

                        # del objs[key]
                        # storage.save()
                        # print(objs)
                print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_count(self, arg):
        """
        Counts and retrieves the number of instances of a class
        usage: <class name>.count()
        """
        arg = arg.split()
        storage = FileStorage()
        objs_counter = 0
        objs = storage.all()
        if len(arg) == 0:
            print("** class name missing **")
        else:
            if arg[0] in self.valid_classnames:
                for key, value in objs.items():
                    class_name, obj_id = key.split(".")
                    if arg[0] == class_name:
                        objs_counter += 1
            else:
                print("** invalid class name **")
            if objs_counter == 0:
                return
            print(objs_counter)

    def default(self, arg):
        """
        Default behavior for cmd module when input is invalid
        """
        if "." in arg and "(" and ")" in arg:
            arg_list = arg.split('.')
            command = arg_list[1].split("(")
            incoming_method = command[0]
            arg_class = arg_list[0]
        else:
            incoming_method = arg
            arg_list = ''
            incoming_arg = ''
            arg_class = ''

        method_dict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "update": self.do_update,
            "count": self.do_count
        }

        if incoming_method in method_dict.keys():
            if incoming_method == "count":
                return method_dict[incoming_method]("{}".format(arg_class))
            else:
                incoming_arg = command[1].replace(")", "")
                incoming_arg = incoming_arg.replace('"', '')
                incoming_arg = incoming_arg.replace(',', '')
                return method_dict[incoming_method]("{} {}".format(arg_class, incoming_arg))
        else:
            print("*** Unknown syntax: {}".format(arg))
            return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
