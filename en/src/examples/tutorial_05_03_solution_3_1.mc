; vsc = 1.0
; W pierwszym wierszu pliku zawsze jest informacja o wersji VSC (VSCA) w jakiej
; dany kod jest napisany.
; Program znajdujący najmniejszą spośród 4 liczb.
; Proponowane rozwiązanie działa dla dowolnego ciągu liczb o długości większej
; lub równej 2. Główna idea polega na wywoływaniu funkcji która znajduje minimum
; z dwóch wartości. Dla ciągu czterach (4) liczb: a,b,c,d:
; iteracja 1: t = min(a,b)
; iteracja 2: t = min(t,c)
; iteracja 3: t = min(t,d)
; Rozwiązanie to nie korzysta ze stosu.
; Pierwsza z liczb znajduje się pod adresem 10 a następne kolejno z nią.
; Liczba liczb znajduje się pod adresem 14. 
; Wynik, wartość najmniejszej liczby z zadanego ciągu, znajduje się pod adresem 15.

;Address Value
                  ; .data 10      ; Rozpoczęcie umieszczania danych od adresu 10.
  0010    00010   ; v: 10         ; Pierwsza z liczb.
  0011    10003   ;    -3         ; Druga z liczb.
  0012    00005   ;    5          ; Kolejne liczby.
  0013    00001   ;    1          ;
  0014    00004   ; n: 4          ; Liczba liczb.
; 0015    00000   ; result: ?     ; Wynik = min(v[1], v[2],..., v[n])
                                  ; Uwaga do linii powyżej:
                                  ; W kodzie maszynowym nie trzeba pisać '0015    00000'
                                  ; czyli nadawać wartości początkowej, gdyż podczas wykonania
                                  ; i tak z tej wartości nie będziemy korzystać i zostanie ona
                                  ; nadpisana. Gdyby były jeszcze inne dane, to należy je wpisywać
                                  ; z pominięciem adresu 0012, np. od adresu 0013.
; 0016    00000   ; a: ?          ; Adres pierwszego argumentu funkcji minimum.
; 0017    00000   ; t: ?          ; Wartość pośredniego, tymczasowego, wyniku funkcji minimum
                                  ; i jednocześnie drugi argument funkcji minimum.

;   Język
;   maszynowy       Assembler
; Adres   Wartość   Instrukcja             Komentarz
                  ; .code 20             ; Rozpoczęcie umieszczania kodu od adresu 20.

                                         ; Inicjalizacja - początek.
  0020    02014   ;          DEC n       ; Zmniejsz wartość pod adresem n o 1 ponieważ
                                         ; dla n liczb trzeba wykonać n-1 porównań
  0021    10010   ;          CPA v       ; Kopiuj wartość spod adresu v do akumulatora.
  0022    20017   ;          STO t       ; Zapisz wartość z akumulatora pod adresem t.
  0023    93100   ;          CPA (v)     ; Kopiuj wartość v do akumulatora.
  0024    00010                          ; Zgodnie z listą rozkazów jeśli v jest większe
                                         ; lub równe 10 wówczas należy tę wartość
                                         ; kodować w kolejnym bajcie.
  0025    92301   ;          ADD (1)     ; Do wartości w akumulatorze dodaj wartość 1.
  0026    20016   ;          STO a       ; Zapisz wartość z akumulatora pod adresem a.
                                         ; Inicjalizacja - koniec.

                                         ; Rozpoczęcie petli.
  0027    10014   ; loop:    CPA n       ; Kopiuj wartość spod adresu n do akumulatora.
  0028    80033   ;          BRZ end     ; Jeśli wartość w akumulatorze jest równa zero to
                                         ; skocz pod etykietę 'end'.
  0029    60036   ;          BRA minimum ; Skok bezwarunkowy pod etykietę 'minimum' - wywołanie
                                         ; funkcji.
                                         ; Argumenty dla funkcji są pod adresem a oraz t.
  0030    02014   ; return:  DEC n       ; Zmniejsz wartość pod adresem n o 1.
  0031    01016   ;          INC a       ; Zwiększ wartość pod adresem a o 1. Oznacza to
                                         ; przesunięcie indeksu na kolejny element do porównania.
  0032    60027   ;          BRA loop    ; Skok bezwarunkowy pod etykietę 'loop'.
  0033    10017   ; end:     CPA t       ; Kopiuj wartość spod adresu t do akumulatora.
                                         ; W tym momencie pod adresem t powinien już
                                         ; znajdować się wynik.
  0034    20015   ;          STO result  ; Zapisz wartość z akumulatora pod adresem result.
  0035    00000   ;          HLT         ; Zatrzymaj procesor.


                                         ; Kod funkcji.
  0036    94116   ; minimum: CPA [a]     ; Kopiuj wartość spod adresu wskazanego przez wartość
                                         ; pod adresem a do akumulatora.
  0037    40017   ;          SUB t       ; Odejmij od akumulatora wartość spod adresu t.
                                         ; Teraz w akumulatorze jest wartość [a]-t.
  0038    70040   ;          BRN min_a   ; Jeśli wartość w akumulatorze jest ujemna to
                                         ; skocz pod etykietę 'min_a'. Wartość będzie ujemna
                                         ; gdy [a] jest MNIEJSZY od t.
  0039    60042   ;          BRA end     ; Skok nie nastąpił, zatem min([a],t) = t.
                                         ; Skok bezwarunkowy pod etykietę 'end'.
  0040    94116   ; min_a:   CPA [a]     ; Skok nastąpił, zatem min([a],t) = [a].
                                         ; Kopiuj wartość spod adresu a do akumulatora.
  0041    20017   ;          STO t       ; Zapisz zawartość akumulatora, czyli min([a],t) = [a]
                                         ; pod adresem t.
  0042    60030   ; end:     BRA return  ; Zakończ funkcję wykonując skok bezwarunkowy bezpośrenio
                                         ; za miejsce wywołania, tj. pod etykietę 'return'.
