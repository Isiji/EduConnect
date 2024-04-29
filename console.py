#!/usr/bin/python3
"""this the main console for the school project"""
import cmd
from models import storage
from models.teacher import Teacher
from models.student import Student
from models.classroom import Classroom
from models.base_model import BaseModel
from models.school import School
from models.admin import Admin

import shlex

class EduConnectCommand(cmd.Cmd):
    """Main console class"""
    prompt = '(EduConnect).. '
    classes = {"Teacher": Teacher, "Student": Student, "School": School, "Classroom": Classroom} 
    # create for quiting
    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True
    
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

    #create for create
    def do_create(self, arg):
        """Creates a new instance of a class"""
        if not arg:
            print("** class name missing **")
        elif arg not in self.classes:
            print("** class doesn't exist **")
        else:
            new = eval(arg)()
            new.save()
            print(new.id)

    #create for show
    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[key])

    #create for destroy
    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()

    #create for all
    def do_all(self, arg):
        """Prints all instances of a class"""
        args = arg.split()
        if not arg:
            print([str(obj) for obj in storage.all().values()])
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            print([str(obj) for obj in storage.all(eval(args[0])).values()])

    #create for update
    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key not in storage.all():
                print("** no instance found **")
            else:
                obj = storage.all()[key]
                setattr(obj, args[2], args[3])
                obj.save()

if __name__ == '__main__':
    EduConnectCommand().cmdloop()

