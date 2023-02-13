import openpyxl

workbook = openpyxl.load_workbook("..//ExcelFiles//writingTestData.xlsx")
sheet = workbook["Writing"]

for rows in range(1,10):
    for columns in range(1,3):
        sheet.cell(row=rows, column=columns).value="Hello"

workbook.save("..//ExcelFiles//writingTestData.xlsx")