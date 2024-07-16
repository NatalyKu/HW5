salary_text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
import re
pattern = r'\d*\.\d{2}'
for salary in re.findall(pattern,salary_text):
    print(salary)