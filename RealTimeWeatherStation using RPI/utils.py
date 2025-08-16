def degrees_to_cardinal(degrees):
    cardinal_directions = [
        'N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE',
        'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW'
    ]
    index = int(((degrees + 11.25) % 360) // 22.5)
    return cardinal_directions[index]
