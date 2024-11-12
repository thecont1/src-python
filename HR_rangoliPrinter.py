import sys

def line_constructor(central_line: str) -> list:
    number_of_lines = ord(central_line[-1]) - 96
    lines = []

    for n in range(number_of_lines):
        # central_line = central_line[2*n : ][-1:1:-1] + central_line[2*n : ]
        line = '-'*n*2 + central_line[::-1][:-(2*n)-1] + central_line[2*n : ] + '-'*n*2
        lines.append(line)

    return lines

def rangoli_printer(lines: list) -> None:
    for n in range(len(lines)-1, 0, -1):
        print(lines[n])

    for n in range(len(lines)):
        print(lines[n])

N = 1

if __name__ == '__main__':
    if len(sys.argv) > 1:
        N = int(sys.argv[1])
    else:
        print("Beautiful things will happen when you provide a number between 1 and 26 (inclusive) as a command line argument. For now, we're assuming 2\n")
        N = 2

    central_line = [chr(96+n)+'-' for n in range(1, N+1)]
    central_line = ''.join(central_line)[:-1]

    rangoli_printer(line_constructor(central_line))