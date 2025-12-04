# Brute force part 1
def highest_voltage(bank):
    high_volt = 0
    for i, a in enumerate(bank):
        for b in bank[i+1:]:
            if int(a+b) > high_volt:
                high_volt = int(a+b)

    return high_volt

banks = []
with open('input.txt', 'r') as f:
    for line in f.readlines():
        banks.append(line.strip())

bank_voltage_sum = 0
for bank in banks:
    bank_voltage_sum += highest_voltage(bank)

print(bank_voltage_sum)

# Part two, sort and find 12 largest numbers and their index

def find_largest_number(jolts: str, length: int) -> str:
    if length == 0:
        return ""
    if len(jolts) == 0:
        return ""
    digit = int(jolts[0])
    digit_index = 0

    for i, jolt in enumerate(jolts):
        if len(jolts) - i < length:
            break
        if int(jolt) > digit:
            digit = int(jolt)
            digit_index = i
    
    print(f"Digit: {digit}, rest={jolts[1:]}, length={length}")
    
    return str(digit) + find_largest_number(jolts[digit_index + 1:], length - 1)


sorted_banks = []

part_two_result = 0

for bank in banks:
    num = int(find_largest_number(bank, 12))
    print(num)
    part_two_result += num

print(part_two_result)