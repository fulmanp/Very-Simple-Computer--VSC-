;Label     Instruction
.data 101           ; Start data block at address 0
v1:        1        ; First component of vector 1
           2        ;
           3        ; Last component of vector 1
v2:        -3       ; First component of vector 2
           -2
           -1       ; Last component of vector 2
a_v1:      v1       ; Address of the first component of vector 1
a_v2:      v2       ; Address of the first component of vector 2
result:    0        ; Result
vec_len:   3        ; n - length of vector

.code 130           ; Start code block at address 130

begin:     CPA vec_len
           BRZ end
           CPA [a_v1]
           MUL [a_v2]
           ADD result
           STO result
           INC a_v1
           INC a_v2
           DEC vec_len
           BRA begin
end:       HLT