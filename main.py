import os
import re
from PyPDF2 import PdfReader
from openpyxl import Workbook

def extract_pdf_data(pdf_file):
    text = ''
    with open(pdf_file, 'rb') as file:
        reader = PdfReader(file)
        for page_num in range(len(reader.pages)):
            text += reader.pages[page_num].extract_text()
    return text

def extract_value(text, keyword):
    pattern = re.compile(rf'{re.escape(keyword)}\s*(.*?)(\s{2}|$)', re.DOTALL)
    match = re.search(pattern, text)
    if match:
        value = match.group(1).strip()
        # Находим первые две строки после ключевого слова
        first_two_lines = '\n'.join(value.split('\n')[:2])
        return first_two_lines
    else:
        return None

def save_to_excel(data, excel_file):
    wb = Workbook()
    ws = wb.active
    lines = data.split('\n')
    for row_num, line in enumerate(lines, start=1):
        ws.cell(row=row_num, column=1, value=line)
    wb.save(excel_file)

# Папка с PDF-файлами
pdf_folder = r'D:\pars\pdf'

# Создаем Excel-файл для записи данных
excel_file = r'D:\pars\output.xlsx'

# Ключевое слово для поиска значения
keyword = "Адрес скважины и положение ее в рельефе"

# Перебираем все файлы в папке
for filename in os.listdir(pdf_folder):
    if filename.endswith('.pdf'):
        pdf_file = os.path.join(pdf_folder, filename)
        pdf_data = extract_pdf_data(pdf_file)
        value = extract_value(pdf_data, keyword)
        if value:
            save_to_excel(value, excel_file)
