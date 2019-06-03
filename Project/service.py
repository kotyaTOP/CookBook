
from Project.config import app, mydb
from flask import render_template, request, redirect, url_for
from Project.models import Dish, Ingredient, Unit, Dish_Ingredient
from Project.forms import DishForm, IngredForm, UnitForm, DishIngredForm, FormSearch

@app.route('/')
def menu():
    return render_template('./menu.html')



if __name__ == '__main__':
    metadata = mydb.metadata
    metadata.create_all(mydb.engine)
    app.run()