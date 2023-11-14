; vsc = 1.0
; W pierwszym wierszu pliku zawsze jest informacja o wersji VSC (VSCA) w jakiej
; dany kod jest napisany.
; Program liczy iloczyn skalarny dwóch wektorów v1 i v2 o długości n.
; Pierwszy wektor znajduje się pod adresem 10 (pod adresem 10 znajduje się jego
; pierwsza składowa; druga pod adresem 11, trzecia pod adresem 12 itd).
; Drugi wektor znajduje się pod adresem 20.
; Pod adresem 4 znajduje się wartość określająca długość wektorów. 
; Wynik, wartość iloczynu skalarnego dwóch wektorów, znajduje się pod adresem 3.

;Address Value
                  ; .data 1       ; Rozpoczęcie umieszczania danych od adresu 1.
  0001    00010   ; idx1: 10      ; Adres pod którym znajduje się pierwsza składowa wektora v1.
  0002    00020   ; idx2: 20      ; y - druga liczba.
  0003    00000   ; result: 0     ; Wynik = dotProduct(v1, v2).
  0004    00010   ; n: 10         ; Długość wektorów.
                  ; ?[5]          ; Obszar (blok) pięciu (5) bajtów "wypełnienia" zaczynający się pod 
                                  ; adresem 00005 a kończący się pod adresem 00009. Bezpośrednio
                                  ; za nim, a więc od adresu 00010, umieszczone będą kolejne dane.
                                  ; Ze względu na to, że w kodzie maszynowym używamy bezpośrednich
                                  ; adresów, nie musimy wówczas tego bloku tam rezerwowac.
  0010    00001   ; v1: 1         ; Pierwsza składowa wektora v1
  0011    10002   ;    -2         ; Druga składowa wektora v1
  0012    00003   ;     3         ; Kolejne składowe wektora v1
  0013    00004   ;     4
  0014    00005   ;     5
  0015    00006   ;     6
  0016    00007   ;     7
  0017    10008   ;    -8
  0018    00009   ;     9
  0019    00010   ;     10
  0020    10010   ; v2: -10       ; Pierwsza składowa wektora v2
  0021    10009   ;    -9         ; Druga składowa wektora v2
  0022    00008   ;     8         ; Kolejne składowe wektora v2
  0023    00007   ;     7
  0024    10006   ;    -6
  0025    00005   ;     5
  0026    00004   ;     4
  0027    00003   ;     3
  0028    00002   ;     2
  0029    00001   ;     1

;   Język
;   maszynowy       Assembler
; Adres   Wartość   Instrukcja             Komentarz
                  ; .code 30             ; Rozpoczęcie umieszczania kodu od adresu 20.
0030      10004   ; loop:    CPA n       ; Kopiuj wartość spod adresu n do akumulatora.
0031      80040   ;          BRZ end     ; Jeśli wartość w akumulatorze jest równa zero to
                                         ; skocz pod etykietę 'end'.
0032      94101   ;          CPA [idx1]  ; Kopiuj wartość spod adresu będącego wartością
                                         ; znajdującą się pod adresem idx1 do akumulatora.
0033      94502   ;          MUL [idx2]  ; Pomnóż wartość akumulatora przez wartość spod
                                         ; adresu będącego wartością znajdującą się pod
                                         ; adresem idx2.
0034      30003   ;          ADD result  ; Do wartości w akumulatorze dodaj wartość spod
                                         ; adresu result.
0035      20003   ;          STO result  ; Zapisz wartość z akumulatora pod adresem result.
0036      01001   ;          INC idx1    ; Zwiększ wartość pod adresem idx1 o 1.
0037      01002   ;          INC idx2    ; Zwiększ wartość pod adresem idx2 o 1.
0038      02004   ;          DEC n       ; Zmniejsz wartość pod adresem n o 1.
0039      60030   ;          BRA loop    ; Skok bezwarunkowy pod etykietę 'loop'.
0040      00000   ; end:     HLT         ; Zatrzymaj procesor.
