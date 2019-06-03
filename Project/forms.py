from CookBook.Project.config import mydb
from CookBook.Project.models import Dish, Dish_Ingredient, Unit, Ingredient
from wtforms import validators, Form, SubmitField, IntegerField, StringField, FieldList
from wtforms_alchemy import ModelForm
from wtforms_alchemy.fields import QuerySelectField
from wtforms_components.fields import TimeField

class DishForm(ModelForm):
    class Meta:
        model = Dish

    dish_name = StringField('Название блюда', [validators.DataRequired()])
    recipe = StringField('Рецепт', [validators.DataRequired()])
    time = TimeField('Время', [validators.DataRequired()])
    button_save = SubmitField('Сохранить')

class IngredForm(ModelForm):
    class Meta:
        model = Ingredient

    ingred_name = StringField('Название ингредиента', [validators.DataRequired()])
    button_save = SubmitField('Сохранить')

class UnitForm(ModelForm):
    class Meta:
        model = Unit

    unit_name = StringField('Единица измерения', [validators.DataRequired()])
    button_save = SubmitField('Сохранить')

class DishIngredForm(ModelForm):
    class Meta:
        model = Dish_Ingredient

    dish = QuerySelectField('Блюдо',
                            query_factory=lambda: mydb.session.query(Dish).all(),
                            get_pk=lambda g: g.id_dish,
                            get_label=lambda g: "%s" % (g.dish_name))
    ingred = QuerySelectField('Ингредиент',
                              query_factory=lambda: mydb.session.query(Ingredient).all(),
                              get_pk=lambda g: g.id_ingred,
                              get_label=lambda g: "%s" % (g.ingred_name))
    unit = QuerySelectField('Единица измерения',
                            query_factory=lambda: mydb.session.query(Unit).all(),
                            get_pk=lambda g: g.id_unit,
                            get_label=lambda g: "%s" % (g.unit_name))
    sum = IntegerField('Количество', [validators.DataRequired()])
    button_save = SubmitField('Сохранить')

class FormSearch(Form):
    dish_name = StringField('Название блюда')
    ingred_name = StringField("Имя ингредиента")
    ingred_names = StringField('Список ингредиентов (через пробел)')
    button_search3 = SubmitField('Поиск по ингредиентам')
    button_search1 = SubmitField('Поиск по названию')

    button_search2_add = SubmitField('+')
    button_search2_remove = SubmitField('-')

    ingreds = FieldList(QuerySelectField('Ингредиент',
                                         query_factory=lambda: mydb.session.query(Ingredient).all(),
                                         get_pk=lambda g: g.id_ingred,
                                         get_label=lambda g: "%s" % (g.ingred_name)))
