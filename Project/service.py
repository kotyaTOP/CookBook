
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

    if do == "add":
        s = Dish_Ingredient()
    else:
        s = mydb.session.query(Dish_Ingredient).filter(Dish_Ingredient.id_dish_ingred == id).one_or_none()

    form = DishIngredForm(request.form, obj=s)

    if do == "delete":
        mydb.session.delete(s)
        mydb.session.flush()
        return redirect(url_for('dish_ingred'))

    if form.button_save.data:
        form.populate_obj(s)
        mydb.session.add(s)
        if s.id_dish_ingred != id:
            return redirect(url_for('dish_ingred', id=s.id_dish_ingred))

    return render_template('change_dish_ingred.html', form=form)

if __name__ == '__main__':
    metadata = mydb.metadata
    metadata.create_all(mydb.engine)
    app.run()