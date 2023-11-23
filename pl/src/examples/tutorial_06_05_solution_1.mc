; vsc = 1.0
; W pierwszym wierszu pliku zawsze jest informacja o wersji VSC (VSCA) w jakiej
; dany kod jest napisany.
                  ; .data 10      ; Rozpoczęcie umieszczania danych od adresu 10.
                  
                  ; Wektor danych
0000    00008     ;v: 8
0001    00005     ;   5
0002    00007     ;   7
0003    00009     ;   9
0004    00002     ;   2
0005    00004     ;   4
0006    00003     ;   3
0007    00001     ;   1

                  ; Indeksy
0020    00002     ;i0:   2
0021    00005     ;i1:   5
0022    00007     ;i2:   7

0026    00000     ;res   0

;   Język
;   maszynowy       Assembler
; Adres   Wartość   Instrukcja                  Komentarz
                  ; .code 30                  ; Rozpoczęcie umieszczania kodu od adresu 30.

0030    94120     ; CPA [20]
0031    94321     ; ADD [21]
0032    94322     ; ADD [22]
0033    20026     ; STO  26
0034    00000     ; end:  HLT