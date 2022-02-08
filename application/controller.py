from infrastructure.repository import departmentRepository
from modules.department import Department
from modules.patient import Patient
class HospitalController:

    def __init__(self, repo: departmentRepository = departmentRepository()):
        self.__repo = repo

    def repository_index_check(self, index):
        self.__repo.repositoryIndexCheck(index)

    def get_controller(self):
        return self.__repo.get()

    def add_department(self, department: Department):
        self.__repo.addDepartment(department)

    def add_patient_to_department(self, patient: Patient, index):
        self.__repo.addPatientToDepartment(patient, index)

    def delete_patient_from_department(self, index1, index2):
        self.__repo.deletePatientFromDepartment(index1, index2)

    def update_patient_from_department(self, index1, index2, firstName, lastName, cnp, disease):
        self.__repo.updatePatientFromDepartment(index1, index2, firstName, lastName, cnp, disease)

    def delete_department_of_index(self, index):
        self.__repo.deleteDepartmentOfIndex(index)

    def check_ID(self, id):
        return self.__repo.checkID(id)

    def get_department_of_index(self, index):
        return self.__repo.getDepartmentOfIndex(index)

    def update_department_at_index(self,index, departmentName, departmentID, departmentBeds):
        self.__repo.updateDepartmentAtIndex(index, departmentName, departmentID, departmentBeds)

    def sort_patients_from_department_by_CNP(self,index):
        self.__repo.sortPatientsFromDepartmentByCNP(index)

    def sort_by_number_of_patients_alphabeticaly(self):
        self.__repo.mySortByNumberOfPatientsAlphabeticaly()

    def sort_by_number_of_patients(self):
        self.__repo.mySortByNumberOfPatients()

    def sort_and_filter_by_number_of_patients_over_age(self, age):
        self.__repo.sortAndFilterByNumberOfPatientsOverAge(age)

    def get_departments_with_patients_under(self, age):
        return self.__repo.getDepartmentsWithPatientsUnder(age)

    def get_departments_with_patients_with_first_name(self, firstName):
        return self.__repo.getDepartmentsWithPatientsWithFirstName(firstName)



