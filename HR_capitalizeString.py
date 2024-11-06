# HackerRank Problem: https://www.hackerrank.com/challenges/capitalize/problem

def solve(s):
    r = ' '.join([x[0].upper()+x[1:] for x in s.split()])

    if len(s) != len(r):
        r = list(r)
        for i in range(len(s)):
            if s[i].lower() != r[i].lower():
                r.insert(i, s[i])
        r = ''.join(r)

    return r 

if __name__ == '__main__':
    s = "mahesh    shantaram   i"

    print(f"Original String: {s}")
    print(f"Modified String: {solve(s)}")
