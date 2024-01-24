import pandas as pd
from openpyxl import Workbook
import csv

def CreateXLSXFromCSV(name = 'input.csv'):
    wb = Workbook()
    ws = wb.active
    
    with open('testdoc.csv') as f:
        reader = csv.reader(f, delimiter=',')

        for row_index, row in enumerate(reader, start=1):
            for column_index, cell_value in enumerate(row, start=1):
                ws.cell(row=row_index, column=column_index).value=cell_value
    wb.save('group_make.xlsx')

def main():
    inputFileName = input("file name: ")
    CreateXLSXFromCSV(inputFileName)

    myFile = pd.read_excel(r"group_make.xlsx", engine="openpyxl")

    print(myFile['First Name'][0])

    myFile.sort_values(by=myFile.columns[7], inplace=True, ascending=False)
    myFile.reset_index(drop=True, inplace=True)

    scores = myFile.iloc[:, 7]
    fullName = myFile.iloc[:, 0] + ', ' + myFile.iloc[:, 1]

    print(fullName)
    print(scores)

if __name__ == "__main__":
    main()