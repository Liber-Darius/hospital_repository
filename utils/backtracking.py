from modules.patient import Patient
from utils.sorting import mySearch
from utils.sorting import mySort
from utils.sorting import quickSort
from modules.department import Department
from infrastructure.repository import departmentRepository

def combinations(lst, k):
    pool = tuple(lst)
    n = len(pool)
    if k > n:
        return
    indices = list(range(k))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(k)):
            if indices[i] != i + n - k:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, k):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)

def comb(lst, k, cond):
    return [i for i in combinations(lst, k) if cond(i)]
def k_with_same_dep_and_disease(self,k):
        thisListHere = []
        for dept in self.__contents:
            patients = [(dept.get_id(), i) for i in dept.get()]
        thisListHere += patients
        def same_disease(x):
            disease = x[0].get_disease()
            for i in x[1:]:
                if i.get_disease() != disease:
                    return False
            return True
        return comb(thisListHere, k, same_disease)

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
repo.