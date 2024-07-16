salary_text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
import re
from typing import Callable

def generator_numbers(text):
    pattern = r'\d*\.\d{2}'
    for salary in re.findall(pattern,text):
        yield float(salary)

def sum_profit(text,func): #Hvorfor trenger vi typing Callable?
    income = 0
    for i in generator_numbers(text):
        income += i
    return income
 
total_income = sum_profit(salary_text, generator_numbers)
print(f"Загальний дохід: {total_income}")