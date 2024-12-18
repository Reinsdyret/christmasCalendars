
def getCombValue(registers, combOp):
  if 0 <= combOp <= 3:
    return combOp
  
  if combOp == 4: return registers["A"]
  if combOp == 5: return registers["B"]
  if combOp == 6: return registers["C"]

  raise ValueError("Got 7 as a combo operator")


def adv(registers, combOp):
  value = getCombValue(registers, combOp)
  registers["A"] = int(registers["A"] / (2 ** value))


def bxl(registers, lit):
  registers["B"] = registers["B"] ^ lit


def bst(registers, combOp):
  val = getCombValue(registers, combOp) % 8
  registers["B"] = val


def jnz(instr_pointer, registers, lit):
  if registers["A"] == 0: return instr_pointer
  return lit


def bxc(registers, op):
  val = registers["B"] ^ registers["C"]
  registers["B"] = val


def out(registers, combOp):
  return f"{getCombValue(registers, combOp) % 8}"


def bdv(registers, combOp):
  value = getCombValue(registers, combOp)
  registers["B"] = int(registers["A"] / (2 ** value))


def cdv(registers, combOp):
  value = getCombValue(registers, combOp)
  registers["C"] = int(registers["A"] / (2 ** value))


def doInstructions(registers, instructions):
  instruct_pointer = 0
  output = []

  while instruct_pointer < len(instructions) - 1:
    #print(registers)
    instruction = instructions[instruct_pointer]
    op = instructions[instruct_pointer + 1]

    match instruction:
      case 0: adv(registers, op)
      case 1: bxl(registers, op)
      case 2: bst(registers, op)
      case 3:
        new_instruction_pointer = jnz(instruct_pointer, registers, op)
        if new_instruction_pointer != instruct_pointer:
          instruct_pointer = new_instruction_pointer
          continue
      case 4: bxc(registers, op)
      case 5: output.append(out(registers, op))
      case 6: bdv(registers, op)
      case 7: cdv(registers, op)

    instruct_pointer += 2
  return output

registers = {
  "A": 0,
  "B": 0,
  "C": 0
}
instructions = []
with open("input.txt", 'r') as f:
  lines = f.readlines()
  registers["A"] = int(lines[0].split(' ')[-1])
  registers["B"] = int(lines[1].split(' ')[-1])
  registers["C"] = int(lines[2].split(' ')[-1])

  instructions = list(map(int, lines[4].split(' ')[-1].split(',')))
  print(','.join(doInstructions(registers, instructions)))

# Part two

graph = {i: [] for i in range(1,10)}


def checkIthDigit(i, res, wanted):
  val1 = res[-i + 1]
  val2 = wanted[-i + 1]
  return val1 == val2





"""
for i in range(1000000000000000, 9999999999999999):
  if i % 100000 == 0:
    print(i / 9999999999999999 * 100)
  registers["A"] = i

  if doInstructions(registers, instructions) == instructions:
    print(i)
    break
"""