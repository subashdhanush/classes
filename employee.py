class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_bonus(self, bonus_percentage):
        bonus = self.salary * (bonus_percentage / 100)
        total_salary = self.salary + bonus
        print(f"💼 {self.name}'s total salary after {bonus_percentage}% bonus: ₹{total_salary}")


# Creating employees
emp1 = Employee("David", 50000)
emp2 = Employee("Emma", 60000)

# Calculating salary with bonus
emp1.calculate_bonus(10)  # 10% bonus
emp2.calculate_bonus(15)  # 15% bonus
