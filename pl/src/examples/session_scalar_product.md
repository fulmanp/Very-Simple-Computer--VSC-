# Example VSC session on `scalar_product.asm` file

In this example you will learn how to use VSC working on [`scalar_product.asm`](scalar_product.asm) file.

**Created: 2024-10-31** and **Updated: 2024-10-31**

## Session steps


- **Step 1: convert `*.asm` file to `*.mca`.
  
  ```
  fulmanp@MacBook-Pro-Piotr xx % python3 asm2mca.py scalar_product.asm | tail -n +15 > scalar_product.mca
  ```
  
  See: [`scalar_product.asm`](scalar_product.asm), [`scalar_product.mca`](scalar_product.mca)

- **Step 2: convert `*.mca` file to `*.mc`.
  
  ```
  fulmanp@MacBook-Pro-Piotr xx % python3 mca2mc.py scalar_product.mca | tail -n +15 > scalar_product.mc
  ```
  
  See: [`scalar_product.mca`](scalar_product.mca), [`scalar_product.mc`](scalar_product.mc)

- **Step 3: start VSC**

  ```
  fulmanp@MacBook-Pro-Piotr xx % python3 vsc.py
  
  Welcome to VSC (Very Simple Computer)
  Version 1.0
  Build 202410252242
  Type -h and confirm with ENTER for help.
  
  >
  ```
  
- **Step 4: load the code**

  ```
  > -load scalar_product.mc
  Program loaded from: scalar_product.mc
  ```

- **Step 5: set the address of the first instruction**
  
  In this step you set the address of the first instruction VSC should execute:
  
  ```
  > -startAddr 130
  Starting at address: 130
  ```

- **Step 6: see memory state at a given addresses**

  Any time you want, you may see values at give addresses specified as a single number, range, list of numbers and/or ranges:


  ```
  > -show -memory 109-110
  M[0109] = 00000
  M[0110] = 00003
  ```
  
- **Step 7: execute one instruction**

  Start first iteration:

  ```
  > -run -step
  Executing one instruction
  Registers:
  IR = 10110
  BP = 9999
  SP = 9999
   A = None
  IP = 130
  Flags:
  zero     = False
  negative = False
  
  Description: Copy value from memory at address aaaa to accumulator, A := M[aaaa].
  Mnemonic: CPA aaaa
  Machine code: 1aaaa
  Addressing: direct
  Value at address 0110: 00003
  Value in accumulator as bits: 00003
  Value in accumulator as int: +0003
  ```
    
- **Step 8: repeat last command**
    
  To repeat last command, in this case `-run -step`, it is enough to press **ENTER**.
    
  ```
  Executing one instruction
  Registers:
  IR = 80142
  BP = 9999
  SP = 9999
   A = 00003
  IP = 131
  Flags:
  zero     = False
  negative = False
  
  Description: Conditional branch to instruction located at address aaaa if value stored in accumulator is equal to zero.
  Mnemonic: BRZ aaaa
  Machine code: 8aaaa
  Addressing: direct
  Address: 0142
  Value in accumulator: 00003
  Value in accumulator is not equal to zero
  ```

- **Step 9: repeat last command**    

  ```
  Executing one instruction
  Registers:
  IR = 95100
  BP = 9999
  SP = 9999
   A = 00003
  IP = 132
  Flags:
  zero     = False
  negative = False
  
  Description: Copy value from memory at address given in memory at address aaaaa to accumulator, A := M[M[aaaaa]].
  Mnemonic: CPA [aaaaa]
  Machine code: 95100 aaaaa
  Addressing: indirect, two byte length
  Value: 00001
  Value in accumulator as bits: 00001
  Value in accumulator as int: +0001
  ```

- **Step 10: repeat last command**    

  ```
  Executing one instruction
  Registers:
  IR = 95500
  BP = 9999
  SP = 9999
   A = 00001
  IP = 134
  Flags:
  zero     = False
  negative = False
  
  Description: Multiply value from accumulator by value from memory at address given in memory at address aaaaa, A := A * M[M[aaaaa]].
  Mnemonic: MUL [aaaaa]
  Machine code: 95500 aaaaa
  Addressing: indirect, two byte length
  Value as bits: 10003
  Value as int: -0003
  Value in accumulator as bits: 10003
  Value in accumulator as int: -0003
  ```

- **Step 11: repeat last command**    

  ```
  Executing one instruction
  Registers:
  IR = 30109
  BP = 9999
  SP = 9999
   A = 10003
  IP = 136
  Flags:
  zero     = False
  negative = True
  
  Description: Add value at specified address aaaa to accumulator. Result is stored in accumulator, A := A + M[aaaa].
  Mnemonic: ADD aaaa
  Machine code: 3aaaa
  Addressing: direct
  Address: 0109
  Value at address 0109 as bits: 00000
  Value at address 0109 as int: 00000
  Value in accumulator as bits: 10003
  Value in accumulator as int: -0003
  ```

- **Step 12: repeat last command**    

  ```
  Executing one instruction
  Registers:
  IR = 20109
  BP = 9999
  SP = 9999
   A = 10003
  IP = 137
  Flags:
  zero     = False
  negative = True
  
  Description: Copy value from accumulator to memory at address aaaa, M[aaaa] := A.
  Mnemonic: STO aaaa
  Machine code: 2aaaa
  Addressing: direct
  Store at address 0109 value: 10003
  ```

- **Step 13: repeat last command**    

  ```
  Executing one instruction
  Registers:
  IR = 01107
  BP = 9999
  SP = 9999
   A = 10003
  IP = 138
  Flags:
  zero     = False
  negative = True
  
  Description: Increase value at address aaa by 1, M[aaa] := M[aaa] + 1.
  Mnemonic: INC aaa
  Machine code: 01aaa
  Addressing: direct
  Old value at address 0107 as bits: 00101
  Old value at address 0107 as int: +0101
  New value at address 0107 as bits: 00102
  New value at address 0107 as int: +0102
  ```

- **Step 14: repeat last command**    

  ```
  Executing one instruction
  Registers:
  IR = 01108
  BP = 9999
  SP = 9999
   A = 10003
  IP = 139
  Flags:
  zero     = False
  negative = False
  
  Description: Increase value at address aaa by 1, M[aaa] := M[aaa] + 1.
  Mnemonic: INC aaa
  Machine code: 01aaa
  Addressing: direct
  Old value at address 0108 as bits: 00104
  Old value at address 0108 as int: +0104
  New value at address 0108 as bits: 00105
  New value at address 0108 as int: +0105
  ```

- **Step 15: repeat last command**    

  ```
  Executing one instruction
  Registers:
  IR = 02110
  BP = 9999
  SP = 9999
   A = 10003
  IP = 140
  Flags:
  zero     = False
  negative = False
  
  Description: Decrease value at address aaa by 1, M[aaa] := M[aaa] - 1.
  Mnemonic: DEC aaa
  Machine code: 02aaa
  Addressing: direct
  Old value at address 0110 as bits: 00003
  Old value at address 0110 as int: +0003
  New value at address 0110 as bits: 00002
  New value at address 0110 as int: +0002
  ```

- **Step 16: repeat last command**    

  ```
  Executing one instruction
  Registers:
  IR = 60130
  BP = 9999
  SP = 9999
   A = 10003
  IP = 141
  Flags:
  zero     = False
  negative = False
  
  Description: Unconditional branch to instruction located at address aaaa.
  Mnemonic: BRA aaaa
  Machine code: 6aaaa
  Addressing: direct
  Address: 0130
  ```

- **Step 17: repeat last command**    

  Start second iteration:
    
  ```
  Executing one instruction
  Registers:
  IR = 10110
  BP = 9999
  SP = 9999
   A = 10003
  IP = 130
  Flags:
  zero     = False
  negative = False
  
  Description: Copy value from memory at address aaaa to accumulator, A := M[aaaa].
  Mnemonic: CPA aaaa
  Machine code: 1aaaa
  Addressing: direct
  Value at address 0110: 00002
  Value in accumulator as bits: 00002
  Value in accumulator as int: +0002
  ```

- **Step 18: repeat last command**    

  Execute the rest of the code without any breaks:

  ```
  > -run
  Executing code (max. 100 instructions)
  Registers:
  IR = 80142
  BP = 9999
  SP = 9999
   A = 00002
  IP = 131
  Flags:
  zero     = False
  negative = False
  
  Description: Conditional branch to instruction located at address aaaa if value stored in accumulator is equal to zero.
  Mnemonic: BRZ aaaa
  Machine code: 8aaaa
  Addressing: direct
  Address: 0142
  Value in accumulator: 00002
  Value in accumulator is not equal to zero
  Registers:
  IR = 95100
  BP = 9999
  SP = 9999
   A = 00002
  IP = 132
  Flags:
  zero     = False
  negative = False
  
  Description: Copy value from memory at address given in memory at address aaaaa to accumulator, A := M[M[aaaaa]].
  Mnemonic: CPA [aaaaa]
  Machine code: 95100 aaaaa
  Addressing: indirect, two byte length
  Value: 00002
  Value in accumulator as bits: 00002
  Value in accumulator as int: +0002
  Registers:
  IR = 95500
  BP = 9999
  SP = 9999
   A = 00002
  IP = 134
  Flags:
  zero     = False
  negative = False
  
  Description: Multiply value from accumulator by value from memory at address given in memory at address aaaaa, A := A * M[M[aaaaa]].
  Mnemonic: MUL [aaaaa]
  Machine code: 95500 aaaaa
  Addressing: indirect, two byte length
  Value as bits: 10002
  Value as int: -0002
  Value in accumulator as bits: 10004
  Value in accumulator as int: -0004
  Registers:
  IR = 30109
  BP = 9999
  SP = 9999
   A = 10004
  IP = 136
  Flags:
  zero     = False
  negative = True
  
  Description: Add value at specified address aaaa to accumulator. Result is stored in accumulator, A := A + M[aaaa].
  Mnemonic: ADD aaaa
  Machine code: 3aaaa
  Addressing: direct
  Address: 0109
  Value at address 0109 as bits: 10003
  Value at address 0109 as int: -0003
  Value in accumulator as bits: 10007
  Value in accumulator as int: -0007
  Registers:
  IR = 20109
  BP = 9999
  SP = 9999
   A = 10007
  IP = 137
  Flags:
  zero     = False
  negative = True
  
  Description: Copy value from accumulator to memory at address aaaa, M[aaaa] := A.
  Mnemonic: STO aaaa
  Machine code: 2aaaa
  Addressing: direct
  Store at address 0109 value: 10007
  Registers:
  IR = 01107
  BP = 9999
  SP = 9999
   A = 10007
  IP = 138
  Flags:
  zero     = False
  negative = True
  
  Description: Increase value at address aaa by 1, M[aaa] := M[aaa] + 1.
  Mnemonic: INC aaa
  Machine code: 01aaa
  Addressing: direct
  Old value at address 0107 as bits: 00102
  Old value at address 0107 as int: +0102
  New value at address 0107 as bits: 00103
  New value at address 0107 as int: +0103
  Registers:
  IR = 01108
  BP = 9999
  SP = 9999
   A = 10007
  IP = 139
  Flags:
  zero     = False
  negative = False
  
  Description: Increase value at address aaa by 1, M[aaa] := M[aaa] + 1.
  Mnemonic: INC aaa
  Machine code: 01aaa
  Addressing: direct
  Old value at address 0108 as bits: 00105
  Old value at address 0108 as int: +0105
  New value at address 0108 as bits: 00106
  New value at address 0108 as int: +0106
  Registers:
  IR = 02110
  BP = 9999
  SP = 9999
   A = 10007
  IP = 140
  Flags:
  zero     = False
  negative = False
  
  Description: Decrease value at address aaa by 1, M[aaa] := M[aaa] - 1.
  Mnemonic: DEC aaa
  Machine code: 02aaa
  Addressing: direct
  Old value at address 0110 as bits: 00002
  Old value at address 0110 as int: +0002
  New value at address 0110 as bits: 00001
  New value at address 0110 as int: +0001
  Registers:
  IR = 60130
  BP = 9999
  SP = 9999
   A = 10007
  IP = 141
  Flags:
  zero     = False
  negative = False
  
  Description: Unconditional branch to instruction located at address aaaa.
  Mnemonic: BRA aaaa
  Machine code: 6aaaa
  Addressing: direct
  Address: 0130
  Registers:
  IR = 10110
  BP = 9999
  SP = 9999
   A = 10007
  IP = 130
  Flags:
  zero     = False
  negative = False
  
  Description: Copy value from memory at address aaaa to accumulator, A := M[aaaa].
  Mnemonic: CPA aaaa
  Machine code: 1aaaa
  Addressing: direct
  Value at address 0110: 00001
  Value in accumulator as bits: 00001
  Value in accumulator as int: +0001
  Registers:
  IR = 80142
  BP = 9999
  SP = 9999
   A = 00001
  IP = 131
  Flags:
  zero     = False
  negative = False
  
  Description: Conditional branch to instruction located at address aaaa if value stored in accumulator is equal to zero.
  Mnemonic: BRZ aaaa
  Machine code: 8aaaa
  Addressing: direct
  Address: 0142
  Value in accumulator: 00001
  Value in accumulator is not equal to zero
  Registers:
  IR = 95100
  BP = 9999
  SP = 9999
   A = 00001
  IP = 132
  Flags:
  zero     = False
  negative = False
  
  Description: Copy value from memory at address given in memory at address aaaaa to accumulator, A := M[M[aaaaa]].
  Mnemonic: CPA [aaaaa]
  Machine code: 95100 aaaaa
  Addressing: indirect, two byte length
  Value: 00003
  Value in accumulator as bits: 00003
  Value in accumulator as int: +0003
  Registers:
  IR = 95500
  BP = 9999
  SP = 9999
   A = 00003
  IP = 134
  Flags:
  zero     = False
  negative = False
  
  Description: Multiply value from accumulator by value from memory at address given in memory at address aaaaa, A := A * M[M[aaaaa]].
  Mnemonic: MUL [aaaaa]
  Machine code: 95500 aaaaa
  Addressing: indirect, two byte length
  Value as bits: 10001
  Value as int: -0001
  Value in accumulator as bits: 10003
  Value in accumulator as int: -0003
  Registers:
  IR = 30109
  BP = 9999
  SP = 9999
   A = 10003
  IP = 136
  Flags:
  zero     = False
  negative = True
  
  Description: Add value at specified address aaaa to accumulator. Result is stored in accumulator, A := A + M[aaaa].
  Mnemonic: ADD aaaa
  Machine code: 3aaaa
  Addressing: direct
  Address: 0109
  Value at address 0109 as bits: 10007
  Value at address 0109 as int: -0007
  Value in accumulator as bits: 10010
  Value in accumulator as int: -0010
  Registers:
  IR = 20109
  BP = 9999
  SP = 9999
   A = 10010
  IP = 137
  Flags:
  zero     = False
  negative = True
  
  Description: Copy value from accumulator to memory at address aaaa, M[aaaa] := A.
  Mnemonic: STO aaaa
  Machine code: 2aaaa
  Addressing: direct
  Store at address 0109 value: 10010
  Registers:
  IR = 01107
  BP = 9999
  SP = 9999
   A = 10010
  IP = 138
  Flags:
  zero     = False
  negative = True
  
  Description: Increase value at address aaa by 1, M[aaa] := M[aaa] + 1.
  Mnemonic: INC aaa
  Machine code: 01aaa
  Addressing: direct
  Old value at address 0107 as bits: 00103
  Old value at address 0107 as int: +0103
  New value at address 0107 as bits: 00104
  New value at address 0107 as int: +0104
  Registers:
  IR = 01108
  BP = 9999
  SP = 9999
   A = 10010
  IP = 139
  Flags:
  zero     = False
  negative = False
  
  Description: Increase value at address aaa by 1, M[aaa] := M[aaa] + 1.
  Mnemonic: INC aaa
  Machine code: 01aaa
  Addressing: direct
  Old value at address 0108 as bits: 00106
  Old value at address 0108 as int: +0106
  New value at address 0108 as bits: 00107
  New value at address 0108 as int: +0107
  Registers:
  IR = 02110
  BP = 9999
  SP = 9999
   A = 10010
  IP = 140
  Flags:
  zero     = False
  negative = False
  
  Description: Decrease value at address aaa by 1, M[aaa] := M[aaa] - 1.
  Mnemonic: DEC aaa
  Machine code: 02aaa
  Addressing: direct
  Old value at address 0110 as bits: 00001
  Old value at address 0110 as int: +0001
  New value at address 0110 as bits: 00000
  New value at address 0110 as int: 00000
  Registers:
  IR = 60130
  BP = 9999
  SP = 9999
   A = 10010
  IP = 141
  Flags:
  zero     = True
  negative = False
  
  Description: Unconditional branch to instruction located at address aaaa.
  Mnemonic: BRA aaaa
  Machine code: 6aaaa
  Addressing: direct
  Address: 0130
  Registers:
  IR = 10110
  BP = 9999
  SP = 9999
   A = 10010
  IP = 130
  Flags:
  zero     = True
  negative = False
  
  Description: Copy value from memory at address aaaa to accumulator, A := M[aaaa].
  Mnemonic: CPA aaaa
  Machine code: 1aaaa
  Addressing: direct
  Value at address 0110: 00000
  Value in accumulator as bits: 00000
  Value in accumulator as int: 00000
  Registers:
  IR = 80142
  BP = 9999
  SP = 9999
   A = 00000
  IP = 131
  Flags:
  zero     = True
  negative = False
  
  Description: Conditional branch to instruction located at address aaaa if value stored in accumulator is equal to zero.
  Mnemonic: BRZ aaaa
  Machine code: 8aaaa
  Addressing: direct
  Address: 0142
  Value in accumulator: 00000
  Value in accumulator is equal to zero
  Registers:
  IR = 00000
  BP = 9999
  SP = 9999
   A = 00000
  IP = 142
  Flags:
  zero     = True
  negative = False
  
  Description: Stop the cpu.
  Mnemonic: HLT
  Machine code: 00000
  ```

- **Step 19: see memory state at a given addresses**

  Verify result. You multiply `[1,2,3]` by `[-3,-2,-1]` so the result should be `1 * (-3) + 2 * (-2) + 3 * (-1) = (-3) + (-2) + (-3) = -10`:

  ```
  > -show -memory 109-110
  M[0109] = 10010
  M[0110] = 00000
  ```

- **Step 20: exit from VSC**

  ```    
  > -exit
  ```
    
  Exit from VSC.