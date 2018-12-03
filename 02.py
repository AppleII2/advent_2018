import os
def getdata(url):
    import requests
    sess_cookie = {'session': os.environ['ADVENT_SESSION_COOKIE']}
    data = requests.get(url, cookies=sess_cookie)
    return data

def part1(data):
    twos = threes = 0
    for item in data.text.split():
        recurs = [item.count(letter) for letter in set(item)]
        if 2 in recurs:
            twos += 1
        if 3 in recurs:
            threes += 1
    return twos * threes

def part2(data):
    for i, item in enumerate(data):
        for compare_item in data[i:]:
            diff = 0
            for j, letter in enumerate(item):
                if letter != compare_item[j]:
                    diff += 1
            if diff == 1:
                for k, letter in enumerate(item):
                    if letter != compare_item[k]:
                        return item[:k] + item[k+1:]
