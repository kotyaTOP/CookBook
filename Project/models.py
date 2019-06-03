<<<<<<<<< Temporary merge branch 1
# from app_config import mydb
from CookBook.Project.config import mydb
=========
from Project.config import mydb
>>>>>>>>> Temporary merge branch 2

class Dish(mydb.Model):
    __tablename__ = 'Dish'


class Ingredient(mydb.Model):
    __tablename__ = 'Ingredient'


class Unit(mydb.Model):
    __tablename__ = 'Unit'


class Dish_Ingredient(mydb.Model):
    __tablename__ = 'DishIngred'


class User(mydb.Model):
    __tablename__ = 'User'

