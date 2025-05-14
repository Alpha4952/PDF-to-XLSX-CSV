# PDF-to-XLSX-CSV
## A simple python script that converts PDF files into excel or csv files.

### Dependencies
Python 3.13.2  
pandas 2.2.3  
pdfminer.six 20250327  
pdfplumber 0.11.6  

### Usage
1. Execute the file using  
```
py main.py
```
2. Enter your filename (without the .pdf extension).  
Example: with "salary.pdf", please input "salary".  
3. Choose your export format:
  Enter 1 for CSV
  Enter 2 for XLSX  
5. Sit back and watch!  
6. Output
Each table will be exported as a separate file using the following format:  
```{filename}_{number of page the table is from}_{number of table from the page}.{csv/xlsx}```
If your input file is salary.pdf, you might get:
  salary_1_1.xlsx  
  salary_1_2.xlsx  
  salary_2_1.xlsx  
Each file represents:  
  The original filename  
  The PDF page number  
  The table index on that page  

### Notes  
  Works best on PDFs with actual tables — not scanned images.  
  You may need to customize the code for the best results.  

### License
MIT — free to use, modify, and share.
