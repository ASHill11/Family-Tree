import openpyxl


class Person:
    def __init__(self, first_name, last_name, class_year, parse_id, parent_1=None, parent_2=None, parent_3=None, child_1=None, child_2=None, child_3=None, child_4=None, child_5=None):
        self.parse_id = parse_id
        self.first_name = first_name
        self.last_name = last_name
        self.class_year = class_year
        self.parent_1 = parent_1
        self.parent_2 = parent_2
        self.parent_3 = parent_3
        self.child_1 = child_1
        self.child_2 = child_2
        self.child_3 = child_3
        self.child_4 = child_4
        self.child_5 = child_5


def read_excel_data(filename):
    wb = openpyxl.load_workbook(filename)
    sheet = wb.active
    data = []
    for row in sheet.iter_rows(min_row=2, values_only=True):
        person = Person(*row)
        data.append(person)
    return data


people = read_excel_data('family-tree-data.xlsx')
for person in people:
    print(f"ID: {person.parse_id}, Name: {person.first_name} {person.last_name} Class Year: {person.class_year}")

