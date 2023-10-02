bs = int(input("Enter your Salary: "))
yos = int(input("Enter Years of Service: "))


if yos == 5:
    salary_bonus = bs * 0.05
    final_salary = bs + salary_bonus
    run_time = 1 
elif yos == 10:
    salary_bonus = bs * 0.10
    final_salary = bs + salary_bonus
    run_time = 2
elif yos == 15:
    salary_bonus = bs * 0.15
    final_salary = bs + salary_bonus
    run_time = 3
elif yos == 20:
    salary_bonus = bs * 0.20
    final_salary = bs + salary_bonus
    run_time = 4
else:
    print("Invalid")
    run_time = 5

# Print the results
print("Your Salary Bonus:", salary_bonus)
print("Total Salary:", final_salary)
print(f"Runtime: {run_time}(n)")
