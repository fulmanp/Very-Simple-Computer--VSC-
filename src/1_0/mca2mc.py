import sys
import re


def checkIfFit(operand, condition):
  o = int(operand)
  # Integer without a sign
  if condition in {"aa", "aaa", "aaaa", "aaaaa"}:
    if o < 0:
      return None
    d = len(condition)
    s = f"{o:0{d}d}"
    if len(s)>d:
      return None
    return s
  # Integer with a sign
  elif condition in {"ss", "sssss"}:
    d = len(condition)-1
    s = f"{abs(o):0{d}d}"
    if len(s)>d:
      return None
    if o>=0:
      s = "0" + s
    else:
      s = "1" + s
    return s
  else:
    return None


def intToBits(integer):
    bits = f"{integer:05d}"

    if integer<0:
      bits = '1' + bits[1:]

    return bits
    
    
def addressDuplicated(addresses, m):
  if m in addresses:
    return True
  else:
    addresses[m] = 1
    return False


def mca2mc(path):
  addresses = {}
  with open(path, encoding="utf8") as fileSrc:
    lines = fileSrc.readlines()

    reDirect    = re.compile("(?P<address>\d{4})\s{1}(?P<mnemonic>\w*)\s{1}(?P<operand>\d+)")
    reIndirect  = re.compile("(?P<address>\d{4})\s{1}(?P<mnemonic>\w*)\s{1}\[(?P<operand>\d+)\]")
    reImmediate = re.compile("(?P<address>\d{4})\s{1}(?P<mnemonic>\w*)\s{1}\((?P<operand>\d+)\)")
    reNoOperand = re.compile("(?P<address>\d{4})\s{1}(?P<mnemonic>\w*)")
    reData = re.compile("(?P<address>\d{4})\s{1}(?P<value>[\+-]?\d+)")

    memory = None
    mnemonic = None
    operand = None
    addressing = None
    value = None

    for l in lines:
      ln = l.split(";")
      if len(ln)>1:
        comment = ln[1].strip()
      else:
        comment = ""
      ln = ln[0].strip()
      ln = re.sub(r"\s", ' ', ln)  # The \s metacharacter matches whitespace character.
                                   # Whitespace characters can be: A space character.
                                   # A tab character. A carriage return character.
      ln = re.sub(r" +", ' ', ln)
      ln = re.sub(r"([\[\(]) ", r'\1', ln)
      ln = re.sub(r" ([\]\)])", r'\1', ln)
      
      if len(ln) == 0:
        continue
      
      # Expected line formats:
      # ADDRESS MNEMONIC ADDRESS
      # ADDRESS MNEMONIC [ADDRESS]
      # ADDRESS MNEMONIC (VALUE)
      # ADDRESS VALUE     - this must be checkd befor ADDRESS MNEMONIC
      # ADDRESS MNEMONIC
      # 1003 CPA 12
      # (?P<address>\d{4})\s{1}(?P<mnemonic>\w*)\s{1}(?P<operand>\d+)
      # 1003 NBRA [12]
      # (?P<address>\d{4})\s{1}(?P<mnemonic>\w*)\s{1}\[(?P<operand>\d+)\]
      # 1003 STO (12)
      # (?P<address>\d{4})\s{1}(?P<mnemonic>\w*)\s{1}\((?P<operand>\d+)\)
      # 1003 HLT
      # (?P<address>\d{4})\s{1}(?P<mnemonic>\w*)
      # 1003 5
      # 1003 +5
      # 1003 -5
      # (?P<address>\d{4})\s+(?P<value>[\+-]?\d+)
      
      #print(l)
      #print(ln)
      result = re.search(reDirect, ln)
      
      if result:
        memory = result['address']
        mnemonic = result['mnemonic']
        operand = result['operand']
        addressing = "direct"
        if mnemonic in {"BRA", "BRN", "BRNF", "BRZ", "BRZF"}:
          addressing = "immediate"
      else:
        result = re.search(reIndirect, ln)
        if result:
          memory = result['address']
          mnemonic = result['mnemonic']
          operand = result['operand']
          addressing = "indirect"
        else:
          result = re.search(reImmediate, ln)
          if result:
            memory = result['address']
            mnemonic = result['mnemonic']
            operand = result['operand']
            addressing = "immediate"
          else:
            result = re.search(reData, ln)
            if result:
              memory = result['address']
              value = result['value']
            else:
              result = re.search(reNoOperand, ln)
              if result:
                memory = result['address']
                mnemonic = result['mnemonic']
                addressing = "noOperand"
              else:
                print("Incorrect syntax in line:")
                print(l.strip())
                memory = None
                mnemonic = None
                operand = None
                addressing = None
                value = None
            
      if not ((memory and mnemonic) or (memory and value)):
        print("I don't know how to transform line")
        print(ln)
        print(memory, mnemonic, value)
        continue
            
      if (memory and mnemonic):      
        instructions = [
          {"mnemonic": "HLT",  "addressing": "noOperand", "opcode": "00000", "condition": None},
          {"mnemonic": "CPA",  "addressing": "direct",    "opcode": "1",     "condition": "aaaa"},
          {"mnemonic": "CPA",  "addressing": "immediate", "opcode": "921",   "condition": "ss"},
          {"mnemonic": "CPA",  "addressing": "immediate", "opcode": "93100", "condition": "sssss"},
          {"mnemonic": "CPA",  "addressing": "indirect",  "opcode": "941",   "condition": "aa"},
          {"mnemonic": "CPA",  "addressing": "indirect",  "opcode": "95100", "condition": "aaaaa"},
          {"mnemonic": "STO",  "addressing": "direct",    "opcode": "2",     "condition": "aaaa"},
          {"mnemonic": "STO",  "addressing": "indirect",  "opcode": "942",   "condition": "aa"},
          {"mnemonic": "STO",  "addressing": "indirect",  "opcode": "95200", "condition": "aaaaa"},
          {"mnemonic": "ADD",  "addressing": "direct",    "opcode": "3",     "condition": "aaaa"},
          {"mnemonic": "ADD",  "addressing": "immediate", "opcode": "923",   "condition": "ss"},
          {"mnemonic": "ADD",  "addressing": "immediate", "opcode": "93300", "condition": "sssss"},
          {"mnemonic": "ADD",  "addressing": "indirect",  "opcode": "943",   "condition": "aa"},
          {"mnemonic": "ADD",  "addressing": "indirect",  "opcode": "95300", "condition": "aaaaa"},
          {"mnemonic": "SUB",  "addressing": "direct",     "opcode": "4",     "condition": "aaaa"},
          {"mnemonic": "SUB",  "addressing": "immediate",  "opcode": "924",   "condition": "ss"},
          {"mnemonic": "SUB",  "addressing": "immediate",  "opcode": "93400", "condition": "sssss"},
          {"mnemonic": "SUB",  "addressing": "indirect",   "opcode": "945",   "condition": "aa"},
          {"mnemonic": "SUB",  "addressing": "indirect",   "opcode": "95500", "condition": "aaaaa"},
          {"mnemonic": "MUL",  "addressing": "direct",     "opcode": "5",     "condition": "aaaa"},
          {"mnemonic": "MUL",  "addressing": "immediate",  "opcode": "925",   "condition": "ss"},
          {"mnemonic": "MUL",  "addressing": "immediate",  "opcode": "93500", "condition": "sssss"},
          {"mnemonic": "MUL",  "addressing": "indirect",   "opcode": "945",   "condition": "aa"},
          {"mnemonic": "MUL",  "addressing": "indirect",   "opcode": "95500", "condition": "aaaaa"},
          {"mnemonic": "BRA",  "addressing": "immediate",  "opcode": "6",     "condition": "aaaa"},
          {"mnemonic": "BRN",  "addressing": "immediate",  "opcode": "7",     "condition": "aaaa"},
          {"mnemonic": "BRNF", "addressing": "immediate",  "opcode": "907",   "condition": "aa"},
          {"mnemonic": "BRZ",  "addressing": "immediate",  "opcode": "8",     "condition": "aaaa"},
          {"mnemonic": "BRZF", "addressing": "immediate",  "opcode": "908",   "condition": "aa"},
          {"mnemonic": "INC",  "addressing": "direct",     "opcode": "01",    "condition": "aaa"},
          {"mnemonic": "DEC",  "addressing": "direct",     "opcode": "02",    "condition": "aaa"},
          {"mnemonic": "PUSH", "addressing": "noOperand",  "opcode": "03000", "condition": None},
          {"mnemonic": "PUSH", "addressing": "direct",     "opcode": "91030", "condition": "aaaaa"},
          {"mnemonic": "PUSH", "addressing": "immediate",  "opcode": "93030", "condition": "sssss"},
          {"mnemonic": "PUSH", "addressing": "indirect",   "opcode": "95030", "condition": "aaaaa"},
          {"mnemonic": "POP",  "addressing": "noOperand",  "opcode": "04000", "condition": None},
          {"mnemonic": "POP",  "addressing": "direct",     "opcode": "91040", "condition": "aaaaa"},
          {"mnemonic": "POP",  "addressing": "indirect",   "opcode": "95040", "condition": "aaaaa"}
        ]
        
        for ins in instructions:
          done = False
          if mnemonic == ins["mnemonic"] and addressing == ins["addressing"]:
            condition = ins["condition"]
            
            if condition:
              result = checkIfFit(operand, condition)
              
              if result:
                m = "0" * (4-len(memory)) + memory
                s = str(int(memory)+1)
                m2 = "0" * (4-len(s)) + s
                if len(result) == 5:
                  if len(m)>4:
                    print(f"Memory address {m} is to big [1]")
                    return
                  elif len(m2)>4:
                    print(f"Memory address {m2} is to big [2]")
                    return
                  print(f"{m} {ins['opcode']} ; {comment}")
                  print(f"{m2} {result} ; 2nd byte")
                  if addressDuplicated(addresses, m):
                    print(f"WARNING!!! Duplication of address {m}")
                  if addressDuplicated(addresses, m2):
                    print(f"WARNING!!! Duplication of address {m2}")
                  done = True
                else:
                  m = "0" * (4-len(memory)) + memory
                  if len(m)>4:
                    print(f"Memory address {m} is to big [3]")
                    return
                  print(f"{m} {ins['opcode']}{result} ; {comment}")
                  if addressDuplicated(addresses, m):
                    print(f"WARNING!!! Duplication of address {m}")
                  done = True
            else:
              m = "0" * (4-len(memory)) + memory
              if len(m)>4:
                print(f"Memory address {m} is to big [4]")
                return
              print(f"{m} {ins['opcode']} ; {comment}")
              if addressDuplicated(addresses, m):
                print(f"WARNING!!! Duplication of address {m}")
              done = True
  
          if done:
            break
      
      elif (memory and value):
        m = "0" * (4-len(memory)) + memory
        if len(m)>4:
          print(f"Memory address {m} is to big [5]")
          return      
        
        l = len(value)
          
        if l == 5 and value.isdigit(): # Only digits, 5 digits - treat as a ready to use number
          print(f"{m} {value} ; {comment}")
        elif l > 5: # Too big, use dummy replacement
          print(f"Value {value} is not a correct value")
          print(f"{m} 00000 ; {comment}")
        else:    
          value = intToBits(int(value))
          print(f"{m} {value} ; {comment}")


def printWelcomeMsg():
  text = \
'''
Welcome to mca to mc converter
Version 1.0
Build 202410310915

Please note conversion pattern:
# asm -> mca -> mc
# asm - assembler with mnemonic, labels etc.
# mca - (Machine Code Assembler) - machine code but with some assembler syntax like mnemonics
# mc - (Machine Code) - pure machine code

To skip above header in the output you can use 'tail' command like this:
asm2mca.py program.asm | tail -n +15
'''

  print(text)
      
if __name__ == '__main__':
  printWelcomeMsg()
  mca2mc(sys.argv[1])
