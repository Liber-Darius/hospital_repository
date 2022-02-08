from modules.patient import Patient
from utils.sorting import mySearch
from utils.sorting import mySort
from utils.sorting import quickSort
from modules.department import Department

class departmentRepository:

    def __init__(self, list_of_departments = []):
        self.__list_of_departments = list_of_departments

    def addDepartment(self, department):
        self.__list_of_departments.append(department)

    def __len__(self):
        return len(self.__list_of_departments)

    def addPatientToDepartment(self, patient, index):
        self.repositoryIndexCheck(index)
        self.__list_of_departments[index].addPatient(patient)

    def deletePatientFromDepartment(self, index1, index2):
        self.repositoryIndexCheck(index1)
        self.__list_of_departments[index1].deletePatientByIndex(index2)

    def updatePatientFromDepartment(self, index1, index2, firstName, lastname, cnp, disease):
        self.repositoryIndexCheck(index1)
        self.__list_of_departments[index1].updatePatientAtIndex(index2, firstName, lastname, cnp, disease)

    def deleteDepartmentOfIndex(self, index):
        ok = -1
        if index < 0 or index >= len(self.__list_of_departments):
            raise IndexError
            ok = 1
        if ok == -1:
            del self.__list_of_departments[index]

    def repositoryIndexCheck(self, index):
        if index < 0 or index >= len(self.__list_of_departments):
            raise IndexError

    def checkID(self, id):
        '''
        checks whether an id exists in the repository
        input: id - an integer
        output: a truth value
        '''
        for elem in self.__list_of_departments:
            if id == elem.getID():
                return True  # it exists
        return False  # it doesn't

    def getDepartmentOfIndex(self, index):
        self.repositoryIndexCheck(index)
        return self.__list_of_departments[index]

    def updateDepartmentAtIndex(self, index, departmentName, departmentID, departmentBeds):
        self.repositoryIndexCheck(index)
        self.__list_of_departments[index].updateDepartment(departmentName, departmentID, departmentBeds)

    def sortPatientsFromDepartmentByCNP(self, index):
        if index < 0 or index >= len(self.__list_of_departments):
            raise IndexError
        self.__list_of_departments[index].mySortByCNP()

    def get(self):
        return self.__list_of_departments

    '''
    Sort the patients in a department by personal numerical code
     Sort departments by the number of patients
     Sort departments by the number of patients having the age above a given limit (for
    example, above 50 years old)
     Sort departments by the number of patients and the patients in a department
    alphabetically
     Identify departments where there are patients under a given age
    '''


    def mySortByNumberOfPatientsAlphabeticaly(self):
        '''
        sorts by number of patients
        '''
        for elem in self.__list_of_departments:
            elem.sortByFirstAndLastName()

        return mySort(self.__list_of_departments, lambda x, y: len(x.get()) <= len(y.get()))

    def mySortByNumberOfPatients(self):
        '''
        sorts by number of patients
        '''
        return mySort(self.__list_of_departments, lambda x, y: len(x.get()) <= len(y.get()))

    def sortAndFilterByNumberOfPatientsOverAge(self, age):
        '''
        sorts by number of patients having the age above a given one
        input: age - an integer
        '''

        return mySort(self.__list_of_departments, lambda x, y: x.numberOfPatientsOlderThan(age) <= y.numberOfPatientsOlderThan(age))

    def getDepartmentsWithPatientsUnder(self, age):
        '''
        sorts by number of patients having the age above a given one
        input: age - an integer
        '''
        return mySearch(self.__list_of_departments, lambda x: x.numberOfPatientsYoungerThan(age) > 0)

    def getDepartmentsWithPatientsWithFirstName(self, firstName):
        return mySearch(self.__list_of_departments, lambda x: x.numberOfPatientsWithFirstName(firstName) > 0)
