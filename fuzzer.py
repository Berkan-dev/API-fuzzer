import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-u")
parser.add_argument("-f", type=argparse.FileType('r'))
args = parser.parse_args()
target = args.u
wordlist = args.f.readlines()

def loop():
    for word in wordlist:
        word = word.strip() 
        print(word)
        res = requests.get(url=f"{target}/{word}")
        print(res)
        if res.status_code == 404:
            continue
        else:
            data = res.json()
            print(data)
            print(res.status_code)
            print(word)

loop()