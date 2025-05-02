'''
Tess Owens
April 28, 2025
Lab 11, class in Python (extra points)
'''
class Student:


    def __init__(self, name, cohort):
        self.name = name
        self.cohort = cohort
        self.grade={}
    
    def add_grade(self, subject, grade):
        self.grade[subject] = grade
        
# Implement method to calculate average grade


    def get_average_grade(self):
        if not self.grade:
            return 0
        total =sum(self.grade.values())
        return total / len(self.grade)
    
# CALLING THE CLASS
# Create instances and demonstrate usage of each method    
s1 = Student("Tess Owens", "Micro Credit")

s1.add_grade ("Art", 90.5)
s1.add_grade ("Science", 85.5)
s1.add_grade ("History", 88.0)

formatted_grades = ' ❤ '.join(f"{subj}: {gr}" for subj, gr in s1.grade.items())

print(f"Student info:  {s1.name} Class:  {s1.cohort}, Grades: {formatted_grades}, Average: {s1.get_average_grade():.2f}")


