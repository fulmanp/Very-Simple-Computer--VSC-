;Address Value Comment
0020    10010 ; Copy the value at address 0010 to the accumulator.
0021    40011 ; Subtract the value at address 0011 from the accumulator.
              ; Now there is an x-y value in the accumulator.
0022    70025 ; If the value in the accumulator is negative then
              ; jump at address 0025. The value will be negative
              ; when x is LESS than y.
0023    10011 ; The jump did not occur, so min(x,y) = y.
              ; Copy the value at address 0011 to the accumulator.
0024    60026 ; Unconditional jump at the address 0026.
0025    10010 ; The jump occurred, so min(x,y) = x.
              ; Copy the value at address 0010 to the accumulator.
0026    20012 ; Write the contents of the accumulator, i.e. min(x,y)
              ; at address 0012.
0027    00000 ; Stop the processor.