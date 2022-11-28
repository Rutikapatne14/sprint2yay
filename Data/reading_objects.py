#to read locators xpath from excelsheet

import xlrd
path = r"C:\Users\ASUS\Desktop\demo_1.xlsx"

def read_locators_from_excel():
    workbook = xlrd.open_workbook(path)
    worksheet = workbook.sheet_by_name('ssheet')
    rows = worksheet.nrows   # reads the data and returns a generator object
    # print(rows)
    d = {}
    for i in range(1, rows):
        row = worksheet.row_values(i)
        print(row)
        d[row[0]] = (row[1], row[2])
    return d


