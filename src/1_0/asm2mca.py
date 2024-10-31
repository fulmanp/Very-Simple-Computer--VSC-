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


def getInstructions():
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
  
  return instructions


def isInstruction(sequence):
  instructions = getInstructions()
  for i in instructions:
    if i["mnemonic"] == sequence:
      return True
  return False


def intToAddress(a):
  if type(a) is int and a<9999 and a>=0:
    bits = f"{a:04d}"
    return bits
  return "0000"


def isNumber(sequence):
  s = ""
  
  if sequence[0] in ["+", "-"]:
    sign = sequence[0]
    value = sequence[1:]
  else:
    sign = "+"
    value = sequence
  
  if value.isdigit():
    l = len(value)
    if l == 5 and len(sequence) == 5: # Binary number, no need to encode
      return {"result": "ok", "value": s}
    elif l < 5:
      if sign == "+":
        s = "0"
      else:
        s = "1"
      
      s += "0"*(4-l) + value

      return {"result": "ok", "value": s}
    else:
      v = f"Sequence {sequence} is to long to be a correct number"
      return {"result": "error", "value": v}
  else:
    return {"result": "ok", "value": None}


def normalizeLines(lines):
  linesNew = []
  labels = []
  
  for l in lines:
    # There may be at most one ":" and one ";" character in every line
    # todo
    
    ln = l.split(";")
    if len(ln)>1:
      comment = ln[1].strip()
    else:
      comment = ""
    ln = ln[0].strip()
    ln = re.sub(r"\s", ' ', ln)
    ln = re.sub(r"([\[\(])", r' \1 ', ln)
    ln = re.sub(r"([\]\)])", r' \1 ', ln)
    ln = re.sub(r"(:)", r' \1 ', ln)
    ln = re.sub(r" +", ' ', ln)
    
    if len(ln) > 0:
      # If line starts with "." this is directive. Do nothing with this.
      if ln.startswith("."):
        linesNew.append(ln)
      else: # Make sure that every line has unique label
        # Add or modify label i every line.
        # Check if label is present.
        # Check if ":" is present.
        if ":" in ln:
          ln = ln.split(":")
          # Check if label exists.
          if len(ln)>1:
            label = ln[0].strip()
            labels.append(label)
            ln = label + " : " + ln[1].strip()
          else: # There is only ":" without any label.
            ln = " : " + ln[0].strip()
        else: # There is no label.
          ln = " : " + ln
          
        if comment == "":
          linesNew.append(ln)
        else:
          linesNew.append(ln + " ; " + comment)

  return (linesNew, labels)


def getTokens(lines, labels):
  def msgError(instruction, line):
    print(f"Unsupported instruction format: {instruction}")
    print(f"in line: {line}")
      
  tokens = []
  for line in lines:
    t = []
    ln = line.strip()
    ln = ln.split(";")
    if len(ln)>1:
      comment = ln[1].strip()
      ln = ln[0].strip().split(" ")
      ln.append(";")
      ln.append(comment)
    else:
      ln = ln[0].strip().split(" ")
    
    # Check if directive
    if ln[0] == ".data":
      if len(ln) > 1 and ln[1].isdigit():
        t = {"type": "directive", "value": ln[1], "subtype": "data"}
        tokens.append([t])
        continue
      else:
        print(f"Incomplete directive in line: {line}")
        return None
    elif ln[0] == ".code":
      if len(ln) > 1 and ln[1].isdigit():
        t = {"type": "directive", "value": ln[1], "subtype": "code"}
        tokens.append([t])
        continue
      else:
        print(f"Incomplete directive in line: {line}")
        return None
    
    # Line is not directive - proceed
    # Divide line into three sections: label, instruction and comment
    labelSeparatorIndex = None
    commentSeparatorIndex = None
    
    for i, e in enumerate(ln):
      if e == ":":
        labelSeparatorIndex = i
      elif e == ";":
        commentSeparatorIndex = i

    if commentSeparatorIndex is not None:
      if commentSeparatorIndex < len(ln)-1:
        comment = ln[(commentSeparatorIndex+1):]
      else:
        comment = None
    else:
      comment = None
    
    if labelSeparatorIndex is not None:  
      if labelSeparatorIndex > 0:
        label = ln[0:labelSeparatorIndex]
      else:
        label = None
    else:
      label = None
        
    if (commentSeparatorIndex is not None) and (labelSeparatorIndex is not None):
      instruction = ln[labelSeparatorIndex+1:commentSeparatorIndex]
    elif (commentSeparatorIndex is not None):
      instruction = ln[:commentSeparatorIndex]
    elif (labelSeparatorIndex is not None):
      instruction = ln[labelSeparatorIndex+1:]
    
    #print(ln)
    #print(label)
    #print(comment)
    #print(instruction)
    
    if label:
      t.append({"type": "label", "value": label[0]})
    
    lIns = len(instruction)
    if lIns == 1:
      mnemonic = instruction[0]
      operand = None
      addressing = "noOperand"
      
      # Check if this is an instruction or value or label
      v = isNumber(mnemonic)
      if v["result"] == "error":
        print(v["value"])
        return None
      v = v["value"]
      if isInstruction(mnemonic):
        t.append({"type": "instruction", "value": mnemonic})
      elif v is not None:
        t.append({"type": "data", "value": v, "subtype": "number"})
      elif mnemonic in labels:
        t.append({"type": "data_label", "value": mnemonic})
      else:
        msgError(instruction, line)
        return None
    elif lIns == 2 or lIns == 4:
      if lIns == 2:
        mnemonic = instruction[0]
        operand = instruction[1]
        addressing = "direct"
      elif lIns == 4:  
        mnemonic = instruction[0]
        operand = instruction[2]
        if instruction[1] == "[" and instruction[3] == "]":
          addressing = "indirect"
        elif instruction[1] == "[" and instruction[3] == "]":
          addressing = "immediate"
          
      if mnemonic in {"BRA", "BRN", "BRNF", "BRZ", "BRZF"}:
          addressing = "immediate"
        
      if isInstruction(mnemonic):
        if operand in labels:
          
          t.append({"type": "instruction", "value": mnemonic, "addressing": addressing})
          t.append({"type": "operand_label", "value": operand})
          #tokens.append(t)
        elif operand.isDigit() and len(operand) == 5:
          t = []
          t.append({"type": "instruction", "value": mnemonic, "addressing": addressing})
          t.append({"type": "operand_number", "value": operand})
          #tokens.append(t)
      else:
        print(f"{mnemonic} is not mnemonic in line: {line}")
        return None
    else:
      print(f"Unsupported instruction format: {instruction}")
      print(f"in line: {line}")
      return None
    
    tokens.append(t)
    
  return tokens


def reorganizeTokens(tokens):
  tokensAsDictionaries = []
  for t in tokens:
    d = {}
    
    for tt in t:
      d[tt["type"]] = tt
      
    tokensAsDictionaries.append(d)
  
  return tokensAsDictionaries


def processTokens(tokens):
  memory = []
  labels = {}
  a = None
  
  # First pass: assume all instructiona are one byte but reserve 2 butes for each
  for t in tokens:
    if "directive" in t: # At this moment directives only defines beginning of blocks
      a = int(t["directive"]["value"])
    elif "data" in t: # I have only data, so it must be located in a one memory cell
      addr = intToAddress(a)
      if "label" in t:
        labels[t["label"]["value"]] = addr
        memory.append({"address": addr, "value": t["data"]["value"], "label": t["label"]["value"]})
      else:
        memory.append({"address": addr, "value": t["data"]["value"]})
      a += 1
    elif "data_label" in t: # I have only data, so it must be located in a one memory cell
      addr = intToAddress(a)
      if "label" in t:
        labels[t["label"]["value"]] = addr
      memory.append({"address": addr, "data_label": t["data_label"]["value"], "value": None})
      a += 1
    elif "instruction" in t:
      addr = intToAddress(a)
      instruction = t["instruction"]["value"]
      
      if "label" in t:
        label = t["label"]["value"]
        labels[t["label"]["value"]] = addr
      else:
        label = None
      if "operand_label" in t:
        operand_label = t["operand_label"]["value"]
        addressing = t["instruction"]["addressing"]
        if label:
          memory.append({"address": addr, "value": instruction, "operand_label": operand_label, "operand": None, "addressing": addressing, "bytes": 2, "label": label})
        else:
          memory.append({"address": addr, "value": instruction, "operand_label": operand_label, "operand": None, "addressing": addressing, "bytes": 2})
        a += 1
        addr = intToAddress(a)
        memory.append({"address": addr, "value": "NOP"})
        a += 1
      elif "operand_number" in t:
        # If operand is exact number there is no need to gues instruction size
        operand = t["operand_number"]["value"]
        #tutu
      else:
        if label:
          memory.append({"address": addr, "value": instruction, "label": label})
        else:
          memory.append({"address": addr, "value": instruction})
        a += 1
      
  # Second pass: iteratively try to remove NOPs
  instructions = getInstructions()
  for _ in range(len(memory)): # len(memory) is the upper limit of iterations
    # Substitute all labels with numbers.
    for m in memory:
      if "data_label" in m:
        m["value"] = labels[m["data_label"]]
      elif "operand_label" in m:
        m["operand"] = labels[m["operand_label"]]
    # Check number of bytes for instructions.
    # First instruction with reduced NOP stop searching
    # and force to move all subsequent instructions
    # and recalculate all addresses for labels.
    
    relocate = False
    relocationIndex = None
    for i, m in enumerate(memory):
      relocate = False
      for ins in instructions:
        if "value" in m and "addressing" in m:
          if m["value"] == ins["mnemonic"] and m["addressing"] == ins["addressing"]:
            condition = ins["condition"]
          
            if condition:
              operand = m["operand"]
              result = checkIfFit(operand, condition)
              if result:
                #print(f"Fit to {ins}")
                if len(result)<5 and m["bytes"] == 2:
                  #print("Relocate")
                  m["bytes"] = 1
                  relocate = True
                  relocationIndex = i
                  break
      
      if relocate == True:
        break
    
    if relocate == False:
      break
    
    # Do relocation.
    #print(f"Start relocation form index {i} and instruction {m}")
    memoryNew = memory[0:i+1]
    for i in range(i+2,len(memory)):
      e = memory[i]
      a = int(e["address"])
      a -= 1
      addr = intToAddress(a)
      e["address"] = addr
      memoryNew.append(e)
      
    memory = memoryNew
      
    # Update all labels
    for m in memory:
      if "label" in m:
        addr = m["address"]
        label = m["label"]
        if labels[label] != addr:
          #print(f"Update label {label} to new value {addr}")
          labels[label] = addr
   
  return (memory, labels)


def getMCA(memory):
  newMemory = []
  for m in memory:
    addr = m["address"]
    value = m["value"]
    if value.isdigit():
      l = len(value)
      if l<5:
        value = "0"*(5-l) + value
      newMemory.append(f"{addr} {value}")
    else:
      if "operand" in m:
        operand = m["operand"]  
        addrMode = m["addressing"]
        
        if addrMode == "direct":
          newMemory.append(f"{addr} {value} {operand}")
        elif addrMode == "indirect":
          newMemory.append(f"{addr} {value} [{operand}]")
        elif addrMode == "immediate":
          if value in {"BRA", "BRN", "BRNF", "BRZ", "BRZF"}:
            newMemory.append(f"{addr} {value} {operand}")
          else:
            newMemory.append(f"{addr} {value} ({operand})")
      else:
        if value != "NOP":  
          newMemory.append(f"{addr} {value}")
      
  return newMemory


def asm2mca(path):
  addresses = {}
  with open(path, encoding="utf8") as fileSrc:
    lines = fileSrc.readlines()
    lines, labels = normalizeLines(lines)
    tokens = getTokens(lines, labels)
    tokens = reorganizeTokens(tokens)
    memory, labels = processTokens(tokens)
    memory = getMCA(memory)
    
    for m in memory:
      print(m)


def printWelcomeMsg():
  text = \
'''
Welcome to asm to mca converter
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
  asm2mca(sys.argv[1])
