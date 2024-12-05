student_score={
    "Alice": 85,
    "Babu": 78,
    "Charlie": 92,
    "David": 87,
    "Eve": 75

}

total_score=sum(student_score.values())
number_of_students=len(student_score)
average_score=total_score/number_of_students

print(f"The average score is {average_score:.2f}")