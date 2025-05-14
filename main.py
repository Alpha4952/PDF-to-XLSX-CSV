import pdfplumber
import pandas as pd
import logging

logging.getLogger("pdfminer").setLevel(logging.ERROR)

try:
    filename = input('Name of the file (please ignore filename): ')
    with pdfplumber.open(f'{filename}.pdf') as pdf:
        pass
except:
    print('Cannot find the file')
    exit()

try:
    filetype = input('What do you want to turn this file into?\n[1] CSV     [2] XLSX\n')
except:
    print('Not a number, please enter a number')
    exit()

if (filetype != '1') & (filetype != '2'):
    print('Not a valid number, please enter 1 or 2.')
    exit()

dfs = []
with pdfplumber.open(f'{filename}.pdf') as pdf:
    pages = pdf.pages
        
    for i in range(len(pages)):
        print(f'Reading page {i + 1}')

        page = pages[i]
        tables = page.extract_tables()
        
        for j in range(len(tables)):
            print(f'Reading table {j + 1}')

            df = pd.DataFrame(tables[j][1:], columns = tables[j][0])
            
            if filetype == '1':
                df.to_csv(f'{filename}_{i + 1}_{j + 1}.csv', index = 0)
                print(f'Exported {filename}_{i + 1}_{j + 1}.csv')
            else:
                df.to_excel(f'{filename}_{i + 1}_{j + 1}.xlsx', index = 0)
                print(f'Exported {filename}_{i + 1}_{j + 1}.xlsx')
print('Done! Have a good day!')
