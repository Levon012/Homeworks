"""10.Salaries
Given the salaries of three employees working at a department, find the
amount of money by which the salary of the highest-paid employee differs
from the salary of the lowest-paid employee. The input consists of three
positive integers - the salaries of the employees. Output a single number,
the difference between the top and the bottom salaries
Sample Input Sample Output
100 500 1000        900
500 100 1000        900
36 11 20            25
20 20 20            0"""

salaries1 = int(input('from'))
salaries2 = int(input('from'))
salaries3 = int(input('from'))

if 0 < salaries1 <= salaries2 <= salaries3:
    print(salaries3 - salaries1)
elif 0 < salaries3 <= salaries2 <= salaries1:
    print(salaries1 - salaries3)
elif 0 < salaries2 <= salaries1 <= salaries3:
    print(salaries3 - salaries2)
elif 0 < salaries2 <= salaries3 <= salaries1:
    print(salaries1 - salaries2)
elif 0 < salaries1 <= salaries3 <= salaries2:
    print(salaries2 - salaries1)
elif 0 < salaries3 <= salaries1 <= salaries2:
    print(salaries2 - salaries3)
else:
    print(0)

    