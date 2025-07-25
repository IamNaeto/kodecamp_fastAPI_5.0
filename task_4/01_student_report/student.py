class Student:
    def __init__(self, name, subjects_scores):
        self.name = name
        self.subjects_scores = subjects_scores  # dict of subject: score
        self.average = self.calculate_average()
        self.grade = self.calculate_grade()

    def calculate_average(self):
        total = sum(self.subjects_scores.values())
        return total / len(self.subjects_scores)

    def calculate_grade(self):
        avg = self.average
        if avg >= 90:
            return 'A'
        elif avg >= 80:
            return 'B'
        elif avg >= 70:
            return 'C'
        elif avg >= 60:
            return 'D'
        else:
            return 'F'

    def to_dict(self):
        return {
            'name': self.name,
            'subjects_scores': self.subjects_scores,
            'average': self.average,
            'grade': self.grade
        }

    @staticmethod
    def from_dict(data):
        return Student(data['name'], data['subjects_scores'])
