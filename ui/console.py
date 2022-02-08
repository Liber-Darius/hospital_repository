
from infrastructure.repository import departmentRepository
from modules.department import Department
from modules.patient import Patient
from application.controller import HospitalController

def printMenu():
    print("*" * 110)
    print("0 - exit")
    print("1 - create department") #
    print("2 - show list of departments") #
    print("3 - add patient to department") #
    print("4 - delete patient from department") #
    print("5 - update patient from department") #
    print("6 - delete department") #
    print("7 - update department name, id and number of beds")
    print("8 - sort the patients in a department by personal numerical code") #
    print("9 - sort departments by the number of patients") #
    print("10 - sort departments  by the  number  of  patients having  the  age  above  a  given  limit") #
    print("11 - sort  departments  by  the  number  of  patients  and  the  patients  in  a  department alphabetically ") #
    print("12 - identify departments where there are patients under a given age") #
    print("13 - identify  patients  from  a  given  department  for  which  the  first or  last  name contain a given string") #
    print("14 - identify departments where there are patients with a given first name") #
    print("15 - form groups  of k patients  from  the  same  department  and  the  same  disease ")
    print("16 - form  groups  of k departments having  at  most patients  suffering  from  the  same disease")
    print("*" * 110)

def run(controller: HospitalController):

    printMenu()
    command = input(">>> ")
    while command != "0":
        f = Department()
        if command == "1":
            departmentName = input("Enter the department name: ")
            while True:
                try:
                    departmentID = int(input("Enter the department ID: "))
                    if controller.check_ID(departmentID):
                        raise ValueError
                    break
                except ValueError:
                    print("the ID already exists or is not valid, please try again... ")
            departmentBeds = int(input("Enter the department number of beds: "))
            departmentLength = int(input("Enter the department list of patients length: "))
            f = Department(departmentID, departmentName, departmentBeds, [])
            for elem in range (0, departmentLength):
                patiento = Patient()
                print("Patient number: ", elem + 1)
                firstName = input("Enter the first name: ")
                lastName = input("Enter the last name: ")
                while True:
                    try:
                        cnp = int(input("Enter the cnp: "))
                        patiento.setCNP(cnp)
                        f.checkCNP(cnp)
                        break
                    except ValueError:
                        print("the cnp entered already exists or is not 13 letters long, please try again... ")
                disease = input("Enter the disease: ")
                patiento = Patient(firstName, lastName, cnp, disease)
                f.addPatient(patiento)
            controller.add_department(f)

        elif command == "2":
            for elem in controller.get_controller():
                print(elem)

        elif command == "3":
            print("Here is the list of the departments:\n ")
            i=1
            for elem in controller.get_controller():
                print(str(i) + "." + str(elem))
                i+=1
                patiento = Patient()
            while True:
                try:
                    index = int(input("Select the department (by the number before the dot): "))
                    controller.repository_index_check(index-1)
                    break
                except IndexError:
                    print("the index is not valid, please try again... " )
            firstName = input("Enter the first name: ")
            lastName = input("Enter the last name: ")
            while True:
                try:
                    cnp = int(input("Enter the cnp: "))
                    patiento.setCNP(cnp)
                    f.checkCNP(cnp)
                    break
                except ValueError:
                    print("the cnp entered already exists or is not 13 letters long, please try again... ")
            disease = input("Enter the disease: ")
            patiento = Patient(firstName, lastName, cnp, disease)
            controller.add_patient_to_department(patiento, index-1)

        elif command == "4":
            print("Here is the list of the departments:\n ")
            i=1
            for elem in controller.get_controller():
                print(str(i) + "." + str(elem))
                i+=1
            while True:
                try:
                    index1 = int(input("Select the department (by the number before the dot): "))
                    controller.repository_index_check(index1-1)
                    break
                except IndexError:
                    print("the index is not valid, please try again... " )
            i = 1
            print("\nHere is the list of the patients:\n ")
            for elem in controller.get_department_of_index(index1-1).get():
                print(str(i) + "." + str(elem))
                i += 1
            while True:
                try:
                    index2 = int(input("\nSelect the patient (using the number before the dot): "))
                    controller.get_department_of_index(index1-1).departmentIndexCheck(index2-1)
                    break
                except IndexError:
                    print("the index is not valid, please try again... ")

            controller.delete_patient_from_department(index1-1, index2 - 1)

        elif command == "5":
            print("Here is the list of the departments:\n ")
            i = 1
            for elem in controller.get_controller():
                print(str(i) + "." + str(elem))
                i += 1
            while True:
                try:
                    index1 = int(input("Select the department (by the number before the dot): "))
                    controller.repository_index_check(index1 - 1)
                    break
                except IndexError:
                    print("the index is not valid, please try again... ")
            i = 1
            print("\nHere is the list of the patients:\n ")
            for elem in controller.get_department_of_index(index1 - 1).get():
                print(str(i) + "." + str(elem))
                i += 1
            while True:
                try:
                    index2 = int(input("\nSelect the patient (using the number before the dot): "))
                    controller.get_department_of_index(index1 - 1).departmentIndexCheck(index2 - 1)
                    break
                except IndexError:
                    print("the index is not valid, please try again... ")
            while True:
                try:
                    cnp = int(input("Enter the cnp: "))
                    patiento.setCNP(cnp)
                    f.checkCNP(cnp)
                    break
                except ValueError:
                    print("the cnp entered already exists or is not 13 letters long, please try again... ")
            firstName = input("Enter the first name: ")
            lastName = input("Enter the last name: ")
            disease = input("Enter the disease: ")
            controller.update_patient_from_department(index1-1, index2-1, firstName, lastName, cnp, disease)

        elif command == "6":
            print("Here is the list of the departments:\n ")
            i = 1
            for elem in controller.get_controller():
                print(str(i) + "." + str(elem))
                i += 1
            while True:
                try:
                    index1 = int(input("Select the department (using the number before the dot): "))
                    controller.delete_department_of_index(index1-1)
                    break
                except IndexError:
                    print("the index is not valid, please try again... ")

        elif command == "7":
            print("Here is the list of the departments:\n ")
            i = 1
            for elem in controller.get_controller():
                print(str(i) + "." + str(elem))
                i += 1
            while True:
                try:
                    index1 = int(input("Select the department (using the number before the dot): "))
                    controller.repository_index_check(index1 - 1)
                    break
                except IndexError:
                    print("the index is not valid, please try again... ")
            departmentName = input("Enter the department name: ")
            departmentID = int(input("Enter the department ID: "))
            departmentBeds = int(input("Enter the department number of beds: "))
            controller.update_department_at_index(index1-1, departmentName, departmentID, departmentBeds)

        elif command == "8":
            print("Here is the list of the departments:\n ")
            i = 1
            for elem in controller.get_controller():
                print(str(i) + "." + str(elem))
                i += 1
            while True:
                try:
                    index1 = int(input("Select the department (using the number before the dot): "))
                    controller.sort_patients_from_department_by_CNP(index1 - 1)
                    break
                except IndexError:
                    print("the index is not valid, please try again... ")

        elif command == "9":
            controller.sort_by_number_of_patients()

        elif command == "10":
            age = int(input("Enter the limit: "))
            controller.sort_and_filter_by_number_of_patients_over_age(age)

        elif command == "11":
            controller.sort_by_number_of_patients_alphabeticaly()

        elif command == "12":
            age = int(input("enter age: "))
            print("here are the departments which satisfy the condition:\n")
            for elem in controller.get_departments_with_patients_under(age):
                print(str(elem))

        elif command == "13":
            print("Here is the list of the departments:\n ")
            i = 1
            for elem in controller.get_controller():
                print(str(i) + "." + str(elem))
                i += 1
            while True:
                try:
                    index1 = int(input("Select the department (by the number before the dot): "))
                    controller.repository_index_check(index1 - 1)
                    break
                except IndexError:
                    print("the index is not valid, please try again... ")
            stringus = input("enter the string: ")
            for elem in controller.get_department_of_index(index1 - 1).getPatientsThatContainString(stringus):
               print(str(elem))

        elif command == "14":
            firstName = int(input("enter the first name: "))
            print("here are the departments which satisfy the condition:\n")
            for elem in controller.get_departments_with_patients_with_first_name(firstName):
                print(str(elem))
        elif command == "0":
                print("Have a nice day!")
                exit()
                
        else:
            print("command ",command, " not found")

        printMenu()
        command = input(">>> ")

if __name__ == "__main__":
    controller = HospitalController()
    run(controller)