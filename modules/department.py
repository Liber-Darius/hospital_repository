from modules.patient import Patient
from utils.sorting import mySearch
from utils.sorting import mySort
from utils.sorting import quickSort
class Department:
    def __init__(self, id = 0, name = " ", beds = 0 ,  list_of_patients = []):
        self.__id = id
        self.__name = name
        self.__beds = beds
        self.__list_of_patients = list_of_patients

    def getName(self):
        return self.__name

    def getBeds(self):
        return self.__beds

    def setID(self, id):
        self.__id == id

    def getID(self):
        return self.__id

    def departmentIndexCheck(self, index):
        if index < 0 or index >= len(self.__list_of_patients):
            raise IndexError

    def checkCNP(self, cnp):
        '''
        checks whether an id exists in the repository
        input: cnp - an integer
        output: a truth value
        '''
        if len(str(cnp)) != 13:
            raise ValueError
        for elem in self.__list_of_patients:
            if cnp == elem.getCNP():
                raise ValueError

    def __len__(self):
        return len(self.__list_of_patients)

    def __str__(self):
        msg =  "Department " + self.__name + " of id: " + str(self.__id) + " with a capacity of " + str(self.__beds) + " beds, and the following patients: \n "
        for elem in range (0, len(self.__list_of_patients)):
            msg += str(self.__list_of_patients[elem])
            msg += "\n "
        return msg

    def __eq__(self, other):
        if self.getID() == other.getID() and self.getName() == other.getName() and self.getBeds() == other.getBeds() and self.get() == other.get():
            return True
        else:
            return False

    def get(self):
        return self.__list_of_patients

    def addPatient(self, patient):
        self.__list_of_patients.append(patient)

    def getPatientAtIndex(self, index):
        if index < 0 or index >= len(self.__list_of_patients):
            raise IndexError
        return self.__list_of_patients[index]

    def deletePatientByIndex(self, index):
        if index < 0 or index >= len(self.__list_of_patients):
            raise IndexError
        del self.__list_of_patients[index]

    def deletePatientByCNP(self, cnp):
        ok = -1
        for i in range(0, len(self.__list_of_patients)):
            if self.__list_of_patients[i].getCNP() == cnp:
                ok = i
                break
        if ok != -1:
            del self.__list_of_patients[ok]

    def updateDepartment(self, new_departmentName, new_departmentID, new_departmentBeds):
        self.__name = new_departmentName
        self.__id = new_departmentID
        self.__beds = new_departmentBeds

    def updatePatientAtIndex(self, index, new_firstName, new_lastName, new_cnp, new_disease):
        '''
        updates patient
        input: index - an integer
            new_firstName = a string
            new_lastName = a string
            new_cnp = a string
            new_disease = a string
        '''
        if index < 0 or index >= len(self.__list_of_patients):
            raise IndexError
        self.checkCNP(new_cnp)
        if new_cnp == self.__list_of_patients[index].getCNP():
            self.__list_of_patients[index].setCNP(new_cnp)
        else:
            self.__list_of_patients[index].setCNP(new_cnp)

        self.__list_of_patients[index].setFirstName(new_firstName)
        self.__list_of_patients[index].setLastName(new_lastName)
        self.__list_of_patients[index].setDisease(new_disease)

    def mySortByCNP(self):
        '''
        sorts by cnp
        '''

        return mySort(self.__list_of_patients, lambda x, y: x.getCNP() < y.getCNP())

    def numberOfPatientsOlderThan(self, age):
        '''
        returns the number of patients older than a given age 
        input: age - an integer
        '''
        nbr = 0
        for elem in self.__list_of_patients:
            if elem.getAge() > age:
                nbr += 1
        return nbr

    def numberOfPatientsWithFirstName(self, firstName):
        '''
        returns the number of patients older than a given age
        input: age - an integer
        '''
        nbr = 0
        for elem in self.__list_of_patients:
            if elem.getFirstName() == firstName:
                nbr += 1
        return nbr

    def numberOfPatientsYoungerThan(self, age):
        '''
        returns the number of patients older than a given age
        input: age - an integer
        '''
        nbr = 0
        for elem in self.__list_of_patients:
            if elem.getAge() < age:
                nbr += 1
        return nbr

    def sortByFirstAndLastName(self):
        '''
        sorts by first and last name
        '''
        return mySort(self.__list_of_patients, lambda x, y: x.getFirstName()+x.getLastName() < y.getFirstName()+y.getLastName() )


    def getPatientsThatContainString(self, stringus):
        '''
        filters the patients that have a given string in their first or last name
        input: stringus - a string
        '''
        return mySearch(self.__list_of_patients, lambda x: stringus.lower() in x.getFirstName().lower() or stringus.lower() in  x.getLastName().lower())





