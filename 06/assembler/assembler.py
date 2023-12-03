# this is a one off script that assumes no errors in the input file
from config import COMP, DEST, JUMP



f = open("../pong/pongL.asm", "r")
w = open("demo.hack", "w")
line = True
while line:
    line=f.readline()
    print(line, end="")
    if line[0:2] == '//':
        continue
    phrase=line.strip()
    if not phrase:
        continue

    opcode = None
    instruction = None
    
    if phrase[0] == '@': 
        opcode="0"
        instruction=str(bin(int(phrase[1:]))[2:].zfill(15))
        #print("opcode:", opcode, "instruction", instruction)
        machine_code = opcode+instruction
        print(opcode+instruction)
        w.write(machine_code + '\n')
    else: 
        opcode="1"
        parts=phrase.split("=")
        destination=parts[0] if len(parts) >= 2 else "null"
        rest=parts[1] if len(parts) >= 2 else parts[0]
        restparts=rest.split(";")
        comp=restparts[0]
        jump=restparts[1] if len(restparts) >= 2 else "null"
        print("opcode:", opcode, "destination:", destination,  "comp:", comp, "jump:", jump)
        machine_code = "111" + COMP[comp] + DEST[destination] + JUMP[jump]
        print(machine_code)
        w.write(machine_code + '\n')