<<<<<<<<< Temporary merge branch 1
# from config import app, mydb
from CookBook.Project.config import app, mydb
=========
from Project.config import app, mydb
from flask import render_template, request, redirect, url_for
from Project.models import Dish, Ingredient, Unit, Dish_Ingredient
from Project.forms import DishForm, IngredForm, UnitForm, DishIngredForm, FormSearch

@app.route('/')
def menu():
    return render_template('./menu.html')


@app.route('/change_dish_ingred/<id>/<do>', methods=['GET', 'POST'])
def change_dish_ingred(id, do):
    id = int(id)
    i = 1
    if do == "add":
        s = Dish_Ingredient()
    else:
        s = mydb.session.query(Dish_Ingredient).filter(Dish_Ingredient.id_dish_ingred == id).one_or_none()
@app.route('/show')
def show():
    @app.route('/dish')
    def dish():
        i = 1
        return 0

    @app.route('/ingredient')
    def ingredient():
        return 0

    @app.route('/dish_ingred')
    def dish_ingred():
        return 0

    @app.route('/unit')
    def unit():
        return 0

    return 0

    form = DishIngredForm(request.form, obj=s)

    if do == "delete":
        mydb.session.delete(s)
        mydb.session.flush()
        return redirect(url_for('dish_ingred'))
@app.route('/change_dish')
def change_table():
   return 0

    if form.button_save.data:
        form.populate_obj(s)
        mydb.session.add(s)
        if s.id_dish_ingred != id:
            return redirect(url_for('dish_ingred', id=s.id_dish_ingred))

@app.route('/search_dish')
def search_dish():
    return 0

@app.route('/add_user')
def add_user():
    return 0
    return render_template('change_dish_ingred.html', form=form)


if __name__ == '__main__':
    metadata = mydb.metadata
    metadata.create_all(mydb.engine)
    app.run()