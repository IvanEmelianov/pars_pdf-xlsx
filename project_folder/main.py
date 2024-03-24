import os

from pdf_handler import PDF
from parser_handler import Parser
from excel_handler import Excel
from params import Params

if __name__ == "__main__":
    pdf_files = [f for f in os.listdir(Params.PDF_FOLDER) if f.endswith('.pdf')]

    for pdf_file in pdf_files:
        pdf_path = os.path.join(Params.PDF_FOLDER, pdf_file)
        pdf_data = PDF.extract_pdf_data(pdf_path)
        values = Parser.extract_value(pdf_data, Params.KEYWORD)
        if values:
            combined_values = '\n'.join(values)
            print(f"Распарсенные данные из файла {pdf_file}:\n{combined_values}\n")

            Excel.save_to_excel(combined_values, Params.EXCEL_FILE)