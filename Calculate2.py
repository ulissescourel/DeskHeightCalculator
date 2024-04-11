from math import ceil

def desk_chair_height(height, decimal_pref):
    feet, inches = height.split('\'')
    total_inches = int(feet) * 12 + int(inches)
    multiplier = 10**(decimal_pref)  # convert decimal_pref to multiplier
    desk_height = round(total_inches * 0.56 * multiplier) / multiplier  # 56% of total height, rounded to nearest tenth
    chair_height = round(total_inches * 0.29 * multiplier) / multiplier  # 29% of total height, rounded to nearest tenth
    return {'desk_height': desk_height, 'chair_height': chair_height}

height = "5'10\""  # 5 feet 10 inches
desk_chair_height(height, 1)  # 1 decimal places
desk_chair_height(height, 2)  # 2 decimal places
desk_chair_height(height, 0)  # no decimals