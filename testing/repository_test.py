from modules.department import Department
import unittest
from modules.patient import Patient
from infrastructure.repository import departmentRepository
class Test(unittest.TestCase):
    def testAddAndGetDepartment(self):
        depo1 = Department(2, "Cardiology", 34, [])
        b = Patient("Berchis", "Iulia", 6030302243823, "flu")  # 17
        c = Patient("Mezei", "Eric", 2980302243823, "stroke")  # 22
        d = Patient("Orghici", "Remus", 1920302543823, "stroke")  # 28
        e = Patient("Tache", "Anastasia", 2920302243823, "unknown")  # 28
        f = Patient("Noveanu", "Marcus", 6050302243823, "hypertension")  # 15
        g = Patient("Berchis", "Anamaria", 1900403243823, "seizure")  # 30
        h = Patient("Pop", "Luca", 5010302243823, "flu")
        depo1.addPatient(b)
        depo1.addPatient(c)
        depo1.addPatient(d)
        depo2 = Department(27, "Orthopedics", 15, [e,f,g])
        depo3 = Department(19, "Emergencies", 25, [h])
        repo = departmentRepository([])
        self.assertEqual(repo.get(), [])
        repo.addDepartment(depo1)
        self.assertEqual(repo.get(), [depo1])
        repo.addDepartment(depo2)
        self.assertEqual(repo.get(), [depo1, depo2])
        repo.addDepartment(depo3)
        self.assertEqual(repo.get(), [depo1, depo2, depo3])

    def testAddAndDeletePatientToDepartment(self):
        depo1 = Department(2, "Cardiology", 34, [])
        b = Patient("Berchis", "Iulia", 6030302243823, "flu")  # 17
        c = Patient("Mezei", "Eric", 2980302243823, "stroke")  # 22
        d = Patient("Orghici", "Remus", 1920302543823, "stroke")  # 28
        e = Patient("Tache", "Anastasia", 2920302243823, "unknown")  # 28
        f = Patient("Noveanu", "Marcus", 6050302243823, "hypertension")  # 15
        g = Patient("Berchis", "Anamaria", 1900403243823, "seizure")  # 30
        h = Patient("Pop", "Luca", 5010302243823, "flu")
        depo1.addPatient(b)
        depo2 = Department(27, "Orthopedics", 15, [e, f, g])
        depo3 = Department(19, "Emergencies", 25, [h])
        repo = departmentRepository()
        repo.addDepartment(depo1)
        repo.addDepartment(depo2)
        repo.addDepartment(depo3)
        i = Patient("Podolac", "Eduard", 5010704243823, "diabetes")
        repo.addPatientToDepartment(i, 2)
        self.assertEqual(depo3.get(), [h,i])
        repo.addPatientToDepartment(c, 1)
        self.assertEqual(depo2.get(), [e,f,g,c])
        repo.addPatientToDepartment(d, 0)
        self.assertEqual(depo1.get(), [b,d])
        #now the delete function
        #depo1 = [b,d]
        #depo2 = [e,f,g,c]
        #depo3 = [h,i]
        #repo = [depo1, depo2, depo3]
        with self.assertRaises(IndexError):
            repo.deletePatientFromDepartment(3,0)
        with self.assertRaises(IndexError):
            repo.deletePatientFromDepartment(1,4)
        with self.assertRaises(IndexError):
            repo.deletePatientFromDepartment(5,7)
        repo.deletePatientFromDepartment(1,3)
        self.assertEqual(repo.getDepartmentOfIndex(1).get(), [e,f,g])
        repo.deletePatientFromDepartment(0,0)
        self.assertEqual(repo.getDepartmentOfIndex(0).get(), [d])

    def testUpdatePatientFromDepartment(self):
        b = Patient("Berchis", "Iulia", 6030302243823, "flu")  # 17
        c = Patient("Mezei", "Eric", 2980302243823, "stroke")  # 22
        d = Patient("Orghici", "Remus", 1920302543823, "stroke")  # 28
        e = Patient("Tache", "Anastasia", 2920302243823, "unknown")  # 28
        f = Patient("Noveanu", "Marcus", 6050302243823, "hypertension")  # 15
        g = Patient("Berchis", "Anamaria", 1900403243823, "seizure")  # 30
        h = Patient("Pop", "Luca", 5010302243823, "flu")
        i = Patient("Podolac", "Eduard", 5010704243823, "diabetes")
        depo1 = Department(2, "Cardiology", 34, [b,c,d])
        depo2 = Department(27, "Orthopedics", 15, [e, f, g])
        depo3 = Department(19, "Emergencies", 25, [h,i])
        repo = departmentRepository([])
        repo.addDepartment(depo1)
        repo.addDepartment(depo2)
        repo.addDepartment(depo3)
        with self.assertRaises(IndexError):
            repo.updatePatientFromDepartment(-2,0, "Suciu", "Dragos", 2780902243823, "unknown")
        with self.assertRaises(IndexError):
            repo.updatePatientFromDepartment(2,7, "Suciu", "Dragos", 2780902243823, "unknown")
        with self.assertRaises(IndexError):
            repo.updatePatientFromDepartment(4,0, "Suciu", "Dragos", 2780902243823, "unknown")
        with self.assertRaises(ValueError):
            repo.updatePatientFromDepartment(2,0, "Suciu", "Dragos", 278090223, "unknown")
        repo.updatePatientFromDepartment(0,0, "Baciu", "Tudor", 5040705243823, "unknown")
        self.assertEqual(str(repo.getDepartmentOfIndex(0).getPatientAtIndex(0)), str(Patient("Baciu", "Tudor", 5040705243823, "unknown")))

    def testDeleteDepartmentOfIndex(self):
        b = Patient("Berchis", "Iulia", 6030302243823, "flu")  # 17
        c = Patient("Mezei", "Eric", 2980302243823, "stroke")  # 22
        d = Patient("Orghici", "Remus", 1920302543823, "stroke")  # 28
        e = Patient("Tache", "Anastasia", 2920302243823, "unknown")  # 28
        f = Patient("Noveanu", "Marcus", 6050302243823, "hypertension")  # 15
        g = Patient("Berchis", "Anamaria", 1900403243823, "seizure")  # 30
        h = Patient("Pop", "Luca", 5010302243823, "flu")
        i = Patient("Podolac", "Eduard", 5010704243823, "diabetes")
        depo1 = Department(2, "Cardiology", 34, [b, c, d])
        depo2 = Department(27, "Orthopedics", 15, [e, f, g])
        depo3 = Department(19, "Emergencies", 25, [h, i])
        repo = departmentRepository([])
        repo.addDepartment(depo1)
        repo.addDepartment(depo2)
        repo.addDepartment(depo3)
        with self.assertRaises(IndexError):
            repo.deleteDepartmentOfIndex(-1)

    def testGetDepartmentOfIndex(self):
        depo1 = Department(2, "Cardiology", 34, [])
        depo2 = Department(27, "Orthopedics", 15, [])
        depo3 = Department(19, "Emergencies", 25, [])
        repo = departmentRepository([])
        repo.addDepartment(depo1)
        repo.addDepartment(depo2)
        repo.addDepartment(depo3)
        with self.assertRaises(IndexError):
            repo.getDepartmentOfIndex(-2)
        with self.assertRaises(IndexError):
            repo.getDepartmentOfIndex(4)
        self.assertEqual(str(repo.getDepartmentOfIndex(0)), str(depo1))
        self.assertEqual(str(repo.getDepartmentOfIndex(1)), str(depo2))
        self.assertEqual(str(repo.getDepartmentOfIndex(2)), str(depo3))

    def testUpdateDepartmentAtIndex(self):
        depo1 = Department(2, "Cardiology", 34, [])
        depo2 = Department(27, "Orthopedics", 15, [])
        depo3 = Department(19, "Emergencies", 25, [])
        repo = departmentRepository([])
        repo.addDepartment(depo1)
        repo.addDepartment(depo2)
        repo.addDepartment(depo3)
        with self.assertRaises(IndexError):
            repo.updateDepartmentAtIndex(-1, "Pneuonomology", 1, 21)
        with self.assertRaises(IndexError):
            repo.updateDepartmentAtIndex(4, "Pneuonomology", 2, 21)
        repo.updateDepartmentAtIndex(0, "Pneuonomology", 2, 21 )
        self.assertEqual(repo.getDepartmentOfIndex(0), Department(2,"Pneuonomology",21, [] ))
        repo.updateDepartmentAtIndex(1, "Pharmaceutical", 6, 35)
        self.assertEqual(repo.getDepartmentOfIndex(1), Department(6, "Pharmaceutical", 35, []))

    def testSortPatientsByCNP(self):
        b = Patient("Berchis", "Iulia", 6030302243823, "flu")  # 17
        c = Patient("Mezei", "Eric", 2980302243823, "stroke")  # 22
        d = Patient("Orghici", "Remus", 1920302543823, "stroke")  # 28
        e = Patient("Tache", "Anastasia", 2920302243823, "unknown")  # 28
        f = Patient("Noveanu", "Marcus", 6050302243823, "hypertension")  # 15
        g = Patient("Berchis", "Anamaria", 1900403243823, "seizure")  # 30
        h = Patient("Pop", "Luca", 5010302243823, "flu")
        i = Patient("Podolac", "Eduard", 5010704243823, "diabetes")
        depo1 = Department(2, "Cardiology", 34, [b, c, d])
        depo2 = Department(27, "Orthopedics", 15, [e, f, g])
        depo3 = Department(19, "Emergencies", 25, [h, i])
        repo = departmentRepository([])
        repo.addDepartment(depo1)
        repo.addDepartment(depo2)
        repo.addDepartment(depo3)
        with self.assertRaises(IndexError):
            repo.sortPatientsFromDepartmentByCNP(-1)
        with self.assertRaises(IndexError):
            repo.sortPatientsFromDepartmentByCNP(3)
        repo.sortPatientsFromDepartmentByCNP(0)
        self.assertEqual(repo.getDepartmentOfIndex(0).get(), [d,c,b])
        repo.sortPatientsFromDepartmentByCNP(1)
        self.assertEqual(repo.getDepartmentOfIndex(1).get(), [g,e,f])
        repo.sortPatientsFromDepartmentByCNP(2)
        self.assertEqual(repo.getDepartmentOfIndex(2).get(), [h, i])

    def TestMySortByNumberOfPatientsAlphabeticaly(self):
        b = Patient("Berchis", "Iulia", 6030302243823, "flu")  # 17
        c = Patient("Mezei", "Eric", 2980302243823, "stroke")  # 22
        d = Patient("Orghici", "Remus", 1920302543823, "stroke")  # 28
        e = Patient("Tache", "Anastasia", 2920302243823, "unknown")  # 28
        f = Patient("Noveanu", "Marcus", 6050302243823, "hypertension")  # 15
        g = Patient("Berchis", "Anamaria", 1900403243823, "seizure")  # 30
        h = Patient("Pop", "Luca", 5010302243823, "flu")
        i = Patient("Podolac", "Eduard", 5010704243823, "diabetes")
        depo1 = Department(2, "Cardiology", 34, [b, c, d])
        depo2 = Department(27, "Orthopedics", 15, [e, f, g])
        depo3 = Department(19, "Emergencies", 25, [h, i])
        repo = departmentRepository([])
        repo.addDepartment(depo1)
        repo.addDepartment(depo2)
        repo.addDepartment(depo3)
        expected_depo1 = Department(2, "Cardiology", 34, [b, c, d])
        expected_depo2 = Department(27, "Orthopedics", 15, [g,f,e])
        expected_depo3 = Department(19, "Emergencies", 25, [i,h])
        repo.mySortByNumberOfPatientsAlphabeticaly()
        self.assertEqual(repo.get(), [expected_depo1, expected_depo2, expected_depo3])

    def testSortAndFilterByNumberOfPatientsOverAge(self):
        b = Patient("Berchis", "Iulia", 6030302243823, "flu")  # 17
        c = Patient("Mezei", "Eric", 2980302243823, "stroke")  # 22
        d = Patient("Orghici", "Remus", 1920302543823, "stroke")  # 28
        e = Patient("Tache", "Anastasia", 2920302243823, "unknown")  # 28
        f = Patient("Noveanu", "Marcus", 6050302243823, "hypertension")  # 15
        g = Patient("Berchis", "Anamaria", 1900403243823, "seizure")  # 30
        h = Patient("Pop", "Luca", 5010302243823, "flu")  # 19
        i = Patient("Podolac", "Eduard", 5010704243823, "diabetes")  # 19
        depo1 = Department(2, "Cardiology", 34, [b, c, d])  # 17 #22 #28
        depo2 = Department(27, "Orthopedics", 15, [e, f, g])  # 28 #15 #30
        depo3 = Department(19, "Emergencies", 25, [h, i])  #19 #19
        repo = departmentRepository([])
        repo.addDepartment(depo1)
        repo.addDepartment(depo2)
        repo.addDepartment(depo3)
        repo.sortAndFilterByNumberOfPatientsOverAge(30)
        self.assertEqual(repo.get(), [depo1, depo2, depo3])
        repo.sortAndFilterByNumberOfPatientsOverAge(18)
        self.assertEqual(repo.get(), [depo1, depo2, depo3])
        repo.sortAndFilterByNumberOfPatientsOverAge(16)
        self.assertEqual(repo.get(), [depo2, depo3, depo1])
        repo.sortAndFilterByNumberOfPatientsOverAge(27)
        self.assertEqual(repo.get(), [depo3, depo1, depo2])
        repo.sortAndFilterByNumberOfPatientsOverAge(14)
        self.assertEqual(repo.get(), [depo3, depo1, depo2])

    def testGetDepartmentsWithPatientsUnder(self):
        b = Patient("Berchis", "Iulia", 6030302243823, "flu")  # 17
        c = Patient("Mezei", "Eric", 2980302243823, "stroke")  # 22
        d = Patient("Orghici", "Remus", 1920302543823, "stroke")  # 28
        e = Patient("Tache", "Anastasia", 2920302243823, "unknown")  # 28
        f = Patient("Noveanu", "Marcus", 6050302243823, "hypertension")  # 15
        g = Patient("Berchis", "Anamaria", 1900403243823, "seizure")  # 30
        h = Patient("Pop", "Luca", 5010302243823, "flu")  # 19
        i = Patient("Podolac", "Eduard", 5010704243823, "diabetes")  # 19
        depo1 = Department(2, "Cardiology", 34, [b, c, d])  # 17 #22 #28
        depo2 = Department(27, "Orthopedics", 15, [e, f, g])  # 28 #15 #30
        depo3 = Department(19, "Emergencies", 25, [h, i])  # 19 #19
        repo = departmentRepository([])
        repo.addDepartment(depo1)
        repo.addDepartment(depo2)
        repo.addDepartment(depo3)
        self.assertEqual(repo.getDepartmentsWithPatientsUnder(10),[])
        self.assertEqual(repo.getDepartmentsWithPatientsUnder(15), [])
        self.assertEqual(repo.getDepartmentsWithPatientsUnder(20), [depo1, depo2, depo3])
        self.assertEqual(repo.getDepartmentsWithPatientsUnder(17), [depo2])
        self.assertEqual(repo.getDepartmentsWithPatientsUnder(18), [depo1, depo2])

    def testGetDepartmentsWithPatientsWithFirstName(self):
        a = Patient("Pop", "Amalia", 5040903243824, "unknown") #16
        b = Patient("Berchis", "Iulia", 6030302243823, "flu")  # 17
        c = Patient("Mezei", "Eric", 2980302243823, "stroke")  # 22
        d = Patient("Orghici", "Remus", 1920302543823, "stroke")  # 28
        e = Patient("Tache", "Anastasia", 2920302243823, "unknown")  # 28
        f = Patient("Noveanu", "Marcus", 6050302243823, "hypertension")  # 15
        g = Patient("Berchis", "Anamaria", 1900403243823, "seizure")  # 30
        h = Patient("Pop", "Luca", 5010302243823, "flu")  # 19
        i = Patient("Podolac", "Eduard", 5010704243823, "diabetes")  # 19
        depo1 = Department(2, "Cardiology", 34, [a, b, c, d])  #16  #17 #22 #28
        depo2 = Department(27, "Orthopedics", 15, [e, f, g])  # 28 #15 #30
        depo3 = Department(19, "Emergencies", 25, [h, i])  # 19 #19
        repo = departmentRepository([])
        repo.addDepartment(depo1)
        repo.addDepartment(depo2)
        repo.addDepartment(depo3)
        self.assertEqual(repo.getDepartmentsWithPatientsWithFirstName("Marquez"), [])
        self.assertEqual(repo.getDepartmentsWithPatientsWithFirstName("Mezei"), [depo1])
        self.assertEqual(repo.getDepartmentsWithPatientsWithFirstName("Pop"), [depo1, depo3])
        self.assertEqual(repo.getDepartmentsWithPatientsWithFirstName("Berchis"), [depo1, depo2])
        self.assertEqual(repo.getDepartmentsWithPatientsWithFirstName("Podolac"), [depo3])

    def testMySortByNumberOfPatients(self):
        a = Patient("Pop", "Amalia", 5040903243824, "unknown")  # 16
        b = Patient("Berchis", "Iulia", 6030302243823, "flu")  # 17
        c = Patient("Mezei", "Eric", 2980302243823, "stroke")  # 22
        d = Patient("Orghici", "Remus", 1920302543823, "stroke")  # 28
        e = Patient("Tache", "Anastasia", 2920302243823, "unknown")  # 28
        f = Patient("Noveanu", "Marcus", 6050302243823, "hypertension")  # 15
        g = Patient("Berchis", "Anamaria", 1900403243823, "seizure")  # 30
        h = Patient("Pop", "Luca", 5010302243823, "flu")  # 19
        i = Patient("Podolac", "Eduard", 5010704243823, "diabetes")  # 19
        depo1 = Department(2, "Cardiology", 34, [a, b, c, d])  # 16  #17 #22 #28
        depo2 = Department(27, "Orthopedics", 15, [e, f, g])  # 28 #15 #30
        depo3 = Department(19, "Emergencies", 25, [h, i])  # 19 #19
        repo = departmentRepository([])
        repo.addDepartment(depo1)
        repo.addDepartment(depo2)
        repo.addDepartment(depo3)
        repo.mySortByNumberOfPatientsAlphabeticaly()
        self.assertEqual(repo.get(), [depo3, depo2, depo1])


if __name__ == "__main__":
    unittest.main()