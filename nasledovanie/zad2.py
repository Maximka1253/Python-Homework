class Bachelor:
    def __init__(self, firstName, lastName, group, averageMark):
        self.firstName = firstName
        self.lastName = lastName
        self.group = group
        self.averageMark = averageMark

    def getScholarship(self):
        if self.averageMark == 5:
            return 10000
        elif self.averageMark > 3:
            return 5000
        else:
            return 0

class Undergraduate(Bachelor):
    def __init__(self, firstName, lastName, group, averageMark, scientificWork="None"):
        super().__init__(firstName, lastName, group, averageMark)
        self.scientificWork = scientificWork

    def getScholarship(self):
        if self.averageMark == 5:
            return 15000
        elif self.averageMark > 3:
            return 7500
        else:
            return 0

students = [
    Bachelor("Иван", "Иванов", "Б-101", 5),
    Bachelor("Петр", "Петров", "Б-104", 2),
    Undergraduate("Ольга", "Сидорова", "М-202", 5),
    Undergraduate("Михаил", "Кузякин", "М-204", 4),
    Bachelor("Максим", "Бабадзанов", "Б-102", 4)
]

for s in students:
    role = "Магистрант" if isinstance(s, Undergraduate) else "Бакалавр"
    print(f"{role} {s.lastName}: {s.getScholarship()} р.")