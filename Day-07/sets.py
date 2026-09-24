# Sets remove duplicate values

cities = {"Hyderabad", "Chennai", "Hyderabad", "Pune"}
print(cities)

cities.add("Bengaluru")
cities.discard("Pune")
print("Updated cities:", cities)

# Unique skills collected from two teams
team_a = {"Python", "SQL", "Git"}
team_b = {"Python", "Django", "Docker"}
print("All skills:", team_a | team_b)
