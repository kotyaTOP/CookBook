from app_config import mydb

class Dish(mydb.Model):
    __tablename__ = 'Dish'


class Ingredient(mydb.Model):
    __tablename__ = 'Ingredient'


class Unit(mydb.Model):
    __tablename__ = 'Unit'


class Dish_Ingredient(mydb.Model):
    __tablename__ = 'DishIngred'


