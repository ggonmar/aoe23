import sys
sys.path.append('..')
import reader
import re


entries=reader.read("input.txt","LINES")

def format_entry(str):
    id=re.search("Game (\d+):", str).group(1)
    str=re.sub("Game (\d+):", "", str).strip()
    print(id)

    print(str)
    plays=list(map(lambda i: i.strip(), str.split(';')))
    print(plays)
    
    for p in plays:
        cubes=list(map(lambda i: i.strip(), p.split(',')))
        print(cubes)
        
def part1(entries):
    return
format_entry("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green")