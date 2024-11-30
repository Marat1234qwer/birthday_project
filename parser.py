import datetime
import time


def get_date():
    with open('date.txt', 'r') as f:  # использовать для тестов
        date_now = f.read()
    # today_dt = datetime.date.today()                # реальное использование
    # today = str(today_dt)[5:]                       # дата формата - dd.mm
    # today_part = today.partition('-')
    # date_now = today_part[-1] + '.' + today_part[0]
    return date_now


def read_data_birthday():
    with open('result.txt', 'r') as f:
        data_birthday = f.readlines()
    birthday_dates = []  # список дней рождений
    for i in range(len(data_birthday)):
        birthday_dates.append(data_birthday[i][:5])
    return data_birthday, birthday_dates


def create_string(data_birthday, birthdays, date_now):  # формируем строку сотрудников у которых др.
    target_lst = []
    for i in range(len(birthdays)):
        target = ''
        if date_now == birthdays[i]:
            target = data_birthday[i][11:]
            lst_target = list(target)
            for j in range(len(lst_target)):
                if lst_target[j] == ' ':
                    for _ in range(j-1):
                        lst_target.pop(1)
                    lst_target[1] = '.'
                    break
            target = ''.join(lst_target)
            target_lst.append(target)
    for i in range(len(target_lst)):
        target_lst[i] = target_lst[i][:-1] + '<br>'
    target_string = ''.join(target_lst)
    return target_string[:-4]


def write_index_html(target_string):
    with open('maket.html', 'r') as f:
        maket = f.readlines()
    for i in range(len(maket)):
        if maket[i] == 'date_target\n':
            maket[i] = str(get_date()) + '<br>'
        elif maket[i] == 'target\n':
            maket[i] = target_string
            with open('index.html', 'w') as f:
                f.writelines(maket)
            break


def main(date_now):
    data_birthday, birthdays = read_data_birthday()
    target_string = create_string(data_birthday, birthdays, date_now)
    write_index_html(target_string)


if __name__ == '__main__':
    while True:
        try:
            date_now = get_date()
            main(date_now)
            time.sleep(5)  # изиенить на 3600 - запуск скрипта каждый час
        except Exception as ex:  # записываем возможные ошибки
            with open('errors.log', 'a') as f:
                f.write(str(time.asctime()) + ' ERROR - ' + str(ex) + '\n')
            time.sleep(5)  # изменить на 3600
