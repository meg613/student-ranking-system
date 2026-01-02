from ranking_system import StudentRankingSystem

system=StudentRankingSystem()

system.add_student("Megha",98)
system.add_student("Riya",95)
system.add_student("Hima",88)
system.add_student("Tina",90)

ranked=system.rank_students()

print("Student Rankings:")
for i,student in enumerate(ranked,start=1):
    print(f"Rank {i}: {student.name} - {student.marks}")

print("\nTop 2 students:")
for s in system.top_k_students(2):
    print(s.name, s.marks)