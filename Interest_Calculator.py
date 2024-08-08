principle = 0; rate = 0; time = 0; n = 0

# Dictionary for compounding frequencies
compounding_frequencies = {
    1: ('Daily', 365),
    2: ('Weekly', 52),
    3: ('Monthly', 12),
    4: ('Quarterly', 4),
    5: ('Annually', 1)
}

print("V Compund Interest Calculator V")

# Validate Principal
while principle <= 0:
    while True:
        try:
            principle = float(input("> Enter the principal amount: "))
            break
        except ValueError:
            print("> Enter a valid number")
    if principle <= 0:
        print("> Principal must be greater than 0")

# Validate Interest Rate
while rate <= 0:
    while True:
        try:
            rate = float(input("> Enter the annual interest rate (as a percentage): "))
            break
        except ValueError:
            print("> Enter a valid number")
    if rate <= 0:
        print("> Interest rate must be greater than 0")

# Validate Time
while time <= 0:
    while True:
        try:
            time = float(input("> Enter time in years: "))
            break
        except ValueError:
            print("> Enter a valid number")
    if time <= 0:
        print("> Time cannot be 0 or negative")

# Display compounding frequency options
print("> How often is the interest compounded per year?")
for key, value in compounding_frequencies.items():
    print(f"{key}. {value[0]}")

# Validate and select Compounding Frequency
while n <= 0:
    while True:
        try:
            choice = int(input("> Enter the number corresponding to the compounding frequency: "))
            if choice in compounding_frequencies:
                n = compounding_frequencies[choice][1]
                break
            else:
                print("> Please enter a number between 1 and 5")
        except ValueError:
            print("> Enter a valid number")

# Calculate Compound Interest
total = principle * pow((1 + rate / (100 * n)), n * time)

print(f"Total amount after {time} years is: {total:.2f}")
