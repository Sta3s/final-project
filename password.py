from rich import print
import random
import sqlite3

conn = sqlite3.connect('history_sql.db') 
cursor = conn.cursor() 
table ="""CREATE TABLE IF NOT EXISTS history (LEVEL CHAR,COUNT CHAR,PASSW TEXT);"""
cursor.execute(table) 


print("[italic red]-----PASSWORD GENERATOR-----[/italic red]")
numbers = [1,2,3,4,5,6,7,8,9,0]
chars = ["a","b","c","d","e","f","g","h","j"]
special_chars = ["*","-",".","?","!"]


def generate_password(chars):
    password = ""
    print("Numbers count in your password(4-25)")
    count_numbers = int(input())
#Проверка, чтобы пароль был в диапозоне от 4 до 25 символов
    if count_numbers >= 4 and count_numbers <= 25:
#Генерируем пароль по одному символу count_numbers кол-во раз и берем символы из chars
        for i in range(count_numbers):
            password = password + str((random.choice(chars)))
        print("Your password: [italic red]"+password+"[/italic red]")

        cursor.execute("insert into history (LEVEL, COUNT, PASSW) values (?, ?, ?)",(level, count_numbers, password))
        password = ""


#Запускаем цикл, который ждет команды, чтобы генерировал пароли до момента пока команда не будет "6"
while True:
    print("1.Create password 1 level (only numbers)")
    print("2.Create password 2 level (numbers and chars)")
    print("3.Create password 3 level (numbers, chars and special chars)")
    print("4.Show password history in sql format")
    print("5.Exit")
    level = int(input())
#В зависимости от команды запускаем функцию с разными символами    
    if level == 1:
        generate_password(numbers)

    if level == 2:
        numbers_chars = numbers+chars
        generate_password(numbers_chars) 

    if level == 3:
        numbers_special = numbers+chars+special_chars
        generate_password(numbers_special) 

    if level == 4:
        print("Your password History: ") 
        data=cursor.execute('''SELECT * FROM history''') 
#Показывам историю паролей через sql базы данных, цикл используем для того, чтобы вывести все пароли
        for password in data.fetchall(): 
            print("Level:", password[0])
            print("Chars count:", password[1])
            print("Password:", password[2])
            print("=========")
        conn.commit() 
        conn.close()
    elif level == 5:
        break

    else:
        print("Please enter valid level(1-3)")

