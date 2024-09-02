"""Create a tuple of student names and their corresponding scores. Write a function to find
the student with the highest score."""


def student(score):
    x = score[0][1]
    y = score[0]
    for i in score:
        if i[1] > x:
            x = i[1]
            y = i
    return y
s = ('Levon', 15), ('Haikush', 14), ('Narek', 11)
print(student(s))

