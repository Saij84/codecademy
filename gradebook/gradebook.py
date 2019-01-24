last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]

subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]


def newGradeSubjects(subject, grade):
  if subject not in subjects and (len(subjects)==len(grades)):
    subjects.append(subject)
    grades.append(grade)
  else:
    print("please make sure that the subject is not already in the subjects and\
     that grade have the same count as subjects")
    pass

gradebook = zip(subjects, grades)
full_gradebook  = last_semester_gradebook + list(gradebook)


newGradeSubjects("computer science", 100)
newGradeSubjects("Visual arts", 93)

print(full_gradebook)