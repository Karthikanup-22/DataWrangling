import xlrd

# Open the workbook
workbook = xlrd.open_workbook("sample2.xls")
sheet = workbook.sheet_by_index(0)

# Display all rows
for row_idx in range(sheet.nrows):
    print(sheet.row(row_idx))
