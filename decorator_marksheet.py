def decorate(function):
    def wrapper(students_data):
        # write your code below this comment
        for s in students_data:
            avg_score = round((s['scores']['math'] + s['scores']['science'] + s['scores']['english'])/3, 2)
            print("{}: {}".format(s['name'], avg_score))
        # write your code above this comment
        return function(students_data)
    return wrapper


@decorate
def return_mean_grace(students):
    # write your code below this comment
    grace_marks = list( map( lambda s: s['grace_marks'], students ) )
    return round(sum(grace_marks)/len(grace_marks), 2)


students = [
    {"name": "Alice", "scores": {"math": 88, "science": 90, "english": 85}, "grace_marks": 10},
    {"name": "Bob", "scores": {"math": 72, "science": 68, "english": 74}, "grace_marks": 11},
    {"name": "Charlie", "scores": {"math": 95, "science": 92, "english": 91}, "grace_marks": 9},
    {"name": "David", "scores": {"math": 60, "science": 75, "english": 70}, "grace_marks": 10},
    {"name": "Eve", "scores": {"math": 82, "science": 78, "english": 88}, "grace_marks": 11}
]

print(return_mean_grace(students))