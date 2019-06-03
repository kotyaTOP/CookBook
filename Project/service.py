
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

@app.route('/unit')
def unit():
    units = mydb.session.query(Unit).all()
    return render_template('unit.html', units=units)


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

@app.route('/main_page')
def main_page():
    form = FormSearch(request.args)
    dishes = mydb.session.query(Dish_Ingredient).all()

    if form.button_search1.data:
        q = mydb.session.query(Dish)
        if form.dish_name.data != '':
            q = q.filter(Dish.dish_name == form.dish_name.data)
        dish = q.all()
        dish_id = [elem.id_dish for elem in dish]
        dishes = get_dish_ingred(dish_id)


    ingreds = [] #список выбранных для поиска ингредиентов
    missing_ingreds_dict = {}
    if form.button_search3.data:
        for f_ingred in form.ingreds:
            ingred = f_ingred.data
            if ingred not in ingreds:
                ingreds.append(ingred)
        if len(ingreds):
            missing_ingreds_dict = get_missing_ingreds_for_all(ingreds)
            dishes = get_dish_ingred(get_important_dishes(missing_ingreds_dict))
            sort_dishes_by_missing_ingreds(dishes, missing_ingreds_dict)

    dishes_id = []
    new_dishes = []
    ingreds = {}
    for dish in dishes:
        if not dishes_id.__contains__(dish.id_dish):
            new_dishes.append(dish)
            dishes_id.append(dish.id_dish)
        if not ingreds.keys().__contains__(dish.id_dish):
            ingreds[dish.id_dish] = []

        ingreds[dish.id_dish].append(str(dish.ingred.ingred_name) + ' - ' + str(dish.sum) + str(dish.unit.unit_name))



    if form.button_search2_add.data:
        form.ingreds.append_entry()
        return render_template('main.html', dish=new_dishes, ingreds=ingreds, form=form, miss_ingreds=missing_ingreds_dict)

    if form.button_search2_remove.data:
        form.ingreds.pop_entry()
        return render_template('main.html', dish=new_dishes, ingreds=ingreds, form=form, miss_ingreds=missing_ingreds_dict)


    return render_template('main.html', dish=new_dishes, ingreds=ingreds, form=form, miss_ingreds=missing_ingreds_dict)


def get_important_dishes(miss_dict):
    dishes = mydb.session.query(Dish)
    new_dishes = []
    for dish in dishes:
        ingreds = get_ingreds_for_dish(dish.id_dish)
        if (len(miss_dict[dish.id_dish]) < len(ingreds)):
            new_dishes.append(dish.id_dish)
    return new_dishes


def sort_dishes_by_missing_ingreds(all_dish, missing_dict: dict): #возвращает список блюд_ингредиентов по возрастанию недостающих блюд
    for i in range(len(all_dish) - 1):
        for j in range(len(all_dish) - i - 1):
            if len(missing_dict[all_dish[j].id_dish]) > len(missing_dict[all_dish[j + 1].id_dish]):
                all_dish[j], all_dish[j + 1] = all_dish[j + 1], all_dish[j]



def get_missing_ingreds(dish_id: int, ingreds: list): #получает список ингредиентов (id), которых не достает до нужного списка
    dish_ingreds = get_ingreds_for_dish(dish_id)
    missing_ingreds = [elem.ingred_name for elem in dish_ingreds if elem not in ingreds ]
    return missing_ingreds

def get_missing_ingreds_for_all(ingreds: list): #получает словарь, где ключ - блюдо (id), значение - список недостающх ингредиентов (id)
    dishes = mydb.session.query(Dish)
    missing_ingreds_dict = {}
    for dish in dishes:
        missing_ingreds_dict[dish.id_dish] = get_missing_ingreds(dish.id_dish, ingreds)
    return missing_ingreds_dict

def get_ingreds_for_dish(dish_id: int):
    all_dishes = mydb.session.query(Dish_Ingredient)
    dishes = mydb.session.query(Dish)
    ingreds_dict = get_ingreds_for_dishes(dishes, all_dishes)
    return ingreds_dict[dish_id]

def get_ingreds_for_dishes(dishes: list, dishes_ingreds: list): #формирует словарь,где ключ - блюдо(id), значение - список его ингредиентов (id)
    ingreds_dict = {}
    for dish in dishes:
        if not ingreds_dict.keys().__contains__(dish):
            ingreds_dict[dish.id_dish] = []
    for dish in dishes_ingreds:
        ingreds_dict[dish.dish.id_dish].append(dish.ingred)
    return ingreds_dict

def get_dish_ingred(dishes_id: list):   #получает по списку блюд список всех блюд_ингредиентов
    new_dish_ingreds = []
    dish_ingreds = mydb.session.query(Dish_Ingredient).all()

    for elem in dish_ingreds:
        if elem.id_dish in dishes_id:
            new_dish_ingreds.append(elem)
    return new_dish_ingreds

def contains(minlist: list, list: list):
    for elem in minlist:
        if not elem in list:
            return False
    return True


if __name__ == '__main__':
    metadata = mydb.metadata
    metadata.create_all(mydb.engine)
    app.run()