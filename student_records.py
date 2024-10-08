def output_formatter(func):
    # complete the decorator
    def wrapper(*args, **kwargs):
        print (f"\n********** Lesser Mortals High School **********\n")
        result = func(*args, **kwargs)
        for s in result:
            print("Name: {}, Age: {}, Average Grade: {}".format(s['name'], s['age'], s['average_grade']))

    return wrapper

# decorate the function
@output_formatter
def process_students_data(students):
    # complete the function
    major_students = list( filter( lambda s: s['age']>=18, students ) )
    major_students = list( map( lambda s: {'name': s['name'], 'age': s['age'], 'average_grade': round(sum(s['grades'])/len(s['grades']), 2)}, major_students ))

    return major_students


students = [
    {"name": "Alice", "age": 17, "grades": [88, 90, 92]},
    {"name": "Bob", "age": 19, "grades": [76, 80, 78]},
    {"name": "Bobba", "age": 24, "grades": [76, 80, 78]},
    {"name": "Charlie", "age": 18, "grades": [90, 85, 85]},
    {"name": "Chitra", "age": 24, "grades": [69, 79, 75]}
]

process_students_data(students)