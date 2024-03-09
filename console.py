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
    prompt = "(hbnb) "
    # storage = FileStorage()
    valid_classnames = [
        "BaseModel", "User", "Place",
        "State", "City", "Amenity", "Review"
    ]

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    do_EOF = do_quit

    def do_create(self, arg):
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
                        print(value)
                        return
                print("** no instance found **")

            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
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
                        # print(objs)
                        return
                print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
        arg = arg.split()
        storage = FileStorage()
        objs_list = []
        objs = storage.all()
        for key, value in objs.items():
            objs_list.append(str(value))
        print(objs_list)

    def do_update(self, arg):
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
                                attribute_value = eval(arg[3])
                            except Exception:
                                pass

                            setattr(value, atttribute_name, attribute_value)
                            value.save()
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
            print(f"** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
