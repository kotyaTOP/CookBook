from config import app, mydb

@app.route('/')
def menu():
    return 0


@app.route('/show')
def show():
    @app.route('/dish')
    def dish():
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


@app.route('/change_dish')
def change_table():
   return 0


@app.route('/search_dish')
def search_dish():
    return 0

@app.route('/add_user')
def add_user():
    return 0


if __name__ == '__main__':
    metadata = mydb.metadata
    metadata.create_all(mydb.engine)
    app.run()
