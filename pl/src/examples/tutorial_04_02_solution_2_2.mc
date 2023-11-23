; vsc = 1.0
; W pierwszym wierszu pliku zawsze jest informacja o wersji VSC (VSCA) w jakiej
; dany kod jest napisany.
;
; Napisz program obliczający dla zadanej wartości zmiennej x wartość wielomianu P(x):
; P(x) = ax^{3} + bx^{2}+cx + d
; W programie przyjęto:
; x = 2
; a = -3
; b = 2
; c = 3
; d = -7
; P(x) = (-3)*8 + 2*4 + 3*2 + (-7) = -24 +8 + 6 - 7 = -17
;
;Address Value
                  ; .stack 50     ; Położenie wskaźnika podstawy stosu (BP).
                  ; .data 10      ; Rozpoczęcie umieszczania danych od adresu 10.
                  
                                  ; Zmienne dla programu głównego.
  0010    00004   ; comp: 4       ; Liczba jednomianów składowych wielomianu P.
  0011    00000   ; result: 0     ; Wynik = P(x).
                                  ; Zmienne dla podprogramu obliczającego wartość
                                  ; wyrażenia x^n.
; 0012    00000   ; base:   ?     ; Podstawa wyrażenia x^3.
; 0013    00000   ; power:  ?     ; Wykładnik wyrażenia x^3.
; 0014    00000   ; coef:   ?     ; Współycznnik jednomianu.
; 0015    00000   ; resSub: ?     ; Wynik wykonania podprogramu.

;   Język
;   maszynowy       Assembler
; Adres   Wartość   Instrukcja                  Komentarz
                  ; .code 20                  ; Rozpoczęcie umieszczania kodu od adresu 20.
                  
                                              ; Przygotowanie wartości na stosie.
                                              ; Przygotowanie danych dla podprogramu.
0020      92102   ;           CPA (2)         ; Umieść w akumulatorze wartość x.
0021      20012   ;           STO base        ; Zapisz zawartość akumulatora pod adresem 'base', a więc M[base] == x.
                                              ; załadowanie na stos współczynników i wykładników odpowiadających jednomianom.
0022      93030   ;           PUSH (3)        ; Załadowanie na stos wykładnika przy współczynniku 'a'.
0023      00003
0024      93030   ;           PUSH (-3)       ; Załadowanie na stos wartości współczynnika 'a'.
0025      10003
0026      93030   ;           PUSH (2)        ; Załadowanie na stos wykładnika przy współczynniku 'b'.
0027      00002
0028      93030   ;           PUSH (2)        ; Załadowanie na stos wartości współczynnika 'b'.
0029      00002
0030      93030   ;           PUSH (1)        ; Załadowanie na stos wykładnika przy współczynniku 'c'.
0031      00001
0032      93030   ;           PUSH (3)        ; Załadowanie na stos wartości współczynnika 'c'.
0033      00003
0034      93030   ;           PUSH (0)        ; Załadowanie na stos wykładnika przy współczynniku 'd'.
0035      00000
0036      93030   ;           PUSH (-7)       ; Załadowanie na stos wartości współczynnika 'a'.
0037      10007
                                              ; Stos gotów do obliczeń.

0038      02010   ; loopMain: DEC comp        ; Zmniejsz o 1 licznik określający liczbę składowych.
0039      90745   ;           BRNF stop       ; Skok warunkowy pod etykiete 'stop' jeśli w wyniku wykonania
                                              ; ostatniej instrukcji arytmetycznej otrzymano wartość ujemną.
0040      60046   ;           BRA powSub      ; Wywołanie podprogramu.
0041      10011   ; ret:      CPA result      ; Skopiowanie do akumulatora obecnej (cząstkowej) wartości obliczanego wyrażenia.
0042      30015   ;           ADD resSub      ; Dodanie do obecnej (cząstkowej) wartości obliczanego wyrażenia
                                              ; wartości jednomianu obliczonej w podprogramie.
0043      20011   ;           STO result      ; Zapisanie obecnej (cząstkowej) wartości obliczanego wyrażenia.
0044      60038   ;           BRA loopMain    ; Skok bezwarunkowy pod etykietę 'loopMain'.

0045      00000   ; stop:     HLT             ; Zatrzymanie procesora.

                  ;                           ; Początek podprogramu obliczającego wartość wyrażenia x^n.
0046      92101   ; powSub:   CPA (1)         ; Skopiuj do akumulatora wartość 1.
0047      91040   ;           POP coef        ; Zdejmi element ze stosu i zapisz pod etykietą 'coef'.
0048      00014
0049      91040   ;           POP power       ; Zdejmi element ze stosu i zapisz pod etykietą 'power'.
0050      00013

                                              ; Rozpoczęcie pętli liczącej potęgę.
                                              ; Pętla powinna wykonać się n razy dla wyrażenia base^power.
0051      02013   ; loop:     DEC power       ; Zmniejsz o jeden (1) wartość pod etykietą 'power'.
0052      90755   ;           BRNF end        ; Skok warunkowy pod etykiete 'end' jeśli w wyniku wykonania
                                              ; ostatniej instrukcji arytmetycznej otrzymano wartość ujemną.
                                              ; Nastąpi to wówczas gdy wartość pod etykietą 'power' będzie
                                              ; mniejsza niż zero.
0053      50012   ;           MUL base        ; Pomnóż zawartość akumulatora przez wartość pod etykietą 'base'.
0054      60051   ;           BRA loop        ; Wykonaj skok bezwarunkowy pod etykietę 'loop'.
0055      50014   ; end:      MUL coef        ; Policzona jest już wartość wyrażenia base^power. Teraz mnożymy ją
                                              ; przez wartość pod etykietą 'coef'.
0056      20015   ;           STO resSub      ; Zapisanie wartości jednomianu coef*base^power pod etykietą 'resSub'.
0057      60041   ;           BRA ret         ; Wykonaj skok bezwarunkowy pod etykietę 'ret'.
