import csv
from pprint import pprint as pp

file_csv_from_mis = 'out_data1.csv'
staff_dict = {}

with open(file_csv_from_mis, encoding='cp1251', newline='') as csvfile:
    row_csv_content = csv.reader(csvfile, delimiter=';')

    for row in row_csv_content:
        if row_csv_content.line_num == 1:
            staff_dict[row[9]] = ''
        else:
            if staff_dict.get(row[9], False):
                print(staff_dict.get(row[9], False))
                staff_dict[row[9]] = staff_dict[row[9]] + 1
            else:
                staff_dict[row[9]] = 1

pp(staff_dict)
