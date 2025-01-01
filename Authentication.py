import sqlite3


def login():
    email = input('Enter Your Email: ')
    lower_email = email.lower()

    with sqlite3.connect('sqlight3.db') as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM users WHERE email == ?', (lower_email,))
        result = cursor.fetchall()

    if result:
        password = input('Enter Your Password: ')
        if result[0][4] == password:
            with sqlite3.connect('sqlight3.db') as connection:
                cursor = connection.cursor()
                cursor.execute('UPDATE users SET is_logged_in = ? WHERE email == ?', (True, lower_email))
                connection.commit()
                print('You Are Logged In!!!')
        else:
            print('Your Password is Not Correct!')
            login()
    else:
        print('Email Does Not Exists!')
        login()


def register():
    email = input('Enter Your Email: ')
    lower_email = email.lower()

    with sqlite3.connect('sqlight3.db') as connection:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM users WHERE email == ?', (lower_email,))
        result = cursor.fetchall()

    if result:
        print('Email Already Exists!')
        register()
    else:
        password = input('Enter Your Password: ')
        first_name = input('Enter Your First Name: ')
        last_name = input('Enter Your Last Name: ')

        with sqlite3.connect('sqlight3.db') as connection:
            cursor = connection.cursor()
            cursor.execute(
                'INSERT INTO users (email, password, first_name, last_name, is_logged_in) values (?, ?, ?, ?, ?)',
                (lower_email, password, first_name, last_name, True)
            )
            connection.commit()
