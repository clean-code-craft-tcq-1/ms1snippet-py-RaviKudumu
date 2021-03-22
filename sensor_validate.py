sensor_max_difference = { 'soc': 0.05, 'current' : 0.1 }

def sensor_working_properly(value, nextValue, maxDelta):
    if nextValue - value > maxDelta:
        return False
    return True

def is_sensor_reading_proper(values, sensor_name):
    values = remove_none_values(values)
    last_but_one_reading = len(values) - 1
    for i in range(last_but_one_reading):
        if(not sensor_working_properly(values[i], values[i + 1], sensor_max_difference[sensor_name])):
            return False
    return True

def remove_none_values(values):
    values = [i for i in values if i]
    return values
