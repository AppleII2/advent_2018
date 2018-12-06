import os
def getdata(url):
    import requests
    sess_cookie = {'session':os.environ['ADVENT_SESSION_COOKIE']}
    data = requests.get(url, cookies=sess_cookie)
    return data

def breakdown(string, function, startfunction=False):
    if startfunction:
        startfunction()
    starttime = time.time()
    while True:
        string_new = string
        string = function(string)
        if string_new == string:
            endtime = time.time()
            print(endtime - starttime)
            return len(string)

def listloop_solution(string):
    string = list(string)
    for i in range(1, len(string)):
        if string[i].lower() == string[i-1].lower() and string[i] != string[i-1]:
            string[i] = string[i-1] = ''
    return ''.join(string)

def regex_solution(string):
    return re.sub(regex, '', string)


def create_regex():
    alphabet = "qwertyuiopasdfghjklzxcvbnm"
    regex = ''
    for letter in alphabet:
        regex += letter + letter.upper() + "|"
        regex += letter.upper() + letter + "|"
    return regex.strip('|')

def part2(string, function, startfunction=False):
    results = {}
    alphabet = "qwertyuiopasdfghjklzxcvbnm"
    for letter in alphabet + alphabet.upper():
        chopped_string = re.sub(letter, '', string)
        results[letter] = breakdown(chopped_string, function, startfunction)
    return results[max(results, key=results.get)] 
        
