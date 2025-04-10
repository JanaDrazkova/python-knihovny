def time_to_sec(t_delta_spec: str) -> int:
    '''
    It returns given time delta specifier as time interval in seconds
    '''
    time_values = ''
    time = 0
    d = {'s': 1, 'm': 60, 'h': 3600, 'd': 86400}
    for (pos, char) in enumerate(t_delta_spec):
        # numbers
        if char.isdigit() or char == '.':
            time_values = time_values + char
            # number without unit
            if pos == len(t_delta_spec) - 1:
                time = int(round(float(time_values)))
                return time
        else:
            if char in d.keys():
                # unit without numbers (only single unit is accepted in this case)
                if not time_values:
                    if len(t_delta_spec) == 1:
                        return int(round(float(1) * d[char]))
                    else:
                        raise ValueError('Unsupported time format.')
                time += int(round(float(time_values) * d[char]))
                time_values = ''
                if pos == len(t_delta_spec) - 1:
                    return time
            else:
                raise ValueError('Unsupported time format.')
    else:
        raise ValueError('Empty string.')

