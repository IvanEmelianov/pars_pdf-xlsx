import re

from params import Params


class Parser(Params):
    @staticmethod
    def extract_value(text, keyword):


        pattern = re.compile(rf'{re.escape(keyword)}\s*(.*?)(?:\n|$)', re.DOTALL)
        match = pattern.search(text)

        if match:
            lines = match.group(1).strip().split('\n')
            if len(lines) >= 2:
                first_two_lines = '\n'.join(lines[:2])
                values = [first_two_lines]

                print(f"Результат парсинга:\n{values}\n")  # Отладочный вывод

                return values

        print("Совпадения не найдены")  # Отладочный вывод
        return None