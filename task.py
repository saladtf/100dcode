student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score

print(max_score)
#max = sorted(student_scores)[-1]
#print(max)




#goal is to choose the largest number in the student score
#print(range(1, 10))
#print(max(student_scores))