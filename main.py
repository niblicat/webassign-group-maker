import pandas as pd
from openpyxl import Workbook
import csv
from typing import List
import random

def CreateXLSXFromCSV(name = 'input.csv'):
    wb = Workbook()
    ws = wb.active
    
    with open('testdoc.csv') as f:
        reader = csv.reader(f, delimiter=',')

        for row_index, row in enumerate(reader, start=1):
            for column_index, cell_value in enumerate(row, start=1):
                ws.cell(row=row_index, column=column_index).value=cell_value
    wb.save('group_make.xlsx')

def SortXLSX(name = "group_make.xlsx"):
    myFile = pd.read_excel(f"{name}", engine="openpyxl")

    myFile.sort_values(by=myFile.columns[7], inplace=True, ascending=True)
    myFile.reset_index(drop=True, inplace=True)
    return myFile

def MakeGroups(students: pd.DataFrame, min: int) -> List[pd.DataFrame]:
    total = students.__len__()
    numGroups = total // min

    groups = [pd.DataFrame(columns=['name', 'score']) for _ in range(numGroups)]
    
    for i in range(total):
        group_index = i % numGroups
        row = pd.DataFrame({'name': [students.at[i, 'name']], 'score': [students.at[i, 'score']]})
        groups[group_index] = pd.concat([groups[group_index], row], ignore_index=True)

    # Concatenate the list of DataFrames into one DataFrame
    # result = pd.concat(groups, ignore_index=True)
    print(groups)
    # print("num groups",numGroups)
    # print(result)
    return groups

def RandomiseStudents(students: pd.DataFrame, tolerance: int = 80) -> pd.DataFrame:
    size = students.shape[0]
    print(students)
    for i in range(size):
        silliness = random.randint(0, 1000)
        if silliness < tolerance:
            newPos = random.randint(0, size - 1)
            if newPos != i:
                print(i, newPos)
                temp = students.iloc[i].copy()
                students.iloc[i] = students.iloc[newPos]
                students.iloc[newPos] = temp
    print(students)
    
    return students

def main():
    inputFileName = input("file name: ")
    CreateXLSXFromCSV(inputFileName)

    myFile = SortXLSX()

    scores = myFile.iloc[:, 7]
    names = myFile.iloc[:, 0] + ', ' + myFile.iloc[:, 1]

    # print(names)
    # print(scores)
    students = pd.DataFrame({'name': names, 'score': scores})
    print(students)

    students = RandomiseStudents(students, 100)
    groups = MakeGroups(students, 4)

if __name__ == "__main__":
    main()