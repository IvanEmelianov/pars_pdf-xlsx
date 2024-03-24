from openpyxl import Workbook

from params import Params

class Excel(Params):
    @staticmethod
    def save_to_excel(data, excel_file):
        wb = Workbook()
        ws = wb.active
        lines = data.split('\n')
        for row_num, line in enumerate(lines, start=1):
            ws.cell(row=row_num, column=1, value=line)
        wb.save(excel_file)