from modules.department import Department
import unittest
from modules.patient import Patient
class Test(unittest.TestCase):

    def testAddAndGet(self):
        depo_1 = Department(2, "Cardiology", 34, [])
        self.assertEqual(depo_1.get(), [])
        b = Patient("Berchis", "Iulia", 6030302243823, "flu")
        depo_1.addPatient(b)
        self.assertEqual(depo_1.get(), [b])
        c = Patient("Mezei", "Eric", 2980302243823, "stroke")
        depo_1.addPatient(c)
        self.assertEqual(depo_1.get(), [b,c])

    def testDeletePatientsByIndex(self):
        depo = Department(2, "Cardiology", 34, [])
        b = Patient("Berchis", "Iulia", 6030302243823, "flu")
        c = Patient("Mezei", "Eric", 2980302243823, "stroke")
        d = Patient("Orghici", "Remus", 1920302543823, "stroke")
        depo.addPatient(b)
        depo.addPatient(c)
        depo.addPatient(d)
        with self.assertRaises(IndexError):
            depo.deletePatientByIndex(3)
        with self.assertRaises(IndexError):
            depo.deletePatientByIndex(-1)
        depo.deletePatientByIndex(0)
        self.assertEqual(depo.get(), [c,d])
        depo.deletePatientByIndex(1)
        self.assertEqual(depo.get(), [c])
        depo.deletePatientByIndex(0)
        self.assertEqual(depo.get(), [])

    def testDeletePatientsByCNP(self):
        depo = Department(2, "Cardiology", 34, [])
        b = Patient("Berchis", "Iulia", 6030302243823, "flu")
        c = Patient("Mezei", "Eric", 2980302243823, "stroke")
        d = Patient("Orghici", "Remus", 1920302543823, "stroke")
        depo.addPatient(b)
        depo.addPatient(c)
        depo.addPatient(d)
        depo.deletePatientByCNP(34343)
        self.assertEqual(depo.get(), [b, c, d])
        depo.deletePatientByCNP(5434)
        self.assertEqual(depo.get(), [b, c, d])
        depo.deletePatientByCNP(6030302243823)
        self.assertEqual(depo.get(), [c,d])
        depo.deletePatientByCNP(1920302543823)
        self.assertEqual(depo.get(), [c])
        depo.deletePatientByCNP(2980302243823)
        self.assertEqual(depo.get(), [])

    def testUpdateDepartment(self):
        depo = Department(2, "Cardiology", 34, [])
        depo.updateDepartment("Orthopedics", 12, 67)
        self.assertEqual(depo.getID(), 12)
        self.assertEqual(depo.getBeds(), 67)
        self.assertEqual(depo.getName(), "Orthopedics")

    def testUpdatePatientAtIndex(self):
        depo = Department(2, "Cardiology", 34, [])
        b = Patient("Berchis", "Iulia", 6030302243823, "flu")
        c = Patient("Mezei", "Eric", 2980302243823, "stroke")
        d = Patient("Orghici", "Remus", 1920302543823, "stroke")
        depo.addPatient(b)
        depo.addPatient(c)
        depo.addPatient(d)
        with self.assertRaises(ValueError):
            depo.updatePatientAtIndex(1, "Orgas", "David", 289, "cardiovascular problems" )
        with self.assertRaises(ValueError):
            depo.updatePatientAtIndex(1, "Orgas", "David", 6030302243823, "cardiovascular problems" )
        with self.assertRaises(IndexError):
            depo.updatePatientAtIndex(4, "Orgas", "David", 6030302243823, "cardiovascular problems" )
        depo.updatePatientAtIndex(1, "Orgas", "David", 6035402243823, "cardiovascular problems")
        e = Patient("Orgas", "David", 6035402243823, "cardiovascular problems")
        self.assertEqual(str(depo.getPatientAtIndex(1)), str(e))

    def testMySortByCNP(self):
        depo = Department(2, "Cardiology", 34, [])
        depo.mySortByCNP()
        self.assertTrue(depo.get() == [])
        b = Patient("Berchis", "Iulia", 6030302243823, "flu")
        c = Patient("Mezei", "Eric", 2980302243823, "stroke")
        d = Patient("Orghici", "Remus", 1920302543823, "stroke")
        depo.addPatient(b)
        depo.addPatient(c)
        depo.addPatient(d)
        depo.mySortByCNP()
        self.assertTrue(depo.get() == [d,c,b])
        e = Patient("Tache", "Anastasia", 2920302243823, "unknown")
        depo.addPatient(e)
        depo.mySortByCNP()
        self.assertTrue(depo.get() == [d,e,c,b] )

    def testSortByFirstAndLastName(self):
        depo = Department(2, "Cardiology", 34, [])
        depo.sortByFirstAndLastName()
        self.assertTrue(depo.get() == [])
        b = Patient("Berchis", "Iulia", 6030302243823, "flu")
        c = Patient("Mezei", "Eric", 2980302243823, "stroke")
        d = Patient("Orghici", "Remus", 1920302543823, "stroke")
        depo.addPatient(b)
        depo.addPatient(c)
        depo.addPatient(d)
        depo.sortByFirstAndLastName()
        self.assertTrue(depo.get() == [b,c,d])
        e = Patient("Tache", "Anastasia", 2920302243823, "unknown")
        depo.addPatient(e)
        depo.sortByFirstAndLastName()
        self.assertTrue(depo.get() == [b,c,d,e])
        f = Patient("Noveanu", "Marcus", 6050302243823, "hypertension")
        depo.addPatient(f)
        depo.sortByFirstAndLastName()
        self.assertTrue(depo.get() == [b, c, f, d, e])

    def testGetPatientsThatContainString(self):
        depo = Department(2, "Cardiology", 34, [])
        b = Patient("Berchis", "Iulia", 6030302243823, "flu")
        c = Patient("Mezei", "Eric", 2980302243823, "stroke")
        d = Patient("Orghici", "Remus", 1920302543823, "stroke")
        e = Patient("Tache", "Anastasia", 2920302243823, "unknown")
        f = Patient("Noveanu", "Marcus", 6050302243823, "hypertension")
        depo.addPatient(b)
        depo.addPatient(c)
        depo.addPatient(d)
        depo.addPatient(e)
        depo.addPatient(f)
        self.assertEqual(depo.getPatientsThatContainString("a"), [b,e,f])
        self.assertEqual(depo.getPatientsThatContainString("an"), [e,f])
        self.assertEqual(depo.getPatientsThatContainString("andrei"), [])

    def testNumberOfPatientsOlderThan(self):
        depo = Department(2, "Cardiology", 34, [])
        b = Patient("Berchis", "Iulia", 6030302243823, "flu") #17
        c = Patient("Mezei", "Eric", 2980302243823, "stroke") #22
        d = Patient("Orghici", "Remus", 1920302543823, "stroke") #28
        e = Patient("Tache", "Anastasia", 2920302243823, "unknown") #28
        f = Patient("Noveanu", "Marcus", 6050302243823, "hypertension") #15
        depo.addPatient(b)
        depo.addPatient(c)
        depo.addPatient(d)
        depo.addPatient(e)
        depo.addPatient(f)
        self.assertEqual(depo.numberOfPatientsOlderThan(10), 5)
        self.assertEqual(depo.numberOfPatientsOlderThan(15), 4)
        self.assertEqual(depo.numberOfPatientsOlderThan(18), 3)
        self.assertEqual(depo.numberOfPatientsOlderThan(25), 2)
        self.assertEqual(depo.numberOfPatientsOlderThan(30), 0)

    def testNumberOfPatientsYoungerThan(self):
        depo = Department(2, "Cardiology", 34, [])
        b = Patient("Berchis", "Iulia", 6030302243823, "flu") #17
        c = Patient("Mezei", "Eric", 2980302243823, "stroke") #22
        d = Patient("Orghici", "Remus", 1920302543823, "stroke") #28
        e = Patient("Tache", "Anastasia", 2920302243823, "unknown") #28
        f = Patient("Noveanu", "Marcus", 6050302243823, "hypertension") #15
        depo.addPatient(b)
        depo.addPatient(c)
        depo.addPatient(d)
        depo.addPatient(e)
        depo.addPatient(f)
        self.assertEqual(depo.numberOfPatientsYoungerThan(10), 0)
        self.assertEqual(depo.numberOfPatientsYoungerThan(15), 0)
        self.assertEqual(depo.numberOfPatientsYoungerThan(18), 2)
        self.assertEqual(depo.numberOfPatientsYoungerThan(25), 3)
        self.assertEqual(depo.numberOfPatientsYoungerThan(30), 5)

    def testNumberOfPatientsWithFirstName(self):
        depo = Department(2, "Cardiology", 34, [])
        b = Patient("Berchis", "Iulia", 6030302243823, "flu") #17
        c = Patient("Mezei", "Eric", 2980302243823, "stroke") #22
        d = Patient("Orghici", "Remus", 1920302543823, "stroke") #28
        e = Patient("Tache", "Anastasia", 2920302243823, "unknown") #28
        f = Patient("Noveanu", "Marcus", 6050302243823, "hypertension") #15
        g = Patient("Berchis", "Anamaria", 1900403243823, "seizure" ) #30
        depo.addPatient(b)
        depo.addPatient(c)
        depo.addPatient(d)
        depo.addPatient(e)
        depo.addPatient(f)
        depo.addPatient(g)
        self.assertEqual(depo.numberOfPatientsWithFirstName("Maiorescu"),0)
        self.assertEqual(depo.numberOfPatientsWithFirstName("Mezei"), 1)
        self.assertEqual(depo.numberOfPatientsWithFirstName("Tache"), 1)
        self.assertEqual(depo.numberOfPatientsWithFirstName("Berchis"), 2)
        self.assertEqual(depo.numberOfPatientsWithFirstName("Noveanu"), 1)

if __name__ == "__main__":
    unittest.main()

