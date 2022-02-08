class Patient:
    def __init__(self, firstName = " ", lastName = " ", cnp = 1010101000000, disease = " "):
        self.__firstName = firstName
        self.__lastName = lastName
        self.__cnp = cnp
        if len(str(self.__cnp)) != 13:
            raise ValueError
        # for the persons born between 1900 and 1999 the cnp starts with 1 or 2
        # for the persons born after 2000 the cnp starts with 5 or 6
        # the second and the third letter of the cnp represents the year the person was born
        if (int(cnp/10**12)) == 1 or (int(cnp/10**12)) == 2:
            year_of_birth = 1900 + (int(cnp/10**10))%100
            self.__age = 2020 - year_of_birth
        else:
            year_of_birth = 2000 + (int(cnp/10**10))%100
            self.__age = 2020 - year_of_birth
        self.__disease = disease

    def getFirstName(self):
        return self.__firstName
    def getLastName(self):
        return self.__lastName
    def getCNP(self):
        return self.__cnp
    def getDisease(self):
        return self.__disease
    def getAge(self):
        return self.__age
    def setDisease(self, disease):
        self.__disease = disease
    def setCNP(self, cnp):
        if len(str(cnp)) != 13:
            raise ValueError
        else:
            self.__cnp = cnp
    def setAge(self, age):
        self.__age = age  
    def setLastName(self, lastName):
        self.__lastName = lastName
    def setFirstName(self, firstName):
        self.__firstName = firstName

    def __str__(self):
        return "Patient: " + self.__firstName + " " + self.__lastName + " with the cnp: " + str(self.__cnp) + " suffering from " + self.__disease
