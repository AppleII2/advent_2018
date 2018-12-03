import os
def getdata(url):
    import requests
    sess_cookie = {'session': os.environ['ADVENT_SESSION_COOKIE']}
    data = requests.get(url, cookies=sess_cookie)

def part1(data):
    total = 0
    for item in data.text.split():
        total += int(item.strip("+"))
    return total

def part2(data):
    total = 0
    past_frequencies = {0}
    while True:
        for item in data.text.split():
            total += int(item.strip("+"))
            if total in past_frequencies:
                return total
            else:
                past_frequencies.add(total)

