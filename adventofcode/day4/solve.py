
def checkHor(lines):
    count = 0
    for line in lines:
        count += line.count("XMAS")
        count += line.count("SAMX")
    return count

def checkVer(lines):
    count = 0
    for c in range(len(lines[1])):
        col = ""
        for row in range(len(lines)):
            col += lines[row][c]
        count += col.count("XMAS")
        count += col.count("SAMX")

        count 

    return count


def checkDiag(lines):
    count = 0
    for row in range(0, len(lines) - 3):
        for col in range(len(lines[0]) - 3):
            diag_string = lines[row][col]
            diag_string += lines[row+1][col+1]
            diag_string += lines[row+2][col+2]
            diag_string += lines[row+3][col+3]

            if diag_string == "XMAS":
                count += 1

            if ''.join(reversed(diag_string)) == "XMAS":
                count += 1

    for row in range(0, len(lines)-3):
        for col in range(3, len(lines[0])):
            diag_string = lines[row][col]
            diag_string += lines[row+1][col-1]
            diag_string += lines[row+2][col-2]
            diag_string += lines[row+3][col-3]

            if diag_string == "XMAS":
                count += 1

            if ''.join(reversed(diag_string)) == "XMAS":
                count += 1

    return count


with open("test.txt", "r") as f:
    lines = f.readlines()


print(checkHor(lines))
print(checkVer(lines))
print(checkDiag(lines))


# Part two

def checkMasDiag(lines, row, col):
    diag1 = lines[row-1][col-1] + 'A' + lines[row+1][col+1]
    diag2 = lines[row+1][col-1] + 'A' + lines[row-1][col+1]

    return (diag1 in ["SAM", "MAS"]) and (diag2 in ["SAM", "MAS"])


count = 0
for row in range(1, len(lines) - 1):
    for col in range(1, len(lines[row]) - 1):
        if lines[row][col] == "A" and checkMasDiag(lines, row, col):
            print("-" * 10)
            print(f"{lines[row-1][col-1]} - {lines[row+1][col+1]}")
            print("- A -")
            print(f"{lines[row+1][col-1]} - {lines[row-1][col+1]}")
            count += 1
print("---")
print(count)

