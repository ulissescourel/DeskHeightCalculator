def desk_chair_height(height):
    feet, inches = height.split('\'')
    total_inches = int(feet) * 12 + int(inches[:-1])
    desk_height = total_inches * 0.56  # 56% of total height
    chair_height = total_inches * 0.29  # 29% of total height
    return {'desk_height': desk_height, 'chair_height': chair_height}

height = "5'10\""  # 5 feet 10 inches
suggested_heights = desk_chair_height(height)
print(suggested_heights)