#Name:T.S.S.Roshini
#Program: Employee Records Processing
from functools import reduce
employees = [
    {"name": "Ravi", "department": "IT", "salary": 40000},
    {"name": "Sita", "department": "HR", "salary": 35000},
    {"name": "Amit", "department": "IT", "salary": 50000},
    {"name": "Priya", "department": "Finance", "salary": 45000},
    {"name": "Kiran", "department": "IT", "salary": 30000}
]
it_employees = list(
    filter(lambda e: e["department"] == "IT", employees)
)
hiked_employees = list(
    map(lambda e: {**e, "salary": e["salary"] * 1.10}, it_employees)
)
total_salary = reduce(
    lambda total, e: total + e["salary"],
    hiked_employees,
    0
)
print("Selected employees:")
print(it_employees)
print("\nEmployees after 10% hike:")
print(hiked_employees)
print("\nTotal salary expenditure:", total_salary)
#output
#Selected employees:
#[{'name': 'Ravi', 'department': 'IT', 'salary': 40000}, {'name': 'Amit', 'department': 'IT', 'salary': 50000}, {'name': 'Kiran', 'department': 'IT','salary': 30000}]
#
#Employees after 10% hike:
#[{'name': 'Ravi', 'department': 'IT', 'salary': 44000.0}, {'name': 'Amit', 'department': 'IT', 'salary': 55000.00000000001}, {'name': 'Kiran', 'department': 'IT', 'salary': 33000.0}]
#
#Total salary expenditure: 132000.0