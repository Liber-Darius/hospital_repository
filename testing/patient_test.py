from modules.patient import Patient
import unittest

class Test(unittest.TestCase):

    def testGettersAndSetters(self):
        b = Patient("Luca", "Pop", 5020302243823, "flu")
        self.assertEqual(b.getFirstName(), "Luca")
        self.assertEqual(b.getLastName(), "Pop")
        self.assertEqual(b.getCNP(), 5020302243823)
        self.assertEqual(b.getDisease(), "flu")
        self.assertEqual(b.getAge(), 18)
        self.assertEqual(str(b), "Patient: Luca Pop with the cnp: 5020302243823 suffering from flu")
        b.setFirstName("Istvan")
        self.assertEqual(b.getFirstName(), "Istvan")
        b.setLastName("Szasz")
        self.assertEqual(b.getLastName(), "Szasz")
        b.setDisease("insomnia")
        self.assertEqual(b.getDisease(), "insomnia")
        with self.assertRaises(ValueError):
            b.setCNP(67832)
        c = Patient()
        self.assertEqual(c.getFirstName(), " ")
        self.assertEqual(c.getLastName(), " ")
        self.assertEqual(c.getCNP(), 1010101000000)
        self.assertEqual(c.getAge(),119)
        self.assertEqual(c.getDisease(), " ")
        with self.assertRaises(ValueError):
            d = Patient("Sziegel", "Otto", 678923, "alzheimer")

if __name__ == "__main__":
    unittest.main()