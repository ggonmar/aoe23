import reader
import re

def translate(v):
    match v:
        case 'one':
            return "1"
        case 'two':
            return "2"
        case 'three':
            return "3"
        case 'four':
            return "4"
        case 'five':
            return "5"
        case 'six':
            return "6"
        case 'seven':
            return "7"
        case 'eight':
            return "8"
        case 'nine':
            return "9"
        case _:
            return v        


def part1(entries):
    total=0
    for entry in entries:
        v=re.findall("\d", entry)
        first_number, last_number = v[0], v[-1]
        number=int(str(first_number) + str(last_number) )
        total = total + number
    print(total)
    return total

def part2(entries):
    total=0
    for entry in entries:
        f=re.findall("\d|one|two|three|four|five|six|seven|eight|nine|zero", entry)
        l=re.findall("\d|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin|orez", entry[::-1])
        first_number=translate(f[0])
        last_number=translate(l[0][::-1])
        number=int(str(first_number) + str(last_number) )
        total = total + number
    print(total)
    return total

entries=reader.read("day1.txt","LINES")
part1(entries)
part2(entries)