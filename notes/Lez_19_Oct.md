## Rappresentazione di numeri reali

1. Opzione più semplice utlizzi i primi x bit per la parte intera mentre i secondi x bit per la parte decimale ** virgola fissa o fixed point**
 * presenta numerosi problemi perchè non posso essere sia preciso per la parte intera e quella dopo la virgola

2. Seconda opzione **virgola mobile** ovvero inserisco la parte che mi interessa e poi un separatore che mi dica la seconda parte.
 * per fare ciò mi serve per prima cosa mettere tutto in notazione scientifica. a questo punto posso usare due numeri che rappresentino il mio float * M = mantissa, E = esponente*
 * Per scrivere effettivamente un numero in Floating Point utilizzo segno, exp con il suo segno e poi numero effettivo ovvero la mantissa. ( mantissa := funzione matematica che associa ad un reale la sua parte decimale) 

### Formato IEEE-754

Mantissa nella forma normalizzata <  2 (min 1 è sempre quello quindi non lo scrivo nel calcolatore ma so che ci sarà sempre **hidden bit**)

Base dell'esponente pari a 2

> Float 32bit 754 sp (single precision)
> Segno 1 bit | esponente 8 bit | mantissa 23 bit 
> 10 alla più o meno 38 

> Double 64bit 754 dp (double precision)
> Segno 1 bit | esponente 11 bit | mantissa 52 bit 
> 10 alla più o meno 308

- I numeri decimali trasformati in binario sono un insieme di bit infinito quindi non saranno sembre un'approssimazione del vero numero in binario 

#### UnderFlow e OverFlow

- se il numero eccede il 10^308 overflow

- se il numero eccede il 10^-308 underflow

- se succede qualcosa tipo 1/0 il calcolatore capisce che non è un numero allora risponde NaN ( not a number) 

#### Approssimazioni

In floating point la somma non è sempre associativa
E.g.:
  x = 10exp38
  y = 10exp38
  z = 1
  (x - y) + z = 1
   x - (z + y) = 0

- si porta sempre alla potenza maggiore ( è possibile che il valore non sia significativo su quel valore e dunque lo perdo)

### Infomazione sempre numerica

* il  calcolatore codifica tutto in numero un modo è il codice ASCII
  *American Standard Code for Information Interchange*


**Per codificare N elementi mi serve un numero di bit pari a ceil di log2 di N**

- esitono dei caratteri detti di controllo (CR, NULL)

- Unicode e UTF-8  sono stati aggiunti tutti i caratteri che interessano a tutto il mondo e le emoticon

###UTF - 8

- 1 byte per ASCII
- 2 byte per i Latin 
- 4 byte per le emoji

### Codifiche audio e video 
- RGB 8 bit per ogni canale
- altri esempi sono gli H264 H265


#Architettura dei calcolatori

- archittetura di Von Neuman (gioco della vita di Conway:= automa decisionale) 

- Ingresso e Uscita analogica e calcolazione digitale

-  pezzi RAM ROM e CPU

##CPU (central processing unit)

###Unità operativa:

- È composta da ALU, FPU, Registry, Registro dei Flag

   Ha una piccolissima quantità di memoria la cache e i registri  minuscoli ma estremamente veloci

   1. Unità di controllo e Unità operativa ( ALU Arithmetic Logic Unit + FPU Floating Point Unit + registri) vengono spostati attreverso i bus

   2. Registri: sono  piccole porzioni di memoria max 128 

   3. Flag sono riassunti  tipo allarme il risultato è zero o e negativo o è positivo o è OverFlowato

###Unità di controllo:

- È composto da:

  1. Istruction register  parte di memoria dove vengono posti dei codici per essere analizzati

  2. PC programming counter 

  3. la logica di controllo è un circuito digitale che esegue le operazioni (interpreta il codice macchina dentro IR per decidere ed emette gli ordini che le varie unità devono eseguire)


##Esecuzione  di un'istruzione:

- Fetch la memoria letta agli indirizzi del PC  e lo mette nel IR
- Decode decodifica le info dell' IR 
- Execute viene passata a chi di dovere per effeture l'istruzione


####Clock
il clock è un elemento di temporizzazione ogni *Colpo di Clock* succede un operazione  sincronizza tutte le operazione nella macchina

### Ciclo Macchina
intervallo di tempo in cui viene svolta un'operazione è sempre un multiplo della frequenza di clock
> Chicca: la velocità di unn programma dipende dal tipo di istruzione e dalla frequenza di clock, una divisione tra reali ci mette 15 colpi di clock mentre una tra int  1 

### Memoria 
- caratteristiche:
  1. Indirizzamento
  2. Parallelismo
  3. Accesso (sequenziale o casuale)
  4. Gerarchia 

* Ogni elemento detto locazione o cella di memoria ha un indirizzo
* Ogni cella contiene a 64bit 8byte (word macchina)
* l'accesso è identico per tutte le celle

* Ci sono varie gerarchie Disk -> DRAM -> SRAM -> cache -> registry

###Bus

- I dispositivi sono collegati con i bus (omnibus una connessione per tutti)
  1. Connessioni punto punto non ha senso troppe connessioni
  2. pista in cui tutti i dispositivi sono connessi 
  3. tipo una strada  quindi solo uno alla volta ( il processore fa da vigile)
  4. un bus ha un'ampiezza di nbit stessa del sistema 64bit
  5. la frequenza e quanti bit ogni x tempo
  6. non tutti sono bidirezionali (address solo dal processore)
Tipi di Bus:
 * dati  Dbus
 * indirizzi ( monodirezionale solo verso il componente dal processore) Abus
 * di controllo Cbus
