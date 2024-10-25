; vsc = 1.0
; W pierwszym wierszu pliku zawsze jest informacja o wersji VSC (VSCA) w jakiej
; dany kod jest napisany.
;
; Program znajdujący mniejszą z dwóch zadanych liczb.
; Pierwsza liczba znajduje się pod adresem 10.
; Druga liczba znajduje się pod adresem 11.
; Wynik, mniejsza z dwóch liczb, znajleźć się pod adresem 12.

;Address Value
                  ; .data 10      ; Rozpoczęcie umieszczania danych od adresu 10.
  0010    00005   ; x: 5          ; x - pierwsza liczba.
  0011    10008   ; y: -8         ; y - druga liczba.
; 0012    00000   ; r: ?          ; Wynik = min(x,y).
                                  ; Uwaga do linii powyżej:
                                  ; W kodzie maszynowym nie trzeba pisać '0012    00000'
                                  ; czyli nadawać wartości początkowej, gdyż podczas wykonania
                                  ; i tak z tej wartości nie będziemy korzystać i zostanie ona
                                  ; nadpisana. Gdyby były jeszcze inne dane, to należy je wpisywać
                                  ; z pominięciem adresu 0012, np. od adresu 0013.

;   Język
;   maszynowy       Assembler
; Adres   Wartość   Instrukcja             Komentarz
                  ; .code 20             ; Rozpoczęcie umieszczania kodu od adresu 20.
0020      10010   ;          CPA x       ; Kopiuj wartość spod adresu x do akumulatora.
0021      40011   ;          SUB y       ; Odejmij od akumulatora wartość spod adresu y.
                                         ; Teraz w akumulatorze jest wartość x-y.
0022      70025   ;          BRN min_x   ; Jeśli wartość w akumulatorze jest ujemna to
                                         ; skocz pod etykietę 'min_x'. Wartość będzie ujemna
                                         ; gdy x jest MNIEJSZY od y.
0023      10011   ;          CPA y       ; Skok nie nastąpił, zatem min(x,y) = y.
                                         ; Kopiuj wartość spod adresu y do akumulatora.
0024      60026   ;          BRA finish  ; Skok bezwarunkowy pod etykietę 'finish'.
0025      10010   ; min_x:   CPA x       ; Skok nastąpił, zatem min(x,y) = x.
                                         ; Kopiuj wartość spod adresu x do akumulatora.
0026      20012   ; finish:  STO r       ; Zapisz zawartość akumulatora, czyli min(x,y)
                                         ; pod adresem r.
0027      00000   ;          HLT         ; Zatrzymaj procesor.
