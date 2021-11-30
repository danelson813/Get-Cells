
import gspread
import re

# Establish connection
gc = gspread.service_account('mysecrets.json')

# Get spreadsheet
spreadsheet = gc.open('Weather Sheet') 

# Get worksheet
worksheet1 = spreadsheet.worksheet('2013')

# get cell 
cell1 = worksheet1.get_values('D5')[0][0]

# get cell using acell
cell2 = worksheet1.acell('D5').value

# print(cell1, cell2)

# search for a cell
cell3 = worksheet1.find('-10')

# print(cell3.row, cell3.col)

# search for many cells

cells = worksheet1.findall('-9')
# print(cells)
cells4 = [(cell.row, cell.col) for cell in cells]
# for cell in cells:
  # print(cell.row, cell.col)

# search for cells using re 
reg = re.compile(r'99')
cells5 = worksheet1.findall(reg)
for cell in cells5:
  print(cell.row, cell.col)