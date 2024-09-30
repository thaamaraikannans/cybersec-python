# def print_func(data):
#     print(data)


# def main_func():
#     a = 100
#     b = 200
#     if a > b:
#         print_func("A is greater")
#     else:
#         print_func("B is greater")

# main_func()
# print_func("Kannan")

students_grades = [
    {"name": "Alice", "marks": [{"social": 80, "maths": 60, "science": 20, "tamil": 99, "english": 66}]},
    {"name": "Bob", "marks": [{"social": 70, "maths": 65, "science": 75, "tamil": 85, "english": 78}]},
    {"name": "Charlie", "marks": [{"social": 90, "maths": 85, "science": 95, "tamil": 88, "english": 92}]},
    {"name": "Diana", "marks": [{"social": 82, "maths": 79, "science": 85, "tamil": 90, "english": 87}]},
    {"name": "Eve", "marks": [{"social": 88, "maths": 90, "science": 92, "tamil": 94, "english": 89}]},
    {"name": "Frank", "marks": [{"social": 75, "maths": 80, "science": 23, "tamil": 60, "english": 65}]},
    {"name": "Grace", "marks": [{"social": 95, "maths": 90, "science": 85, "tamil": 80, "english": 88}]},
    {"name": "Hank", "marks": [{"social": 60, "maths": 70, "science": 65, "tamil": 75, "english": 70}]},
    {"name": "Ivy", "marks": [{"social": 85, "maths": 15, "science": 80, "tamil": 85, "english": 82}]},
    {"name": "Jack", "marks": [{"social": 78, "maths": 85, "science": 88, "tamil": 90, "english": 84}]}
]

def calc_total(stu_name ,marks):
    # the marks should be like [80, 60, 20]
    total = sum(marks)
    
    return total



def main_func():
    for student in students_grades:
        name = student["name"]
        marks = student["marks"][0]
        # print(marks)
        subject = ["social", "maths", "science", "tamil", "english"]
        data = []
        for sub in range(len(marks)):
            single_mark = marks[subject[sub]]
            data.append(single_mark)
        # print("the mark of the student",data)
        total = calc_total(marks=data, stu_name=name)
        print(f"The total marks of the student {name} :", total)



main_func()