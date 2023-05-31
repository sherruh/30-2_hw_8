import sqlite3

def create_con(db_name):
    con = None
    try:
        con = sqlite3.connect(db_name)
    except sqlite3.Error as e:
        print(e)
    return con

def create_table(con, sql):
    try:
        cursor = con.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)

def execute_sql(con, sql):
    try:
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
    except sqlite3.Error as e:
        print(e)

db_name = 'hw.db'

create_countries_table_sql = '''
CREATE TABLE employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(200) NOT NULL,
    last_name VARCHAR(200) NOT NULL,
    city_id INTEGER NOT NULL,
    FOREIGN KEY (city_id) REFERENCES cities(id)
)
'''

#create_table(con,create_countries_table_sql)

def show_cities():
    con = create_con(db_name)
    sql_select_all_cities = '''SELECT title FROM cities'''
    try:
        cursor = con.cursor()
        cursor.execute(sql_select_all_cities)
        rows = cursor.fetchall()
        for row in rows:
            print(str(row)[2:-3])
    except sqlite3.Error as e:
            print(e)
    con.close()


def show_empoyees_by_id(id):
    con = create_con(db_name)
    sql_select_employees = '''SELECT e.first_name,e.last_name, c.title, cs.title 
    FROM employees e
    LEFT JOIN cities c
    ON c.id = e.city_id
    LEFT JOIN countries cs
    ON cs.id = c.country_id
    WHERE c.id = ?
    '''

    try:
        cursor = con.cursor()
        cursor.execute(sql_select_employees, id)
        rows = cursor.fetchall()
        for row in rows:
            print(row[0] + ' ' + row[1] + ' ' + row[2] + ' ' + row[3])
    except sqlite3.Error as e:
        print(e)
    con.close()



while (True):
    print('Вы можете отобразить список сотрудников по выбранному id города из перечня городов ниже, для выхода из программы введите 0:')
    show_cities()
    id = input()
    if int(id) == 0:
        break
    show_empoyees_by_id(id)


