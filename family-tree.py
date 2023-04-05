import openpyxl
import subprocess
from dbscripts import * # all functions relating to the sqlite3 database
from person_init import * # all functions relating to the Person object

excel_path = r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE"
file_path = r"C:\Users\ASHil\PycharmProjects\Family-Tree\family-tree-data.xlsx"
people = []
person_name_dict = {}
person_id_dict = {}


def show_kids(person):
    for child in person.children:
        print(child)


def print_table():
    for person in people:
        print((f"{'ID:'} {person.parse_id} \t {'Name:'} {person.first_name} {person.last_name} \t "
              f"{'Class of '}{person.class_year}").expandtabs(15))


def get_person_by_id(person_id):
    if person_id == '':
        pass
    else:
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


def path_selection():
    global file_path, excel_path

    while True:
        print()
        print('Enter the path to either your EXCEL.EXE or the family-tree-data.xlsx')
        print('You will select which path it is in the next step')
        new_path = input('Enter path: ')
        raw_path = r"{}".format(new_path)
        print()
        print(f"Path: {raw_path}")
        selected = input('[1] Set path for EXCEL.EXE \n[2] Set path for family-tree-data.xlsx '
                         '\n[3] Change input \n[9] Go back \nInput choice: ')

        match selected:
            case'1':
                excel_path = raw_path
                print()
                break

            case '2':
                file_path = raw_path
                print()
                break

            case '3':
                print()

            case '9':
                print()
                break


def data_menu():
    print('***************** Data ******************')
    while True:
        global people

        print('Select action:')
        print('[1] Print table')
        print('[2] Open Excel')
        print('[3] Re-parse data')
        print('[4] Edit paths')
        print('[5] Display paths')
        print('[9] Go back')
        selected = input('Input choice: ')

        match selected:
            case '1':
                print()
                print_table()
                print()

            case '2':
                try:
                    subprocess.Popen([excel_path, file_path])
                    print('For changes to take effect you MUST close Excel AND then re-parse the data')
                    print()
                except Exception:
                    print('Error, verify correct paths')
                    print()

            case '3':
                clear_db_people()
                people, person_name_dict, person_id_dict = initialize_people()
                print()

            case '4':
                path_selection()

            case '5':
                print()
                print(f'Path to EXCEL.EXE: {excel_path}')
                print(f'Path to family-tree-data.xlsx: {file_path:}')
                print()

            case '9':
                print('*****************************************')
                print()
                break

            case '':
                print()


def search_menu():
    print('**************** Search *****************')
    while True:
        print('Select search criterion:')
        print('[1] ID')
        print('[2] Last name')
        print('[3] Class year')
        print('[9] Go back')
        selected = input('Input choice: ')

        match selected:
            case '1':
                print()
                get_person_by_id(input('Enter ID: '))

            case '2':
                print()
                print('Enter 9 to go back')
                print('NOTE: Input is case sensitive')
                while True:
                    get = input('Enter last name: ')
                    if get == '9':
                        break
                    else:
                        get_person_by_last(get)
                        print()

            case '3':
                print()
                get_person_by_year(input('Enter class year: '))
                print()

            case '9':
                print('*****************************************')
                print()
                break

            case '':
                print()
        print()


def relationships_menu():
    print('************* Relationships *************')
    while True:
        print('Select action:')
        print('[1] Immediate family')
        print('[2] Show all descendants')
        print('[3] Show all ancestors')
        print('[9] Go back')

        selected = input('Input choice: ')

        match selected:
            case '1':
                show_relationships()
            case '2':
                show_descendants()
            case '3':
                show_ancestors()
            case '9':
                print('*****************************************')
                print()
                break


def credits_menu():
    print('**************** Credits ****************')
    print('Historians: \t Tanner Hansard \'23 and Chris Huser \'22'.expandtabs(10))
    print('Traditions Chairs: \t Owen Dunston \'23, Aidan Hill \'23, and Liam Stevens \'23'.expandtabs(10))
    print('Vice President: \t Miles Baker \'23'.expandtabs(10))
    print('Comp Sci Major: \t Joshua Wood \'23'.expandtabs(10))
    print('*****************************************')
    print()


def show_ancestors():
    print()
    subject = int(input('Enter person ID: '))
    maxDepth = input('How many generations of ancestors? ')
    print()

    subject = person_id_dict[subject]
    future_nodes = [(subject, 0)]
    totalDepth = 0
    names = []

    while len(future_nodes) > 0:
        # take the first element from the list of future nodes
        this_person, depth = future_nodes.pop(0)

        # print the person's name
        # print(this_person.first_name, this_person.last_name)
        name = this_person.first_name + ' ' + this_person.last_name
        if len(names) > depth:
            names[depth].append(name)
        else:
            names.append([name])

        # update total depth
        totalDepth = max(depth, totalDepth)

        # break if max depth reached
        if maxDepth:
            if depth > int(maxDepth): break

        # add person's descendants
        for parent in this_person.parents:
            if (parent, depth + 1) not in future_nodes:
                future_nodes.append((person_id_dict[parent], depth + 1))

    print('*****************************************')
    for index, generation in enumerate(names):
        thisLine = "Generation " + str(totalDepth - index) + ":"
        for index2, name in enumerate(generation):
            thisLine += " " + name
            if index2 < len(generation) - 1:
                thisLine += ","
        print(thisLine)
    print('*****************************************')
    print()


def show_descendants():
    print()
    subject = int(input('Enter person ID: '))
    maxDepth = input('How many generations of descendants? ')
    print()

    subject = person_id_dict[subject]
    future_nodes = [(subject, 0)]
    names = []

    while len(future_nodes) > 0:
        # take the first element from the list of future nodes
        this_person, depth = future_nodes.pop(0)

        # print the person's name
        # print(this_person.first_name, this_person.last_name)
        name = person_name_dict[this_person.parse_id]
        if len(names) > depth:
            names[depth].append(name)
        else:
            names.append([name])

        # break if max depth reached
        if maxDepth:
            if depth > int(maxDepth):
                break

        # add person's descendants
        for child in this_person.children:
            if (child, depth + 1) not in future_nodes:
                future_nodes.append((person_id_dict[child], depth + 1))

    print('*****************************************')
    for index, generation in enumerate(names):
        thisLine = "Generation " + str(index) + ":"
        for index2, name in enumerate(generation):
            thisLine += " " + name
            if index2 < len(generation) - 1:
                thisLine += ","
        print(thisLine)
    print('*****************************************')
    print()


def show_relationships():
    print()
    subject = int(input('Enter person ID: '))
    print()
    subject = person_id_dict[subject]

    tense = 'old man' if len(subject.parents) == 1 else 'old men'
    print(f'{subject.first_name} {subject.last_name}\'s {tense}:')
    for parent in subject.parents:
        if parent:
            print(person_name_dict[parent])

    print(f'\n{subject.first_name} {subject.last_name}\'s buffo:')
    for child in subject.children:
        if child:
            print(person_name_dict[child])

    print()


def main():
    print('Welcome to the Singing Cadet family tree project! Here you can lookup any recorded member to see their '
          'family tree!')
    print('Github Repo: https://github.com/ASHill11/Family-Tree')
    print()
    while True:
        print('*************** Main Menu ***************')
        print('[1] Search')
        print('[2] Relationships')
        print('[7] Data')
        print('[8] Credits')
        print('[9] Exit')
        selected = input('Input choice: ')
        print()

        match selected:
            case '1':
                search_menu()

            case '2':
                relationships_menu()

            case '7':
                data_menu()

            case '8':
                credits_menu()

            case '9':
                exit()

people, person_name_dict, person_id_dict = initialize_people()
main()
