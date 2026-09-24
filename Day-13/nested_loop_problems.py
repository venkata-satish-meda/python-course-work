# Nested loop problem: find pairs that add to a target

prices = [120, 250, 80, 170, 300]
target = 370

for i in range(len(prices)):
    for j in range(i + 1, len(prices)):
        if prices[i] + prices[j] == target:
            print("Matching prices:", prices[i], prices[j])

# Seat numbering
for row in range(1, 4):
    for seat in range(1, 5):
        print(f"R{row}S{seat}", end=" ")
    print()
