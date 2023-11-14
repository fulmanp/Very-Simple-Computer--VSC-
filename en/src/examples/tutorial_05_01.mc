; vsc = 1.0
; The first line of the file always contains information about the VSC (VSCA)
; version the code is written.
;
; A program that finds the smaller of two given numbers.
; The first number is at address 10.
; The second number is at address 11.
; The result, the smaller of the two numbers, will be at address 12.

;Address Value
                  ; .data 10      ; Start placing data from address 10.
  0010    00005   ; x: 5          ; x - first number.
  0011    10008   ; y: -8         ; y - second number.
; 0012    00000   ; r: ?          ; Result = min(x,y).
                                  ; Note to the line above:
                                  ; In machine code you don't have to write '0012 00000'
                                  ; that is, give an initial value, because during execution
                                  ; you will not use this value anyway and you will
                                  ; overwrite it. If there is any other data, you provide it
                                  ; omitting address 0012, e.g. from address 0013.

;   Machine
;   Language        Assembler
; Address Value     Instruction            Comment
                  ; .code 20             ; Start placing the code at address 20.
0020      10010   ;          CPA x       ; Copy the value from address x to the accumulator.
0021      40011   ;          SUB y       ; Subtract the value at address y from the accumulator.
                                         ; Now there is an x-y value in the accumulator.
0022      70025   ;          BRN min_x   ; If the value in the accumulator is negative then
                                         ; branch (jump) to the 'min_x' label. The value will be
                                         ; negative when x is LESS than y.
0023      10011   ;          CPA y       ; The jump did not occur, so min(x,y) = y.
                                         ; Copy the value from address y to the accumulator.
0024      60026   ;          BRA finish  ; Unconditional jump to the 'finish' label.
0025      10010   ; min_x:   CPA x       ; The jump occurred, so min(x,y) = x.
                                         ; Copy the value at address x to the accumulator.
0026      20012   ; finish:  STO r       ; Write the contents of the accumulator, i.e. min(x,y)
                                         ; at address r.
0027      00000   ;          HLT         ; Stop the processor.
