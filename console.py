#!/usr/bin/python3
"""this the main console for the school project"""
import cmd
import models
from models.engine.storage import DBStorage
import models.engine
import models.engine.storage
from models.teacher import Teacher
from models.student import Student
from models.classroom import Classroom
from models.base_model import BaseModel
from models.school import School
from models.admin_model import Admin
import shlex
from models.admin_session import admin_session
from models.teacher_session import teacher_session
from models.student_session import student_session
from models.parent_session import parent_session
from models.login import login
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
    def do_login(self, arg):
        """Login command to login to the program"""
        login()
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
                if key in models.engine.storage.DBStorage().all():
                    print(models.engine.storage.DBStorage().all()[key])
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
                if key in models.engine.DBStorage().all():
                    models.engine.DBStorage().all().pop(key)
                    models.engine.DBStorage().save()
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
            obj_dict = models.engine.storage.DBStorage().all()
        elif args[0] in self.classes:
            obj_dict = models.engine.storage.DBStorage().all(self.classes[args[0]])
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
                if k in models.engine.storage.DBStorage().all():
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
                            setattr(models.engine.storage.DBStorage().all()[k], args[2], args[3])
                            models.engine.storage.DBStorage().all()[k].save()
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

    def do_teacher(self, arg):
        """Enters the teacher session"""
        teacher_session()

    def do_student(self, arg):
        """Enters the student session"""
        student_session()

    def do_parent(self, arg):
        """Enters the parent session"""
        parent_session()

if __name__ == '__main__':
    EduConnectCommand().cmdloop()

