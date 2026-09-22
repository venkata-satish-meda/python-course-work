def show_student(**details):
    for key, value in details.items():
        print(key, ":", value)

show_student(name="Satish", course="Python", age=21)
