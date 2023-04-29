# Complate! 11:46 PM 9/21/2022
import sqlite3

con = sqlite3.connect('Phone.db')
cur = con.cursor()
cur.execute('Create table if not exists data(ID INT PRIMARY KEY,username text,phone INTEGER)')
con.commit()
con.close()

print('1-add number')
print('2-show number')
print('3-delete number')
print('4-Exit')

while True:
    get = input('Switch:')
    # add id,user name,phone number
    if get == '1':
        try:
            con = sqlite3.connect('Phone.db')
            cur = con.cursor()
            i_d = int(input('ID:'))
            username = input('Username:')
            phone = input('Phone number:')
            data = i_d,username,phone
            cur.execute('INSERT INTO data(id,username,phone) VALUES (?,?,?)',data)
            print('-' * 20)
            print('add seccssfuly!')
            print('-' * 20)
            print('1-add number')
            print('2-show number')
            print('3-delete number')
            con.commit()
            con.close()
        except sqlite3.IntegrityError:
            print('plase select another id this id available')
        except ValueError:
            print('Enter a number for id you can't enter a string')
    else:
        # show save
        if get == '2':
            print('-' * 30)
            print(f'id    username    phone')
            print('-' * 30)
            con = sqlite3.connect('Phone.db')
            cur = con.execute('SELECT id,username, phone FROM data')
            for i in cur:
                print(f'{i[0]}      ' + f'{i[1]}     ' + f'{i[2]}')
                print('-' * 30)
            con.commit()
            con.close()
        else:
            # Delete with ID
            if get == '3':
                print('Enter id user')
                try:
                    con = sqlite3.connect('Phone.db')
                    cur = con.cursor()
                    i_d = input('ID:')
                    cur.execute('DELETE FROM data where id = (?)',i_d)
                    con.commit()
                    con.close()
                except sqlite3.ProgrammingError:
                    print('number! :(')
            else:
                # Exit
                if get == '4':
                    print('Good Bye!')
                    break
                else:
                     print('Enter number between 1,2,3,4')
