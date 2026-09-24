# Combined break, continue and pass practice

numbers = [12, -3, 45, 0, 18, 99]
positive_total = 0

for number in numbers:
    if number < 0:
        continue
    if number == 0:
        pass
    if number > 90:
        print("Large value found:", number)
        break
    positive_total += number

print("Total processed:", positive_total)
