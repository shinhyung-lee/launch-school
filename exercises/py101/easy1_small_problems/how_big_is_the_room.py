def get_float_input(prompt):
    while True:
        user_input = input(prompt)
        try:
            number = float(user_input)
            if number > 0:
                return number
            else:
                print("Input must be a positive number.")
        except ValueError:
            print("Invalid input. Please enter a number")

length_in_meter = get_float_input("Enter the length of the room in meters: ")
width_in_meter = get_float_input("Enter the width of the room in meters: ")

area_in_meter = length_in_meter * width_in_meter
area_in_feet = area_in_meter * 10.7639

print(f'The room\'s area is {area_in_meter:.1f} square meters')
print(f'The room\'s area is {area_in_feet:.1f} square feet')