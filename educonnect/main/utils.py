import os
import secrets
from PIL import Image
from educonnect import db_storage, login_manager


#function for updating the frofile picture and account
def save_picture(form_picture):
    """save picture"""
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn


#create a user loader function that checks through the database for the user id
@login_manager.user_loader
def load_user(user_id):
    """checks through the database for the user"""
    from educonnect.models.teacher import Teacher
    from educonnect.models.admin_model import Admin
    from educonnect.models.student import Student
    from educonnect.models.parent import Parent
    from educonnect.models.school import School
    from educonnect import db_storage

    user = db_storage.get(Teacher, user_id)
    if user is None:
        user = db_storage.get(Admin, user_id)
    if user is None:
        user = db_storage.get(Student, user_id)
    if user is None:
        user = db_storage.get(Parent, user_id)
    if user is None:
        user = db_storage.get(School, user_id)
    return user
    
