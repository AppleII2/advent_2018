import os
def getdata(url):
    import requests
    sess_cookie = {'session':os.environ['ADVENT_SESSION_COOKIE']}
    data = requests.get(url, cookies=sess_cookie)
    return data

def sort_by_timestamp(data):
    from datetime import datetime
    data = data.text.split('\n')[:-1] # Another trailing newline here, whyyyyy
    dt_list = []
    for entry in data:
        entry = entry.strip('[').split(']')
        entry[0] = datetime.strptime(entry[0], '%Y-%m-%d %H:%M')
        dt_list.append(entry)
    dt_list.sort(key = lambda x: x[0])
    return dt_list

def group_by_night(ordered_list):
    nights = []
    for entry in ordered_list:
        if entry[1][-2:] == "ft": # If entry is a guard beginning his shift
            try: # hacky way to get around first entry being empty
                nights.append(night)
            except:
                print("----")
            night = []
            night.append(entry)
        else:
            night.append(entry)
    nights.append(night)
    return nights

def create_array(group):
    array = [0] * 60
    for i, entry in enumerate(group[1::2]): # Skips entry for coming on-duty, counts every 2nd entry (wakeups)
        start_min = int('{d.minute}'.format(d=entry[0]))
        end_min = int('{d.minute}'.format(d=group[group.index(entry)+1][0]))
        for j in range(start_min, end_min):
            array[j] += 1
    return array

def create_arrays(grouped_list):
    guards = {}
    import re
    from operator import add
    for group in grouped_list:
        array = create_array(group)
        guard_id = group[0][1]
        guard_id = int(re.findall('\d+', guard_id)[0]) # TODO: More readable than doing a split+strip chain, time for performance + compare
        if guard_id in guards.keys():
            guards[guard_id] = list(map(add, array, guards[guard_id]))
        else:
            guards[guard_id] = array
    guard_totals = {}
    for key, value in guards.items():
        guard_totals[key] = sum(value)
    return guards, guard_totals

def part1(data):
    sorted_list = sort_by_timestamp(data)
    groups = group_by_night(sorted_list)
    guard_arrays, guard_totals = create_arrays(groups)
    sleepiest_guard = max(guard_totals, key=guard_totals.get)
    sleepiest_minute = guard_arrays[sleepiest_guard].index(max(guard_arrays[sleepiest_guard]))
    return sleepiest_guard, sleepiest_minute

def part2(data):
    sorted_list = sort_by_timestamp(data)
    groups = group_by_night(sorted_list)
    guard_arrays, guard_totals = create_arrays(groups)
    guard_max_minute = {}
    for key, value in guard_arrays.items():
        guard_max_minute[key] = max(value)
    consistent_guard = max(guard_max_minute, key=guard_max_minute.get)
    consistent_minute = guard_arrays[consistent_guard].index(max(guard_arrays[consistent_guard]))
    return consistent_minute * consistent_guard
