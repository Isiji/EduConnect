#!/usr/bin/python3
"""this the main console for the school project"""
import cmd
import models
from models.engine.storage import DBStorage
import models.engine
from models.teacher import Teacher
from models.student import Student
from models.classroom import Classroom
from models.base_model import BaseModel
from models.school import School
from models.admin_model import Admin
import shlex

#classes = {"Teacher": Teacher, "Student": Student, "School": School, "Classroom": Classroom} 


class EduConnectCommand(cmd.Cmd):
    """Main console class"""
    prompt = '(EduConnect).. '

    def __init__(self):
        """Initialize the console"""
        super().__init__()
        self.classes = {"Teacher": Teacher, "Student": Student, "School": School, "Classroom": Classroom}

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


    #create for create
    def do_create(self, arg):
        """Creates a new instance of a class"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in self.classes:
            new_dict = self._key_value_parser(args[1:])
            instance = self.classes[args[0]](**new_dict)
        else:
            print("** class doesn't exist **")
            return False
        print(instance.id)
        instance.save()

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
            obj_dict = models.engine.DBStorage().all()
        elif args[0] in self.classes:
            obj_dict = models.engine.DBStorage().all(self.classes[args[0]])
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
                if k in models.engine.DBStorage().all():
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
                            setattr(models.engine.DBStorage().all()[k], args[2], args[3])
                            models.engine.DBStorage().all()[k].save()
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
#create a function that enters into admin session and allows admin to do his functions
def admin_session():
    """this function is for the admin functionality"""
    print("Welcome the EduConnect  Admin Panel")
    print(" ")

    while True:
        print("1. Register a new admin")
        print("2. Register student")
        print("3. Register teacher")
        print("4. Register school")
        print("5. Register classroom")
        print("6. View all students")
        print("7. View all teachers")
        print("8. View all schools")
        print("9. View all classrooms")
        print("10. Delete student")
        print("11. Delete teacher")
        print("12. Delete school")
        print("13. Delete classroom")
        print("14. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid choice. Enter a number")
            continue

        if choice == 1:
            admin = Admin()
            admin.register_admin()

        elif choice == 2:
            student = Student()
            student.register_student()

        elif choice == 3:
            teacher = Teacher()
            teacher.register_teacher()

        elif choice == 4:
            school = School()
            school.register_school()

        elif choice == 5:
            classroom = Classroom()
            classroom.register_classroom()

        elif choice == 6:
            Student.view_all_students()

        elif choice == 7:
            Teacher.view_all_teachers()

        elif choice == 8:
            School.view_all_schools()

        elif choice == 9:
            Classroom.view_all_classrooms()

        elif choice == 10:
            student = Student()
            student.delete_student()

        elif choice == 11:
            teacher = Teacher()
            teacher.delete_teacher()

        elif choice == 12:
            school = School()
            school.delete_school()

        elif choice == 13:
            classroom = Classroom()
            classroom.delete_classroom()

        elif choice == 14:
            print("Thank you for using the EduConnect Admin Panel")
            break

if __name__ == '__main__':
    EduConnectCommand().cmdloop()

