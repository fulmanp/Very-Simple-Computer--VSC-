; vsc = 1.0
; W pierwszym wierszu pliku zawsze jest informacja o wersji VSC (VSCA) w jakiej
; dany kod jest napisany.
; Prosty program testowy wykonujący mnożenie dwóch liczb.
; Pierwsza z liczb znajduje się pod adresem 10, druga liczba pod adresem 11. 
; Wynik, wartość iloczynu liczb, znajduje się pod adresem 12.

;Address Value
                  ; .data 10      ; Rozpoczęcie umieszczania danych od adresu 10.
  0010    00005   ; x: 5          ; Pierwsza z liczb.
  0011    10007   ; y: -7         ; Druga z liczb.
; 0012    00000   ; r: ?          ; Wynik = x * y.
                                  ; Uwaga do linii powyżej:
                                  ; W kodzie maszynowym nie trzeba pisać '0012    00000'
                                  ; czyli nadawać wartości początkowej, gdyż podczas wykonania
                                  ; i tak z tej wartości nie będziemy korzystać i zostanie ona
                                  ; nadpisana. Gdyby były jeszcze inne dane, to należy je wpisywać
                                  ; z pominięciem adresu 0012, np. od adresu 0013.

;   Język
;   maszynowy       Assembler
; Adres   Wartość   Instrukcja       Komentarz
                  ; .code 20       ; Rozpoczęcie umieszczania kodu od adresu 20.
  0020    10010   ;    CPA x       ; Zmniejsz wartość pod adresem n o 1 ponieważ
  0021    50011   ;    MUL y       ; Pomnóż wartość w akumulatorze przez liczbę spod adresu y.
  0022    20012   ;    STO r       ; Zapisz wartość z akumulatora pod adresem r.
  0023    00000   ;    HLT         ; Zatrzymaj procesor.
