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
    """
    Reads data from an Excel file and returns a list of Person objects
    """
    # Load the workbook and select the first worksheet
    workbook = openpyxl.load_workbook(filename)
    worksheet = workbook.active

    # Initialize a list to hold the Person objects
    people_list = []

    # Loop through each row in the worksheet until an empty row is reached
    row_num = 2  # start at row 2 to skip the header row
    while worksheet.cell(row=row_num, column=1).value is not None:
        # Get the data from the row and create a Person object
        id_num = worksheet.cell(row=row_num, column=1).value
        id_num.zfill(4)
        first_name = worksheet.cell(row=row_num, column=2).value
        last_name = worksheet.cell(row=row_num, column=3).value
        class_year = worksheet.cell(row=row_num, column=4).value
        parent_1 = worksheet.cell(row=row_num, column=5).value
        parent_2 = worksheet.cell(row=row_num, column=6).value
        parent_3 = worksheet.cell(row=row_num, column=7).value
        child_1 = worksheet.cell(row=row_num, column=8).value
        child_2 = worksheet.cell(row=row_num, column=9).value
        child_3 = worksheet.cell(row=row_num, column=10).value
        child_4 = worksheet.cell(row=row_num, column=11).value
        child_5 = worksheet.cell(row=row_num, column=12).value
        person = Person(id_num, first_name, last_name, class_year, parent_1, parent_2, parent_3, child_1, child_2,
                        child_3, child_4, child_5)

        # Add the Person object to the list
        people_list.append(person)

        # Move to the next row
        row_num += 1

    # Close the workbook and return the list of Person objects
    workbook.close()
    return people_list


people = read_excel_data('family-tree-data.xlsx')


def print_table():
    for person in people:
        print((f"{'ID:'} {person.parse_id} \t {'Name:'} {person.first_name} {person.last_name} \t "
              f"{'Class of '}{person.class_year}").expandtabs(15))


def get_person_by_id(person_id):
    person_id = int(person_id)
    for person in people:
        if person.parse_id == person_id:
            print(person.first_name, person.last_name)
            print()
            return person
    print("No person found with ID:", person_id)
    print()
    return None


def get_person_by_last(person_last):
    people_list = []
    for person in people:
        if person.last_name == person_last:
            print(f"Parse ID for {person.first_name} {person.last_name}: {person.parse_id}")
            people_list.append(person)

    if not people_list:
        print("No people found with last name:", person_last)

    return people_list


def get_person_by_year(person_year):
    people_list = []
    person_year = int(person_year)
    for person in people:
        if person.class_year == person_year:
            print(f"{person.first_name} {person.last_name}")
            people_list.append(person)

    if not people_list:
        print(f"No people found with class of {person_year}")

    return people_list

def main():
    print('Welcome to the Singing Cadet family tree project! Here you can lookup any recorded member to see their '
          'family tree!')
    print('Github Repo: https://github.com/ASHill11/Family-Tree')
    print()
    while True:
        print('*************** Main Menu ***************')
        print('[1] Search')
        print('[8] Data')
        print('[9] Exit')
        selected = input('Input choice: ')
        print()

        if selected == '1':
            print('**************** Search *****************')
            while True:
                print('Select search criterion')
                print('[1] ID')
                print('[2] Last name')
                print('[3] Class year')
                print('[9] Go back')
                selected = input('Input choice: ')

                if selected == '1':
                    print()
                    get_person_by_id(input('Enter ID: '))

                elif selected == '2':
                    print()
                    get_person_by_last(input('Enter last name: '))
                    print()

                elif selected == '3':
                    print()
                    get_person_by_year(input('Enter class year: '))
                    print()

                elif selected == '9':
                    print('*****************************************')
                    print()
                    break

                else:
                    print()

        elif selected == '8':
            print('***************** Data ******************')
            while True:
                print('Select action')
                print('[1] Print table')
                print('[9] Go back')
                selected = input('Input choice: ')

                if selected == '1':
                    print()
                    print_table()
                    print()

                elif selected == '9':
                    print('*****************************************')
                    print()
                    break

                else:
                    print()

        elif selected == '9':
            exit()


main()
