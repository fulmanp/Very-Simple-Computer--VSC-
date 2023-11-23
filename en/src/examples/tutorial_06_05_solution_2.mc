; vsc = 1.0
; W pierwszym wierszu pliku zawsze jest informacja o wersji VSC (VSCA) w jakiej
; dany kod jest napisany.
                  ; .data 10      ; Rozpoczęcie umieszczania danych od adresu 10.
                  
                  ; Wektor danych
0010    00008     ;v: 8
0011    00005     ;   5
0012    00007     ;   7
0013    00009     ;   9
0014    00002     ;   2
0015    00004     ;   4
0016    00003     ;   3
0017    00001     ;   1

                  ; Indeksy
0020    00002     ;idx:   2
0021    00005     ;       5
0022    00007     ;       7
0023    10001     ;       -1        ; Nie ma elementu o takim indeksie. To oznacza koniec listy indeksów.
0024    00000     ; addr: 0
0025    00000     ; res:  0
0026    00020     ; i:    20

;   Język
;   maszynowy       Assembler
; Adres   Wartość   Instrukcja                  Komentarz
                  ; .code 30                  ; Rozpoczęcie umieszczania kodu od adresu 30.

0030    94126     ; loop: CPA  [i]            ; Wczytaj indeks znajdujący się pod adresem wskazanym przez adres i.
0031    70040     ;       BRN end             ; Skok na koniec po natrafieniu na idx=-1.
0032    93300     ;       ADD (10)            ; +10 aby index+10 wskazywało na właściwą składową wektora.
0033    00010     ;                           ; Na dwóch bajtach, bo aby zapisać +10 trzeba 3 pozycji.
0034    20024     ;       STO addr            ; Zapisz aby można było użyć adresowania pośredniego.
0035    10025     ;       CPA res             ; Wczytaj dotychczasowy wynik.
0036    94324     ;       ADD [addr]          ; Dodaj wartość z adresu wskazanego przez adres addr.
0037    20025     ;       STO res             ; Zapisz dotychczasowy wynik.
0038    01026     ;       INC i               ; Zwiększ wartość i o 1 aby była równa kolejnemu adresowi.
0039    60030     ;       BRA loop            ; 
0040    00000     ; end:  HLT