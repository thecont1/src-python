import sys

def line_constructor(central_line: str) -> list:
    # Calculate the number of lines based on the last character in the central_line
    number_of_lines = ord(central_line[-1]) - 96
    lines = []

    for n in range(number_of_lines):
        # Construct each line by reversing the central_line up to a certain point and appending the rest
        # Add dashes to the beginning and end to center the line
        line = '-'*n*2 + central_line[::-1][:-(2*n)-1] + central_line[2*n : ] + '-'*n*2
        lines.append(line)

    return lines

def rangoli_printer(lines: list) -> None:
    # Print the lines in reverse order except the first one
    for n in range(len(lines)-1, 0, -1):
        print(lines[n])

    # Print the lines in normal order
    for n in range(len(lines)):
        print(lines[n])

if __name__ == '__main__':
    # Check if a command line argument is provided
    N = 2
    if len(sys.argv) > 1:
        N = int(sys.argv[1])
    else:
        # Default to 2 if no argument is provided
        print("Beautiful things will happen when you provide a number between 1 and 26 (inclusive) as a command line argument. For now, we're assuming 2\n")

    # Construct the central line of the rangoli
    central_line = [chr(96+n)+'-' for n in range(1, N+1)]
    central_line = ''.join(central_line)[:-1]

    # Generate and print the rangoli
    rangoli_printer(line_constructor(central_line))