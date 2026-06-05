# VBA Excel Access Standard

Riferimento pratico per codice VBA/Excel/Access preparato per Alberto.

## Struttura codice

- Separare lettura dati, trasformazione e scrittura output.
- Usare nomi espliciti per variabili e procedure.
- Evitare macro monolitiche quando una procedura breve rende il flusso piu leggibile.
- Limitare le continuazioni di riga `_`; per SQL lunghe preferire array e `Join`.

## Excel

- Usare `;` come separatore nelle formule per Excel italiano.
- Dichiarare esplicitamente foglio e intervallo prima di scrivere celle.
- Evitare refresh UI troppo frequenti durante cicli lunghi.

## Access e ADODB

- Trattare le connessioni come read-only quando il contesto non autorizza scritture.
- Chiudere recordset e connessioni in modo esplicito.
- Documentare join ipotizzati quando lo schema non espone relazioni fisiche.

## UserForm

- Preferire generazione via modulo standard `modCreaForm`.
- Ricreare il componente in modo controllato quando serve aggiornare il form.
- Usare controlli semplici e proprieta esplicite.

## Output

Quando produci codice, indica:

- dove incollarlo;
- quali riferimenti VBA servono;
- come provarlo;
- quali limiti restano.
