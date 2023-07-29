import requests
import re
import datetime
import os
import time


if __name__ == "__main__":
    session = requests.Session()
    picked_problems_url = 'https://raw.githubusercontent.com/tony9402/baekjoon/main/picked.md'

    # create a folder named by today's date
    today = datetime.datetime.now().strftime('%y%m%d')
    os.mkdir(today)

    # get problem numbers from the picked.md
    res = session.get(url=picked_problems_url)
    problem_numbers = re.findall(r'\[(\d+)\]', res.text)
    for idx, pnum in enumerate(problem_numbers):
        base_url = 'https://www.acmicpc.net/problem/'
        problem_url = base_url + pnum
        os.system(f'cp template.cpp {today}/{idx+1}_{pnum}.cpp')
        # open chrome and go to the problem page
        os.system(f'open -a "Google Chrome.app" {problem_url}')
        time.sleep(1)