import random
import time

Operators = ["+", "-", "*"]
Min_op = 3
Max_op = 15
Total_problems = 10

def generate_problem():
    oper = random.choice(Operators)
    left = random.randint(Min_op, Max_op)
    right = random.randint(Min_op, Max_op)

    expr = str(left) + " " + oper + " " + str(right)
    ans = eval(expr)
    return expr,ans


input("Press enter to start the timer! ")
print("--------------------------------")
start_time = time.time()

for i in range(Total_problems):
    expr, ans = generate_problem()
    while True:
        user_ans = input("Problem #" + str(i+1) + ": " + expr + " = ")
        if user_ans == str(ans):
            break

end_time = time.time()
total_time = round(end_time - start_time, 2)

print("You finished in " , total_time , " Seconds.")
print("----------------------------------")
