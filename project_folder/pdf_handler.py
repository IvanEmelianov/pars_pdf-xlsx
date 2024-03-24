import os
from PyPDF2 import PdfReader

from params import Params

class PDF(Params):
    @staticmethod
    def extract_pdf_data(pdf_file):
        text = ''
        with open(pdf_file, 'rb') as file:
            reader = PdfReader(file)
            for page_num in range(len(reader.pages)):
                text += reader.pages[page_num].extract_text()
        return text