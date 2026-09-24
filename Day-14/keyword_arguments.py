# Keyword arguments make calls easier to read

def send_message(name, message, priority):
    print(f"{priority.upper()} message for {name}: {message}")

send_message(
    name="Priya",
    message="Interview at 10 AM",
    priority="high"
)

def register_student(name, course, city):
    print(name, course, city)

register_student(city="Hyderabad", name="Kiran", course="Python")
