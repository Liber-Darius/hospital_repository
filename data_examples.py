from modules.department import Department
import unittest
from modules.patient import Patient
from infrastructure.repository import departmentRepository
from utils.sorting import mySearch
from utils.sorting import mySort
from utils.sorting import quickSort
from application.controller import HospitalController

controller = HospitalController()

a = Patient("Pop", "Amalia", 5040903243824, "unknown") #16
b = Patient("Berchis", "Iulia", 6030302243823, "flu")  # 17
c = Patient("Mezei", "Eric", 2980302243823, "stroke")  # 22
d = Patient("Orghici", "Remus", 1920302543823, "stroke")  # 28
e = Patient("Tache", "Anastasia", 2920302243823, "unknown")  # 28
f = Patient("Noveanu", "Marcus", 6050302243823, "hypertension")  # 15
g = Patient("Berchis", "Anamaria", 1900403243823, "seizure")  # 30
h = Patient("Pop", "Luca", 5010302243823, "flu")  # 19
i = Patient("Podolac", "Eduard", 5010704243823, "diabetes")  # 19

depo1 = Department(2, "Cardiology", 34, [a, b, c])  #16  #17 #22 #28
depo2 = Department(27, "Orthopedics", 15, [e, f, g])  # 28 #15 #30
depo3 = Department(19, "Emergencies", 25, [h, i])  # 19 #19

controller.add_department(depo1)
controller.add_department(depo2)
controller.add_department(depo3)
print("#"*90)
print("Here is the list of the departments:\n ")
i=0
for elem in controller.get_controller():
    print(str(i) + "." + str(elem))
    i+=1
print("#"*90)
controller.update_department_at_index(2,"Analysis", 892, 78)
print("Here is the list of the departments after updating department of index 2 with: Analysis, 892, 78\n ")
i=0
for elem in controller.get_controller():
    print(str(i) + "." + str(elem))
    i+=1
print("#"*90)
print("repository being sorted by number of patients: \n")
controller.sort_by_number_of_patients()
i=0
for elem in controller.get_controller():
    print(str(i) + "." + str(elem))
    i+=1
print("#" * 90)
print("repository being sorted by number of patients having the age above 25: \n")
controller.sort_and_filter_by_number_of_patients_over_age(25)
i=0
for elem in controller.get_controller():
    print(str(i) + "." + str(elem))
    i+=1
print("#" * 90)
print("repository being sorted by number of patients and the patients alphabetically: \n")
controller.sort_by_number_of_patients_alphabeticaly()
i=0
for elem in controller.get_controller():
    print(str(i) + "." + str(elem))
    i+=1
print("#" * 90)
print("repository being sorted by number of patients having the age above 25: \n")
controller.sort_and_filter_by_number_of_patients_over_age(25)
i=0
for elem in controller.get_controller():
    print(str(i) + "." + str(elem))
    i+=1
print("#" * 90)
print("the departments with patients under the age of 16 are: \n")
print(*controller.get_departments_with_patients_under(16))
print("#" * 90)
print("the departments with patients the first name Pop are:: \n")
print(*controller.get_departments_with_patients_with_first_name("Pop"))
print("#" * 90)
print("department of index 0 before adding patient: \n" + str(d) + "\n" + str(controller.get_department_of_index(0)))
controller.add_patient_to_department(d,0)
print("#"*90)
print("department of index 0 after adding patient: \n" + str(controller.get_department_of_index(0)))
print("#"*90)
controller.sort_patients_from_department_by_CNP(0)
print("department of index 0 after being sorted by cnp: \n" + str(controller.get_department_of_index(0)))
print("#"*90)
print("the patients from department of index 0 that contain string: Po : " )
for elem in controller.get_department_of_index(0).getPatientsThatContainString("Po"):
    print(elem)
print("#"*90)
controller.delete_patient_from_department(1,0)
print("department of index 1 after deleting patient of index 0 : \n ")
print(controller.get_department_of_index(1))
print("#"*90)
controller.update_patient_from_department(1,0, "Mihai", "Chindris", 6070904243823, "dead")
print("department of index 1 after updating patient of index 0  with: Mihai, Chindris, 6070904243823:, dead \n ")
print(controller.get_department_of_index(1))
print("#"*90)
controller.delete_department_of_index(2)
print("Here is the list of the departments after deleting department of index 2:\n ")
i=0
for elem in controller.get_controller():
    print(str(i) + "." + str(elem))
    i+=1
print("#"*90)





print()