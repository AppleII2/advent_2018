import os
def getdata(url):
    import requests
    sess_cookie = {'session':os.environ['ADVENT_SESSION_COOKIE']}
    data = requests.get(url, cookies=sess_cookie)
    return data

def instruction_to_set(instruction):
    id = instruction.split()[0]
    start_x, start_y = instruction.split()[2].strip(":").split(",")
    start_x, start_y = int(start_x), int(start_y)
    dim_x, dim_y = instruction.split()[3].split("x")
    used_areas = []
    for x in range(int(dim_x)):
        for y in range(int(dim_y)):
            used_inch = str(start_x + x) + "," + str(start_y + y)
            used_areas.append(used_inch)
    return used_areas, set(used_areas), id

def part1(data):
    areas = []
    sets = {}
    for claim in data.text.split('\n')[:-1]: # There is a trailing newline on this data
        claim_area, claim_set, claim_id = instruction_to_set(claim)
        sets[claim_id] = claim_set
        areas += claim_area
    observed = set()
    repeated = set()
    for coordinate in areas:
        if coordinate in observed:
            repeated.add(coordinate)
        else:
            observed.add(coordinate)
    return repeated, len(repeated), sets

def part2(repeated, sets):
    for key, value in sets.items():
        if value.isdisjoint(repeated):
            return key
