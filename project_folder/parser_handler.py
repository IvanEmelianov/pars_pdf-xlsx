import re

from params import Params


class Parser(Params):
    @staticmethod
    def extract_value(text, keyword):


        start_index = text.find(keyword)

        if start_index != -1:
            substring = text[start_index:]
            lines = substring.split('\n')
            if len(lines) >= 3:
                values = [line.strip() for line in lines[:2]]

                values[0] = values[0].replace(keyword, '').strip()

                print(f"Результат парсинга:\n{values}\n")  # Отладочный вывод

                return values

        print("Совпадения не найдены")  # Отладочный вывод
        return None
