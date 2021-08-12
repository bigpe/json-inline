def search_in_list(data: list, map_list: list):
    map_list[0] = map_list[0].replace('?', '', 1)
    search_with_entry = True if map_list[0][0] == '+' else False
    if search_with_entry:
        map_list[0] = map_list[0].replace('+', '', 1)
    entry_count_temp = map_list[0].split('#')
    key_value = map_list[0].split(':', 1)
    if len(key_value) == 2:
        key, value = key_value
    else:
        key = key_value[0]
        value = ''
    if '#' in key:
        key = key.split('#')[0]
    if '#' in value:
        value = value.split('#')[0]
    entry_count = 1
    if len(entry_count_temp) == 2 and entry_count_temp[1].isdigit():
        entry_count = int(entry_count_temp[1])
    new_map_list = map_list[:]
    searched = False
    entry_searched = 0
    for d in data:
        if key in d.keys():
            if not value:  # If search only key
                searched = True
                entry_searched += 1
            if d.get(key) == value and value:  # If search key:value pair
                searched = True
                entry_searched += 1
            if searched and entry_searched == entry_count:  # Stop search
                data = d
                if search_with_entry:
                    data = d.get(key)
                map_list.pop(0)
                break
    if new_map_list == map_list:
        data = None
    return data, map_list
