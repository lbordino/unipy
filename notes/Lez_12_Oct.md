# Lezione 12 Oct


---


### Idee  prima di iniziare.

 - Avere un'idea di fondo di come è possibile risolvere il problema(se non si è capaci a risolvere il problema a mano non possiamo insegnarloa nessuno).


---


## Rappresentazioni di dati

1. Il nostro sistema di conto è decimale posizionale.
2. Il pc ovviamente utilizza un sistema binario ovvero solo (0,1)
  * Bit significa **BI**nary Digi**T**.
  * Per trasformare il binario in decimale elevo la cifra alla corrispondente potenza di 2.
  * Per determinare il valore binario di un numero decimale divido considerando il modulo e li metto in ordine. (Nel senso che li prendo al contrario dall'ultimo al primo)
3. Con n bit posso rappresentare da 0 a  2^n - 1 
4. bit rapprensenta una signola cifra 
5. 8 bit vengono chiamati Byte
6. Word = aggregazione di byte cambia a seconda del numero di byte (quasi sempre 2)
7. Nibble è un 4 bit aggregation
8. I bit più importante è quello più a sinistra poi scemano verso quello più a destra
9. Le somme in sistema binario sono identiche rispetto al sitema decimale, l'unica cosa che cambia è ovviamnete quando faccio il riporto.
10. Overflow è una condizione dinamica possibile solo in relazione ad un'operazione.

> Chicca: uno tra i primi processori inventati era il 4004 a 4bit

- Viene utilizzata la notazione Hex perchè più sintetica 
  * la notazione (ovvero 1^n, 2^n ...) per passare da decimale al Hex


---


###Introdurre il concetto di segno in un numero

Ci sono più metodi:
 * Si può utilizzare il bit MSB come bit di segno perdendo ovviamente una posizione e dunque una potenza di 2
    -  Nasce il problema dello 0
    - Nel fare le operazioni quel segno rompe moltissimo perchè devo verificare ogni volta tutto.
    - In generale non ho perso molto solo lo 0 perchè è sovrabbondante -0 +0
 * Complemento a due:
    - Sommi una quantità positiva a qualcosa di sempre più grande di tutti e sempre negativa, una sorta di traslazione
    - Il primo bit è negativo ma vale la potenza di 2 equivalente
    - parto dall'ultimo bit (negativo) e poi sommo il resto
    - Lo zero è unico ma considerato come +0

#### Come trasformare un numero decimale in complemento a due

1. Se il numero è positivo allora lo tratto come un numer normalissimo e aggiungo x 0 davanti.
2. Se il numero è negativo faccio prima il complento a 1 (inversione) poi sommo un bit a destra sul LSB e ho il mio numero in CA2 o 2C (engl version)


> Chicca: i bit che fillano *00*10 si chiamano padding ovvero completamento. 

#### Quando viene usato il 2C

Non viene mai fatta una sottrazione, viene fatto il 2C del numero e poi banalmente sommato.

*  2C(x) = -x
*  2C(-x) = x

Potrebbe capitare che ci sia un carry (riporto) sul MSB non me ne frega nulla handlo l'exception ma la ignoro un negativo + un positvo non può essere maggiore di quanto fosse quello maggiore.

Quali sono i limiti del 2C:
 - il 2C non è simmetrico  [-128 .. 127]
