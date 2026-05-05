# Function

# can pass parameter


def check_even_number(n, n2):
    if n % 2 == 0:
        return "even"
    else:
        return "odd"


print(check_even_number(42, 44))


def user_info(fname, lname):
    return f"my name is {fname} {lname}"


print(user_info("hari", "sharma"))
# user_info("sharma","hari")


# keyword argument

'''
def calculate_salary(base_salary, bonus, deductions, tax_percent):
    total_salary = base_salary + bonus
    tax = (total_salary * tax_percent) / 100
    final_salary = total_salary - tax - deductions

    return final_salary


print(calculate_salary(5000, 1000, 0))
print(calculate_salary(base_salary=5000, deductions=1000, bonus=0, tax_percentage=10)
      )

pie = 1.2
'''
'''
# default argument

def calc_area(pie,r):
    return pie*r*r
print(calc_area(7))
print(calc_area(7,5.18))


'''
# personal argument multiple data should be pass

def add_number(*data):
    total = 0
    for i in data:
        total = total + i
        print(f'{data}--------> total------> {total}')
        return total

print(add_number(1,2,3,4,5))
print(add_number(1,2))
print(add_number())
print(add_number(1,2,3,4,5,6,7,7,7,7))