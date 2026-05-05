def user_info(**info):
    print(info.get("salary"))


user_info(fname="luna", lname="maharjan", age="12", salary=12, num=123)

user_info(fname="luna", lname="maharjan", age="12", num=123)
user_info(
    fname="luna",
    lname="maharjan",
)


data = {"fname": "luna", "lname": "maharjan", "age": "12", "num": 123}
data.keys()
data.values()
print(data.items())

a, b = 1, 2
b, a = 1, 2


def print_info(**kwargs):
    for value, key in kwargs.items():
        print(f"{key}: {value}")


print_info(name="luna", age=25, city="kathmandu")

print("---------------hello---------------- ")


def print_tuple_info(*args):
    for index, i in enumerate(args):
        print(index + 1, i)


print_tuple_info("hello", "test", "greenfield", 1, 1, 1)


def student_info(*args, **kwargs):
    percentage = sum(args) / len(args)
    name = kwargs.get("name")
    grade = kwargs.get("grade")
    return f"Student name is {name} and grade is {grade} and obtain percentage={percentage}"

    # total = 0
    # for i in args:
    #     total+=i
    # print(total/len(args))


print(student_info(100, 82, 12, 93, 51, 71, 81, name="luna", age=10, grade=9))
print(student_info(100, 82, 93, 62, 64, 51, 71, 81, name="madan", age=10, grade=109))
print(student_info(100, 82, 93, 51, 71, 81, name="balen", age=10, grade=12))
print(student_info(10, 8, 9, 5, 7, 8, name="kp ba", age=10, grade=8))
