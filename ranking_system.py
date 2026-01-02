from student import Student
import heapq

class StudentRankingSystem:
    def __init__(self):
        self.students=[]

    def add_student(self,name,marks):
        self.students.append(Student(name,marks))

    def rank_students(self):
        return sorted(self.students,key= lambda s:s.marks,reverse=True)

    def top_k_students(self,k):
        return heapq.nlargest(k,self.students,key=lambda s:s.marks)


