def get_suggested_heights(height_feet, height_inches):
    height_inches += height_feet * 12
    total_height = height_inches / 12
    desk_height = total_height * 0.56
    chair_height = total_height * 0.29
    return {'desk': desk_height, 
        'chair': chair_height}

# Example usage:
height = get_suggested_heights(5, 6)
print("Suggested desk height: ", height['desk'])
print("Suggested chair height: ", height['chair'])