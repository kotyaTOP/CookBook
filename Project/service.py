from Project.config import app, mydb
from flask import render_template, request, redirect, url_for
from Project.models import Dish



@app.route('/')
def menu():
    return render_template('./menu.html')





@app.route('/change_dish/<id>/<do>', methods=['GET', 'POST'])
def change_dish(id, do):
    id = int(id)

    if do == "add":
        s = Dish()
    else:
        s = mydb.session.query(Dish).filter(Dish.id_dish == id).one_or_none()

    form = DishForm(request.form, obj=s)

    if do == "delete":
        mydb.session.delete(s)
        mydb.session.flush()
        return redirect(url_for('dish'))

    if form.button_save.data:
        form.populate_obj(s)
        mydb.session.add(s)
        if s.id_dish != id:
            return redirect(url_for('dish', id=s.id_dish))

    return render_template('change_dish.html', form=form)


if __name__ == '__main__':
    metadata = mydb.metadata
    metadata.create_all(mydb.engine)
    app.run()