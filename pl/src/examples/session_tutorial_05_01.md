# Example VSC session on `tutorial_05_01.mc` file

In this example you will learn how to use VSC working on [`tutorial_05_01.mc`](tutorial_05_01.mc) file.

**Created: 2023-11-14** and **Updated: 2023-11-14**

Reading this material you may find useful to have a reference to a complete [instruction set](../instruction_set.md)

## Session steps

- **Step 1: start VSC**

	```
	MacBook-Piotr:src fulmanp$ python3 vsc.py 
	
	Welcome to VSCA (Very Simple Computer Assembler)
	Version 1.0
	Build 202311110840
	Type -h and confirm with ENTER for help.
	
	```
	
- **Step 2: load the code**

	```
	> -load tutorial_05_01.mc
	Loading program from: tutorial_05_01.mc
	```

- **Step 3: set the address of the first instruction**
	
	In this step you set the address of the first instruction VSC should execute:
	
	```
	> -startAddr 20
	Starting at address: 20
	```

- **Step 4: see memory state at a given addresses**

	Any time you want, you may see values at give addresses specified as a single number, range, list of numbers and/or ranges:


	```	
	> -show -memory 10-12
	M[0010] = 00005
	M[0011] = 00002
	M[0012] = 03728
	```
- **Step 5: execute one instruction**

    ```
    > -run -step
    Executing one instruction
    Registers:
    IP = 20
    IR = 10010
    A = None
    
    Description: Copy value from memory at address aaaa to accumulator, A := M[aaaa].
    Mnemonic: CPA aaaa
    Machine code: 1aaaa
    Addressing: direct
    Value at address 0010: 00005
    Value in accumulator as bits: 00005
    Value in accumulator as int: +0005
    ```
    
    As you can see executed instruction is `10010` and it is located at address `20`. According to **Description** field this is an instruction which copies value from memory at address `0010` to accumulator. This value is equal to `+5`, so after executing you will have `+5` in accumulator (if you interprete this as an integer; binary it is `00005`).
    
- **Step 6: repeat last command**
    
    To repeat last command, in this case `-run -step`, it is enough to press **ENTER**.
    
    ```
    > 
    Executing one instruction
    Registers:
    IP = 21
    IR = 40011
    A = 00005
    
    Description: Subtract value at specified address aaaa from accumulator. Result is stored in accumulator A := A - M[aaaa].
    Mnemonic: SUB aaaa
    Machine code: 4aaaa
    Addressing: direct
    Address: 0011
    Value at address 0011 as bits: 00002
    Value at address 0011 as int: +0002
    Value in accumulator as bits: 00003
    Value in accumulator as int: +0003
    ```
    
    Next you subtract value at address 11, which is equal to 2, from value stored in accumulator. You will get `accumulator = +5-(+2) = +3`.

- **Step 7: repeat last command**    

    ```    
    > 
    Executing one instruction
    Registers:
    IP = 22
    IR = 70025
    A = 00003
    
    Description: Conditional branch to instruction located at address aaaa if value stored in accumulator is negative.
    Mnemonic: BRN aaaa
    Machine code: 7aaaa
    Addressing: direct
    Address: 0025
    Value in accumulator: 00003
    Value in accumulator is positive
    ```
    
    If value in accumulator is negative do branch (jump) at address `25`. In this case value stored in accumulator is equal to `+3` so there is no branch and next instruction (instruction at address `23`) is fetched.

- **Step 8: repeat last command**

    ```
    > 
    Executing one instruction
    Registers:
    IP = 23
    IR = 10011
    A = 00003
    
    Description: Copy value from memory at address aaaa to accumulator, A := M[aaaa].
    Mnemonic: CPA aaaa
    Machine code: 1aaaa
    Addressing: direct
    Value at address 0011: 00002
    Value in accumulator as bits: 00002
    Value in accumulator as int: +0002
    ```
    
    Copy to accumulator value at address `11` which is equal to `-8`. This value is equal to `min(+5,+2)`.
    
- **Step 9: repeat last command**    

    ```
    > 
    Executing one instruction
    Registers:
    IP = 24
    IR = 60026
    A = 00002
    
    Description: Unconditional branch to instruction located at address aaaa.
    Mnemonic: BRA aaaa
    Machine code: 6aaaa
    Addressing: direct
    Address: 0026
    ```
    
    Make jump to skip part of code.

- **Step 10: repeat last command**

    ``` 
    > 
    Executing one instruction
    Registers:
    IP = 26
    IR = 20012
    A = 00002
    
    Description: Copy value from accumulator to memory at address aaaa, M[aaaa] := A.
    Mnemonic: STO aaaa
    Machine code: 2aaaa
    Addressing: direct
    Store at address 0012 value: 00002
    ```
    
    Copy value in accumulator at address `12` where result should be placed when the execution ends. At this moment value in accumulator is equal to `-8` (see step 8).

- **Step 11: repeat last command**

    ```
    > 
    Executing one instruction
    Registers:
    IP = 27
    IR = 00000
    A = 00002
    
    Description: Stop the cpu.
    Mnemonic: HLT
    Machine code: 00000
    ```
    
    Stop execution.

- **Step 12: repeat last command**

    ``` 
    > 
    Executing one instruction
    Program execution halted. Please do reset
    ```
    
    Last instruction halted the CPU so to execute new code you have to do `-reset` following by `-load` and `-startAddr` as you did at the beginning of this session.
    
- **Step 13: see memory state at a given addresses**

    ```
    > -show -memory 10-12
    M[0010] = 00005
    M[0011] = 00002
    M[0012] = 00002
    ```
    
    Verify if result, which is at address `12`, is qual to minimum of values stored at addresses `10` and `11` which are equal respectively to `+5` and `-8`.
    
- **Step 14: exit from VSC**

    ```    
    > -exit
    ```
    
    Exit from VSC.