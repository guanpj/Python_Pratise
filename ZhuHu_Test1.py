import requests, csv, openpyxl

# wb = openpyxl.load_workbook("ZhiHu_Data.xlsx")
# sheet = wb['zhihu']
# print(sheet['A1'].value)

csv_file = open("ZhiHu_Data.csv", "r", newline='', encoding='utf-8')
reader = csv.reader(csv_file)
for row in reader:
    print(row)