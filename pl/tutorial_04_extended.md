# Topic
Very Simple Computer (VSC) programming -- function call (function stack).

**Topics discussed**
As given above.

# Improvements, part V -- function stack frame

The solution you saw in previous part related to calculating value of a polynomial with a stack (excercise 2, solution 2.2) is almost perfect with the exception of one unsolved problem: *how do you know to which address should you return?* The problem is that you assumed that called function *knows* which function or part of the code was a caller -- in your case, "main" code (see `loopMain` label in that solution) -- and you hardcoded this value in your function (see `ret` label and `BRA ret` in `powerSubprogram`. What if you try to call function from completely different place, for example other function or you try to call it multiple times from various "places"? Always you will return to "main" code which wouldn't be correct. 

That is why functions (subrutines) are frequently set up with a **stack frame** to know where to return and to allow access to both function parameters, and automatic function variables. The idea behind a stack frame is that each subroutine can act independently of its location on the stack, and each subroutine can act as if it is the top of the stack. In other words, each subrutine can act as it would be the only subrutine in a code.

When a function is called, a new stack frame is created at the current `SP` location. A stack frame acts like a *partition* on the stack. All items from previous functions are higher up on the stack, and should not be modified. Each current function has access to the remainder of the stack, from the stack frame until the end of the stack page.

So how it works? When you want to call a function you have to perform a following sequence of instruction

```
...
CALL function ; Jump to 'function' address and push on the stack
              ; address of the next instruction
XXX           ; Next instruction(s) 
...
function:
              ; Prepare stack to be safely use in your function
     PUSH BP  ; Save the current value of BP on the stack
              ; Move SP to BP (set BP as equal to SP)
     CPA SP   ; Read current top of the stack
     STO BP   ; BP now points to the top of the stack
     ...
     ...      ; Exact function code starts
     ...      ; Do what you want to do
     ...
              ; Restore the stack
              ; Move BP to SP (set SP as equal to BP)
     CPA BP   ; Read current base of the stack
     STO SP   ; SP now points to the top of the stack
     POP BP   ; Restore value of BP saved at the beginning
     RET      ; Pop value from the stack and jump to this address
```

In the above code you have seen two new instructions:

- `CALL` -- push on the stack address of the next instruction following this `CALL` instruction;
- `RET` -- pop value from the stack and treating it as an address jump to instruction at this address.

Above sequence of instruction results in the following stack changes (you stop at the time when exact function code starts):

```
Initial   After            After            After move
stack     CALL             PUSH BP          SP to BP

BP -> A1  BP -> A1         BP -> A1                     A1
      ...       ...              ...                    ...
SP -> A2        A2               A2                     A2
          SP -> XXX Addr.        XXX Addr.              XXX Addr.
                           SP -> BP         (BP, SP) -> BP
```

Here is a representation of the stack at the time when exact function code starts:

```
Frame stack:

higher addresses

Address   Value (Meaning) 

BP + 1  (return address)
BP      (old BP value)

lower addresses

stack growth
```

When you want to call a function with some **arguments** and **local variables** very similar schema is used.

```
...
PUSH ARG_N
...
PUSH ARG_1
CALL function ; Jump to 'function' address and push on the stack
              ; address of the next instruction
XXX           ; Next instruction 
...
function:
              ; Prepare stack to be safely use in our function
     PUSH BP  ; Save the current value of BP on the stack
              ; Move SP to BP (set BP as equal to SP)
     CPA SP   ; Read current top of the stack
     STO BP   ; BP now points to the top of the stack
              ; "allocate" space for the M local variables
     CPA SP   ; Read current SP
     SUB M    ; Move SP down (allocate space for M variables)
     STO SP   ; Save SP
     ...
     ...      ; Exact function code starts     
     ...      ; Do what you want to do
     ...
              ; Restore the stack
              ; Move BP to SP (set SP as equal to BP)
     CPA BP   ; Read current base of the stack
     STO SP   ; SP now points to the top of the stack
     POP BP   ; Restore value of BP saved at the beginning
     RET N    ; Pop value from the stack and jump to this address
              ; but before the jump the stack is lowered by N
```

As you can see arguments and local variables which your function needs are pushed to the stack **before** return address. You can reference them relatively with `BP` register (see subsequent paragraph below).

One thing which should I explained to you is `RET N` instruction. This instruction *pops* `N` elements from the stack and next *jumps* to instruction just after `CALL`.

Saying the truth you don't carre about popped elements so technicaly speaking `RET N` instruction does not pop `N` element from the stack but simply *move* stack pointer by `N` to point lower elements -- the easiest way to do it is simply subtract from `SP` value `N`.

Every `RET N` instruction can be substituted by:

```
CPA SP
SUB N
STO SP
RET
```

Generaly speaking you have a following (function) frame on a stack every time you call a function (at the time when exact function code starts):

```
Frame stack:

higher addresses

Address   Value (Meaning) 

BP + 1 + N (Nth function argument)
...
BP + 1 + 1 (1st function argument)
BP + 1     (return address)
BP         (old BP value)
BP - 1     (1st local variable)
...
BP - 1 - M (Mth local variable)

lower addresses

stack growth
```

## Example

See how stack works in the following example

```
.data 0
a: 2
b: 5
wynik: 0

.code 10
start: PUSH wynik
       PUSH a
       PUSH b
       CALL dodaj
       POP wynik
       HLT
       
dodaj: 
       ; Init the stack
       PUSH BP
       CPA SP
       STO BP
     	
       ; Make some computations	
       CPA [BP + 2]
       ADD [BP + 3]
       STO [BP + 4]
       
       ; Restore the stack
       CPA BP
       STO SP
       POP BP
       
       ; Clean the stack and return to the caller
       RET 2
```
