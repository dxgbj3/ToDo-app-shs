from json_store_v2 import *

while True:
    question_to_user = """[0] Выйти с программы
    \t[1] Добавить новую задачу 
    \t[2] Удалить задачу (отметить выполненой)
    \t[3] Вывести все задачи
    
    Что хотите сделать?: """
    user_input = 0
    while True:
        try:
            user_input = int(input(question_to_user))
            if 0 <= user_input <= 3:
                break
            else:
                print('Нет такой команды')
        except ValueError:
            print("Введите число: ")

    if user_input == 0:
        input("Нажмите Enter для выхода")
        break
    elif user_input == 1:
        user_todo_title = input("Введите вашу задачу: ")
        user_todo_data = input("Введите дедлайн: " )
        add_my_todo(user_todo_title, user_todo_data)
    elif user_input == 2:
        user_todo_title = input("Введите задание вашей задачи: ")
        del_my_todo(user_todo_title)
    else:
        user_data = get_my_todo_list()
        str_todo = 'Ваши не выполненные задачи\n\n'
        for todo in user_data:
            str_todo += f"""{'='*30}
Задача: {todo['todo']}
Выполнить до: {todo['date_todo']}
{'='*30}
\n"""
            print(str_todo)

save_in_file()