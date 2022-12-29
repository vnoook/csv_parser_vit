import csv
import openpyxl

# рабочие переменные
file_csv = 'out_data.csv'
staff_dict = {}

# чтение построчно файла csv и заполнение словаря со счётом уникальных значений
with open(file_csv, encoding='cp1251', newline='') as csvfile:
    row_csv_content = csv.reader(csvfile, delimiter=';')

    for row in row_csv_content:
        if row_csv_content.line_num == 1:
            staff_dict[row[9]] = 'Количество'
        else:
            if staff_dict.get(row[9], False):
                staff_dict[row[9]] = staff_dict[row[9]] + 1
            else:
                staff_dict[row[9]] = 1

file_xls = 'out_data.xlsx'

# создание книги xls и активация рабочего листа
wb = openpyxl.Workbook()
wb_s = wb.active

# проход по словарю
for key, val in staff_dict.items():
    # добавление пары ключ-значение на лист
    wb_s.append([key, val])

# сохранение файла xls и закрытие его
wb.save(file_xls)
wb.close()

input('Нажмите ENTER')
