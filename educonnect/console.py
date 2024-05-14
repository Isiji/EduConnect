#!/usr/bin/python3
"""this the main console for the school project"""
import cmd
from educonnect.engine.storage import DBStorage
import educonnect.engine.storage as storage
from teacher import Teacher
from student import Student
from classroom import Classroom
from base_model import BaseModel
from school import School
from admin_model import Admin
import shlex
from admin_session import admin_session
#classes = {"Teacher": Teacher, "Student": Student, "School": School, "Classroom": Classroom} 


class EduConnectCommand(cmd.Cmd):
    """Main console class"""
    prompt = '(EduConnect).. '
    print("Welcome to the EduConnect Console")
    print("Type help to list commands")
    print("Type quit to exit the console")
    print("Type login to login to the program or admin to start admin session")

    def __init__(self):
        """Initialize the console"""
        super().__init__()
        self.classes = {"Teacher": Teacher, "Student": Student, "School": School, "Classroom": Classroom}

    # create for quiting
    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    #create for register
    #create for login
    #create for EOF
    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True
    
    #create for empty line
    def emptyline(self):
        """Empty line does nothing"""
        pass

    #create for help
    def do_help(self, arg):
        """Help command to display the help"""
        cmd.Cmd.do_help(self, arg)

    def _key_value_parser(self, args):
        """creates a dictionary from a list of strings"""
        new_dict = {}
        for arg in args:
            if "=" in arg:
                kvp = arg.split('=', 1)
                key = kvp[0]
                value = kvp[1]
                if value[0] == value[-1] == '"':
                    value = shlex.split(value)[0].replace('_', ' ')
                else:
                    try:
                        value = int(value)
                    except:
                        try:
                            value = float(value)
                        except:
                            continue
                new_dict[key] = value
        return new_dict


    #create for show
    def do_show(self, arg):
        """Prints an instance as a string based on the class and id"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in self.classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in storage.DBStorage().all():
                    print(storage.DBStorage().all()[key])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")


    #create for destroy
    def do_destroy(self, arg):
        """Deletes an instance based on the class and id"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in self.classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in DBStorage().all():
                    DBStorage().all().pop(key)
                    DBStorage().save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")


    #create for all
    def do_all(self, arg):
        """Prints string representations of instances"""
        args = shlex.split(arg)
        obj_list = []
        if len(args) == 0:
            obj_dict = storage.DBStorage().all()
        elif args[0] in self.classes:
            obj_dict = storage.DBStorage().all(self.classes[args[0]])
        else:
            print("** class doesn't exist **")
            return False
        for key in obj_dict:
            obj_list.append(str(obj_dict[key]))
        print("[", end="")
        print(", ".join(obj_list), end="")
        print("]")


    #create for update
    def do_update(self, arg):
        """Update an instance based on the class name, id, attribute & value"""
        args = shlex.split(arg)
        integers = ["number_rooms", "number_bathrooms", "max_guest",
                    "price_by_night"]
        floats = ["latitude", "longitude"]
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in self.classes:
            if len(args) > 1:
                k = args[0] + "." + args[1]
                if k in storage.DBStorage().all():
                    if len(args) > 2:
                        if len(args) > 3:
                            if args[0] == "Place":
                                if args[2] in integers:
                                    try:
                                        args[3] = int(args[3])
                                    except:
                                        args[3] = 0
                                elif args[2] in floats:
                                    try:
                                        args[3] = float(args[3])
                                    except:
                                        args[3] = 0.0
                            setattr(storage.DBStorage().all()[k], args[2], args[3])
                            storage.DBStorage().all()[k].save()
                        else:
                            print("** value missing **")
                    else:
                        print("** attribute name missing **")
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_admin(self, arg):
        """Enters the admin session"""
        admin_session()


if __name__ == '__main__':
    EduConnectCommand().cmdloop()

