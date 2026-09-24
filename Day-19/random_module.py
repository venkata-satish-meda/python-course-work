import random

otp = random.randint(100000, 999999)
print("Demo OTP:", otp)

items = ["Keyboard", "Mouse", "Headset", "Webcam"]
print("Suggested item:", random.choice(items))

numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print("Shuffled:", numbers)
