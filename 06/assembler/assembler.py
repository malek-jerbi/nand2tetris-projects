from config import COMP, DEST, JUMP
from config import SymbolTable

def first_pass(filename):
    with open(f"../{filename}/{filename}.asm", "r") as fx:
        lineCounter = 0
        for line in fx:
            linetrimmed = line.strip()
            if not linetrimmed or linetrimmed[0] == '/':
                continue
            if linetrimmed[0] == '(':
                key = linetrimmed[1:-1]
                SymbolTable[key] = lineCounter
            else:
                lineCounter += 1

def parse_line(phrase, symbol_counter):
    if not phrase or phrase[0:2] == '//' or phrase[0] == '(':
        return None, symbol_counter

    if phrase[0] == '@': 
        return handle_A_instruction(phrase, symbol_counter)
    else: 
        return handle_C_instruction(phrase), symbol_counter

def handle_A_instruction(phrase, symbol_counter):
    opcode = "0"
    x = phrase[1:]
    try:
        int(x)
    except:
        if x not in SymbolTable:
            SymbolTable[x] = symbol_counter
            symbol_counter += 1
        x = SymbolTable[x]
    instruction = str(bin(int(x))[2:].zfill(15))
    return opcode + instruction, symbol_counter

def handle_C_instruction(phrase):
    opcode = "1"
    parts = phrase.split("=")
    destination = parts[0] if len(parts) >= 2 else "null"
    rest = parts[1] if len(parts) >= 2 else parts[0]
    restparts = rest.split(";")
    comp = restparts[0]
    jump = restparts[1] if len(restparts) >= 2 else "null"
    return "111" + COMP[comp] + DEST[destination] + JUMP[jump]

def assemble(filename):
    first_pass(filename)
    symbol_counter = 16
    with open(f"../{filename}/{filename}.asm", "r") as f, open("demo.hack", "w") as w:
        for line in f:
            machine_code, symbol_counter = parse_line(line.strip(), symbol_counter)
            if machine_code:
                w.write(machine_code + '\n')


filename = "pong"
assemble(filename)
