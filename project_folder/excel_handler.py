from openpyxl import Workbook
from params import Params


class Excel(Params):
    @staticmethod
    def save_to_excel(data, excel_file):
        wb = Workbook()
        ws = wb.active

        # Заголовки столбцов (если нужны)
        ws.append(["Address", "Location"])

        # Записываем данные в одну строку
        ws.append([data.replace("\n", " ")])

        wb.save(excel_file)