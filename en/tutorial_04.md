# Topic
Very Simple Computer (VSC) programming -- stack

**Topics discussed**
As given above.

# Improvements, part IV: the stack 

In computer science, a stack or LIFO (*last in, first out*) is an abstract data type that serves as a collection of elements, with two principal operations:

- **push** -- adds an element to the collection;
- **pop** -- removes the last element that was added.

The term LIFO stems from the fact that, using these operations, the last element "popped off" a stack in series of pushes and pops is the first element that was pushed in the sequence. This is equivalent to the requirement that the *push* and *pop* operations occur only at one end of the structure, referred to as the **top of the stack**. The nature of the *pop* and *push* operations means that stack elements have a natural order. Elements are removed from the stack in the reverse order to the order of their addition. Therefore, the lower elements are those that have been on the stack the longest.

If the stack is full and does not contain enough space to accept an entity to be pushed, the stack is then considered to be in an **overflow state** -- which results a well known runtime message: **Stack Overflow**. 

Notice one very important thing: stack in computers growth in direction of lower addresses. It means that if element `y` is above `x` in a stack the address of `y` is lower than `x`:

```
higher addresses

99999
...
xxxxx   x <-- base of the stack
xxxxx-1 ..
xxxxx-2 ..
xxxxx-3 y <-- top of the stack
...       
00000

lower addresses

direction of stack growth
```

To keep things working you need two new registers in your CPU:

- `BP` -- to keep information about the address of the **base of the stack**,
- `SP` -- to keep information about the address of the **top of the stack**.  It is used to indicate the location of the **last item put onto the stack**.

with instructions `PUSH` and `POP`.

When you **put** something **onto** the stack (**PUSH** onto the stack), the SP is **decremented before** the item is placed on the stack. When you take something **off** of the stack (**PULL** from the stack), the SP is **incremented after** the item is pulled from the stack.

For example:

```
PUSH       ; Add an element from accumulator to the stack.
PUSH 5     ; Add an element from address 5 to the stack.
PUSH (5)   ; Add value 5 to the stack.
POP        ; Removes the last element that was added to the stack
           ; and put it into accumulator.
POP 5      ; Removes the last element that was added to the stack
           ; and put it at address 5.            
```

The notation:

- `BP` - means a reference to the current value of `BP`; it is equall to the address of the base of stack. For example:

	```
	PUSH BP   ; Save the current value of BP on the stack.
	```
	
- `[BP]` - means a value at address stored in `BP` register. For example:

	```
	PUSH [BP] ; Save the value at address stored in BP register
	          ; on the stack.
	```
	
Similarly you treat `SP` register.


## When might this be useful?
Stack can be used to transfer data between different parts of your code without paying to much attention on addresses of those data.

### Example 1
Imagine that you have a code calculating something very complex. During calculations you have some intermediate results, say five intermediate results. What you can do?

[comment]: # (Explicit is directly stated and spelled out.)
[comment]: # (Implicit is, “implied or understood though not plainly or directly expressed.”)

### Solution 1.1 -- explicite addresses
```
.data XX        ; Specify the address of the first data
...             ; Some data required by program
resInterm1  ?   ; Intermediate result 1
resInterm2  ?   ; Intermediate result 2
resInterm3  ?   ; Intermediate result 3
resInterm4  ?   ; Intermediate result 4
resInterm5  ?   ; Intermediate result 5

.code YY        ; Specify the address of the first instruction
...             ; Some code
STO resInterm1  ;
...
STO resInterm2  ;
...
STO resInterm3  ;
...
STO resInterm4  ;
...
STO resInterm5  ;
...
CPA resInterm1  ;
ADD resInterm2  ;
ADD resInterm3  ;
ADD resInterm4  ;
ADD resInterm5  ;
STO result      ;
```

### Solution 1.2 -- implicite addresses with stack usage
```
.data XX        ; Specify the address of the first data
...             ; Some data required by program

.base ZZ        ; Specify the address of the base of stack

.code YY        ; Specify the address of the first instruction
...             ; Some code
PUSH            ;
...
PUSH            ;
...
PUSH            ;
...
PUSH            ;
...
PUSH            ;
...
POP             ; Load 5th intermediate result into accumulator
ADD [SP]        ; Add 4th intermediate result
ADD [SP+1]      ; Add 3rd intermediate result
ADD [SP+2]      ; Add 2nd intermediate result
ADD [SP+3]      ; Add 1st intermediate result
STO result      ; Save result
CPA SP          ; Load current stack pointer to accumulator
ADD (4)         ; Move stack pointer 4 bytes back
STO SP          ; Update stack pointer to new value
```

### Example 2

Write a program to calculate for a given $$x$$ a value of polynomial $$P$$:

$$P(x) = ax^{3} + bx^{2}+cx + d$$

First recall solution 4.2 from lecture 1 of calculating $$a^b$$, where $$a$$ -- integer number, $$b$$ -- integer nonnegative number. Now I will present a slightly moddified version of that code:

```
Code to calculate a^b.

Assumption: both a and b are admissible; I do not check
their correctness.

.data XX
base:   a
power:  b
resPow: 1

.code YY
powersubprogram:   
        CPA  (1)     ; Set A=1
loop:   DEC  power   ; Decrease power by one
        BRNF end     ; Jump to end if power<0
        MUL  base    ; Multiply A by a
        BRA  loop    ; End loop - jump to the begining of the loop
end:    STO  resPow  ; Save A as resPow
```

### Solution 2.1 -- in *spaghetti coding* style

Now you are ready to implement a final solution.

```
.data 0

; Local variables for the main code
result:  0    ; Result
x:       x    ; For example x = 2
a:       a    ; For example a = 3
b:       b    ; For example b = 4
c:       c    ; For example c = 5
d:       d    ; For example d = 6

; Local variables for power subprogram
base:   a
power:  b
resPow: 1
ret:    ?

.code 10
        CPA x       ; Prepare local data for subprogram
        STO base    ; This is common for all components
        
        CPA (3)
        STO power
        CPA (ret1)  ; Prepare return address from subprogram
        STO ret
        BRA powersubprogram ; Call subprogram
ret1:   CPA a
        MUL resPow
        ADD result  ; This is not necessary but I add it here
                    ; to have similar code for every degree
        STO result
        
        CPA (2)     ; Prepare local data for subprogram
        STO power
        CPA (ret2)  ; Prepare return address from subprogram
        STO ret
        BRA powersubprogram ; Call subprogram
ret2:   CPA b
        MUL resPow
        ADD result
        STO result
        
        CPA (1)     ; Prepare local data for subprogram
        STO power
        CPA (ret3)  ; Prepare return address from subprogram
        STO ret
        BRA powersubprogram ; Call subprogram
ret3:   CPA c
        MUL resPow
        ADD result
        STO result
        
        CPA (0)     ; Prepare local data for subprogram
        STO power
        CPA (ret4)  ; Prepare return address from subprogram
        STO ret
        BRA powerSubprogram ; Call subprogram
ret4:   CPA d
        MUL resPow
        ADD result
        STO result
        HLT
    
powerSubprogram:   
        CPA (1)     ; Set A=1
loop:   DEC power   ; Decrease power by one
        BRNF end    ; Jump to end if power<0
        MUL base    ; Multiply A by a
        BRA loop    ; End loop - jump to the begining of the loop
end:    STO resPow  ; Save A as resPow
        BRA ret     
```

This solution is much longer than solution 3.1 or 3.1 from lecture 1. However current solution is much more promissing -- as you can see a lot of code is repeated and can be removed if you enclose this code in a loop. Moreover now it can be easily extended to calculate value of a polynomial of any given degree.

### Solution 2.2 -- almost perfect, with a stack

To make this code more universal you can use a stack and rewrite subprogram:

```
.base 50

.data 0

; Local variables for the main code
result:  0    ; Result
comp:    4    ; Number of components in formula P

; Local variables for power subprogram
base:   ?
power:  ?
coef:   ?
resSub: ?

.code 10
                      ; Prepare local data for subprogram
          CPA x       ; Put an exact value as x
          STO base    ; This is common for all components
                      
                      ; Put data onto stack
          PUSH (3)    ; Put here a power for coef. a
          PUSH a      ; Put here an exact value as coef. a
          PUSH (2)    ; Put here a power for coef. b
          PUSH b      ; Put here an exact value as coef. b
          PUSH (1)    ; Put here a power for coef. c
          PUSH c      ; Put here an exact value as coef. c
          PUSH (0)    ; Put here a power for coef. d
          PUSH d      ; Put here an exact value as coef. d
                      ; Stack is ready
        
loopMain: DEC comp    
          BRNF stop
        
          BRA powerSubprogram ; Call subprogram   
ret:      CPA result
          ADD resSub
          STO result
          BRA loopMain
          
stop:     HLT          

powerSubprogram:   
        CPA (1)     ; Set A=1
        POP coef    ;
        POP power   ;
        
loop:   DEC power   ; Decrease power by one
        BRNF end    ; Jump to end if power<0
        MUL base    ; Multiply A by a
        BRA loop    ; End loop - jump to the begining of the loop
end:    MUL coef    ; Multiply base^power by coef 
        STO resSub  ; Save A as resPow
        BRA ret 
```

### !!! Another solution of an example 2 -- much more general but not complete; just an idea. This should be considered BEFORE solution with a stack to understand the power of the stack. !!!

General solution without a stack would be more complicated:

```
.data 0
; Local variables for the main code
coef:      A   ; Coefficient A -- put an exact value here
           B
           C
           D
pow:      pA   ; Power for coef. A -- put an exact value here
          pB
          pC
          pD
varX:      X   ; Put an exact value as X

coefI:  coef   ; Put as value of coef. iterator address of A
powI:    pow   ; Put as value of power iterator address of pA
result:    0 
counter:   4   ; Indicate the number of components

; Local variables for power subprogram

base:      0
power:     0
resPow:    0

.code 20

; Main
begin: CPA varX       ; Prepare local data for subprogram
       STO base
       CPA [powI]
       STO power
       BRA powersubprogram ; Call subprogram
loop:  CPA resT       ; return from subprogram - we have a result of base^pow
       MUL [coefI]
       INC powI
       INC coefI
       ADD result
       STO result
       DEC counter
       CPA counter
       BRN end
       BRA begin
end:   HLT

;subprogram
powerBegin:   CPA (1)
              STO resT
powerLoop:    CPA power
              BRZ powerEnd
              DEC power
              CPA resT
              MUL base
              STO resT
              BRA powerLoop
powerEnd:     BRA loop
```

