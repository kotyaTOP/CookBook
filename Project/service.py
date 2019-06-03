
from CookBook.Project.config import app, mydb
from flask import render_template, request, redirect, url_for
from CookBook.Project.models import Dish, Ingredient, Unit, Dish_Ingredient
from CookBook.Project.forms import DishForm, IngredForm, UnitForm, DishIngredForm, FormSearch

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


@app.route('/change_ingred/<id>/<do>', methods=['GET', 'POST'])
def change_ingred(id, do):
    id = int(id)

    if do == "add":
        s = Ingredient()
    else:
        s = mydb.session.query(Ingredient).filter(Ingredient.id_ingred == id).one_or_none()

    form = IngredForm(request.form, obj=s)

    if do == "delete":
        mydb.session.delete(s)
        mydb.session.flush()
        return redirect(url_for('ingredient'))

    if form.button_save.data:
        form.populate_obj(s)
        mydb.session.add(s)
        if s.id_ingred != id:
            return redirect(url_for('ingredient', id=s.id_ingred))

    return render_template('change_ingred.html', form=form)


@app.route('/change_unit/<id>/<do>', methods=['GET', 'POST'])
def change_unit(id, do):
    id = int(id)

    if do == "add":
        s = Unit()
    else:
        s = mydb.session.query(Unit).filter(Unit.id_unit == id).one_or_none()

    form = UnitForm(request.form, obj=s)

    if do == "delete":
        mydb.session.delete(s)
        mydb.session.flush()
        return redirect(url_for('unit'))

    if form.button_save.data:
        form.populate_obj(s)
        mydb.session.add(s)
        if s.id_unit != id:
            return redirect(url_for('unit', id=s.id_unit))

    return render_template('change_unit.html', form=form)

@app.route('/dish')
def dish():
    dishes = mydb.session.query(Dish).all()
    form = FormSearch(request.args)
    if form.button_search1.data:
        q = mydb.session.query(Dish)
        if form.dish_name.data != '':
            q = q.filter(Dish.dish_name == form.dish_name.data)
        dishes = q.all()

    return render_template('dish.html', dishes=dishes, form=form)

@app.route('/dish_ingred')
def dish_ingred():
    dish_ingred = mydb.session.query(Dish_Ingredient).all()
    form = FormSearch(request.args)
    if form.button_search1.data:
        dish_name = form.dish_name.data
        ingred_name = form.ingred_name.data
        if len(dish_name)>0 and len(ingred_name) > 0:
            dish = mydb.session.query(Dish).filter(Dish.dish_name == dish_name).all()[0]
            print(dish)
            ingred = mydb.session.query(Ingredient).filter(Ingredient.ingred_name == ingred_name).all()[0]
            dish_ingred = find_dish_ingred(dish=dish, ingred=ingred)
        else:
            if len(dish_name)>0 :
                dish = mydb.session.query(Dish).filter(Dish.dish_name == dish_name).all()[0]
                dish_ingred = find_dish_ingred(dish=dish)
            if len(ingred_name) :
                ingred = mydb.session.query(Ingredient).filter(Ingredient.ingred_name == ingred_name).all()[0]
                dish_ingred = find_dish_ingred(ingred=ingred)
    return render_template('dish_ingred.html', dish_ingred=dish_ingred, form=form)

def find_dish_ingred(dish=None, ingred=None):
    q = mydb.session.query(Dish_Ingredient).all()
    answer = []
    for elem in q:
        if dish is not None and ingred is not None:
            if elem.id_dish == dish.id_dish and elem.id_ingred == ingred.id_ingred:
                answer.append(elem)
        else:
            if dish is not None and elem.id_dish == dish.id_dish:
                answer.append(elem)
            if ingred is not None and elem.id_ingred == ingred.id_ingred:
                answer.append(elem)
    return answer

@app.route('/ingredient')
def ingredient():
    ingreds = mydb.session.query(Ingredient).all()
    form = FormSearch(request.args)
    if form.button_search1.data:
        q = mydb.session.query(Ingredient)
        if form.ingred_name.data != '':
            q = q.filter(Ingredient.ingred_name == form.ingred_name.data)
        ingreds = q.all()
    return render_template('ingredient.html', ingred=ingreds, form=form)


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