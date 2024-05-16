from workhome import workhome03
from workhome import workhome02

# Функция меню
def menu():
    dct = {"1": "Запустить модуль с проверкой даты",
           "2": "Запустить шахматный модуль",
           "3": "Выйти из программы"}
    for k, v in dct.items():
        if k.isdigit():
            print(f'{k}: {v}')
        else:
            print(v)

# Функция выбора меню
def select_an_operation(is_flag: bool):
    choice = input("Введите команду: ")
    if choice == "3":
        is_flag = False
        return is_flag
    elif choice == "1":
        workhome02.run()
    elif choice == "2":
        workhome03.run()
    else:
        print("Неверная команда")
    return is_flag

def run():
    is_flag = True
    while is_flag:
        menu()
        is_flag = select_an_operation(is_flag)
         
def main():
    run()

if __name__ == "__main__":
    main()