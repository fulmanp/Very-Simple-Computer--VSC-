```            
aa, aaaa, aaaaa - adress, liczba całkowita bez znaku z zakresu:
aa   : od 00    do 99
aaaa : od 0000  do 9999
aaaaa: od 00000 do 99999

ss, ssss, sssss - wartość, liczba całkowita ze znakiem z zakresu:
ss   : od 19 (-9)       do 09 (+9)
ssss : od 1999  (-999)  do 0999 (+999)
sssss: od 19999 (-9999) do 09999 (+9999)

Najbardziej znacząca cyfra (pierwsza od lewej strony) oznacza koduje znak liczby:
0: wartość dodatnia
1: wartość ujemna

Flagi:
NEGATIVE
ZERO

Flagi ustawiane są w efekcie wykonania operacji arytmetycznych: ADD, SUB, MUL, INC, DEC.

Tryby adresowania:

             91... - bezpośrednie, dwubajtowe
             92... - natychmiastowe, jednobajtowe
             93... - natychmiastowe, dwubajtowe
             94... - pośrednie, jednobajtowe
             95... - pośrednie, dwubajtowe

Mnemonic      Kod maszynowy Znaczenie
HLT           00000         Zatrzymaj cpu.
CPA  aaaa     1aaaa         Skopiuj wartość z pamięci pod adresem aaaa do akumulatora A := M[aaaa].
CPA  (ss)     921ss         Skopiuj dokładną wartość ss do akumulatora, A := ss.
CPA  (sssss)  93100 sssss   Skopiuj dokładną wartość sssss (znajdującą się w następnym bajcie) do akumulatora A := sssss.
CPA  [aa]     941aa         Skopiuj wartość z pamięci pod adres podany w pamięci pod adresem aa do
                             akumulatora, A := M[M[aa]].
CPA  [aaaaa]  95100 aaaaa   Skopiuj wartość z pamięci pod adres podanym w pamięci pod adresem aaaaa
                             do akumulatora A := M[M[aaaaa]].
STO  aaaa     2aaaa         Skopiuj wartość z akumulatora do pamięci pod adres aaaa, M[aaaa] := A.
STO  [aa]     942aa         Skopiuj wartość z akumulatora do pamięci pod adres podanym w pamięci
                             pod adresem aa, M[M[aa]] := A.
STO  [aaaaa]  95200 aaaaa   Skopiuj wartość z akumulatora do pamięci pod adres podanym w pamięci
                             pod adresem aaaaa, M[M[aaaaa]] := A.
ADD  aaaa     3aaaa         Dodaj wartość pod podanym adresem aaaa do akumulatora. Wynik został zapisany
                             w akumulatorze A := A + M[aaaa].
ADD  (ss)     923ss         Dodaj dokładną wartość ss do akumulatora. Wynik zapisywany jest w akumulatorze,
                             A := A + ss.
ADD  (sssss)  93300 sssss   Dodaj dokładną wartość sssss (znajdującą się w następnym bajcie) do akumulatora.
                             Wynik zapisywany jest w akumulatorze A := A + sssss.
ADD  [aa]     943aa         Dodaj wartość z pamięci pod adresem podanym w pamięci pod adresem aa
                             do akumulatora A := A + M[M[aa]].
ADD  [aaaaa]  95300 aaaaa   Dodaj wartość z pamięci pod adresem podanym w pamięci pod adresem aaaaa
                             do akumulatora, A := A + M[M[aaaaa]].
SUB  aaaa     4aaaa         Odejmij wartość pod podanym adresem aaaa od akumulatora.
                             Wynik zapisywany jest w akumulatorze A := A - M[aaaa].
SUB  (ss)     924ss         Odejmij dokładną wartość ss od akumulatora. Wynik zapisywany jest
                             w akumulatorze, A := A - ss.
SUB  (sssss)  93400 sssss   Odejmij od akumulatora dokładną wartość sssss (znajdującą się w następnym bajcie).
                             Wynik zapisywany jest w akumulatorze, A := A - sssss.
SUB  [aa]     944aa         Odejmij wartość z pamięci pod adresem podanym w pamięci pod adresem aa
                             z akumulatora, A := A - M[M[aa]].
SUB  [aaaaa]  95400 aaaaa   Odejmij wartość z pamięci pod adresem podanym w pamięci
                             pod adresem aaaaa z akumulatora, A := A - M[M[aaaaa]].
MUL  aaaa     5aaaa         Pomnóż wartość z akumulatora przez wartość pod podanym adresem aaaa.
                             Wynik zapisywany jest w akumulatorze A := A * M[aaaa].
MUL  (ss)     925ss         Pomnóż wartość z akumulatora przez dokładną wartość ss. Wynik zapisywany jest
                             w akumulatorze, A := A * ss.
MUL  (sssss)  93500 sssss   Pomnóż wartość z akumulatora przez dokładną wartość sssss (znajdującą się w następnym bajcie).
                             Wynik zapisywany jest w akumulatorze A := A * sssss.
MUL  [aa]     945aa         Pomnóż wartość z akumulatora przez wartość z pamięci znajdującą się pod adresem
                             określonym przez wartość pamięci pod adresem aa, A := A * M[M[aa]].
MUL  [aaaaa]  95500 aaaaa   Pomnóż wartość z akumulatora przez wartość z pamięci pod podanym adresem
                             w pamięci pod adresem aaaaa, A := A * M[M[aaaaa]].
BRA  aaaa     6aaaa         Bezwarunkowe przejście do instrukcji znajdującej się pod adresem aaaa.
BRN  aaaa     7aaaa         Warunkowe przejście do instrukcji znajdującej się pod adresem aaaa jeśli wartość
                             przechowywana w akumulatorze jest ujemna.
BRNF aa       907aa         Warunkowe przejście do instrukcji znajdującej się pod adresem aa
                             jeśli flaga NEGATIVE ma wartość TRUE.
BRZ  aaaa     8aaaa         Warunkowe przejście do instrukcji znajdującej się pod adresem aaaa
                             jeśli wartość przechowywana w akumulatorze jest równa zero.
BRZF aa       908aa         Warunkowe przejście do instrukcji znajdującej się pod adresem aa, jeśli flaga ZERO ma wartość TRUE.
INC  aaa      01aaa         Zwiększ wartość pod adresem aaa o 1, M[aaa] := M[aaa] + 1.
DEC  aaa      02aaa         Zmniejsz wartość pod adresem aaa o 1, M[aaa] := M[aaa] - 1.
PUSH          03000         Skopiuj wartość z akumulatora na stos, A -> STACK.
PUSH aaaaa    91030 aaaaa   Skopiuj wartość pod adresem aaaaa na stos, M[aaaaa] -> STACK.
PUSH (sssss)  93030 sssss   Połóż dokładną wartość sssss na stos, ssssss -> STACK.
PUSH [aaaaa]  95030 aaaaa   Połóż wartość pod adresem podanym pod adresem aaaaa na stos,
                             M[M[aaaaa]] -> STOS.
POP           04000         Skopiuj wartość ze stosu do akumulatora, STACK -> A.
POP  aaaaa    91040 aaaaa   Pobierz wartość ze stosu i umieść ją pod adresem aaaaa, STACK -> M[aaaaa].
POP  [aaaaa]  95040 aaaaa   Pobierz wartość ze stosu i umieść ją pod adresem określonym przez wartość
                             pod adresem aaaaa, STACK -> M[M[aaaaa]].
```