---
name: as-common-vba-excel-access-alberto
description: Usa questa skill per codice VBA/Excel/Access di Alberto, inclusi UserForm generati via codice, eSolver read-only, ADODB/ODBC, performance, debug flag e fogli Excel.
---

# Scopo

Generare o modificare codice VBA/Excel/Access secondo le convenzioni tecniche di Alberto.

# Quando usarla

Usala per:
- Excel VBA;
- Access VBA;
- collegamenti eSolver SQL Server read-only;
- ADODB/ODBC;
- UserForm;
- import/export dati;
- fogli di controllo gestione;
- automazioni Amazon/eInvoix.

# Regole personali Alberto

1. Excel italiano: nelle formule usare `;` come separatore argomenti.
2. Evitare variabili chiamate `data` e `currency`; preferire nomi come `dictData`, `currCode`, `dtRif`, `importoVal`.
3. Evitare troppe continuazioni di riga `_` in VBA.
4. Per SQL lunghe usare concatenazioni progressive o array/join.
5. Usare codice semplice, leggibile e manutenibile.
6. Prima di creare nuovi fogli, proporre o chiedere la logica di ordinamento dei fogli.
7. Per UserForm, preferire generazione automatica via modulo standard `modCreaForm`.
8. Per debug usare flag globali:
   - `Flg_Print_Debug`
   - `Flg_Print_Debug_tempi`
9. Per aggiornamenti UI/status bar, evitare refresh troppo frequenti; usare soglia configurabile.
10. Non inserire `Attribute VB_Name = ...` nei file `.txt` destinati al copia/incolla manuale.

# eSolver / SQL Server

Per progetti collegati a eSolver, default preferito:

```text
DSN=eSolver;UID=lettore;PWD=lettore;LANGUAGE=italiano;DATABASE=ESOLVER
```

Regole:
- accesso read-only;
- non assumere foreign key fisiche;
- documentare join ipotizzati;
- separare query, parsing e output;
- evitare modifiche DB.

# UserForm generati via codice

Default operativo:
- modulo standard `modCreaForm`;
- rimozione preventiva del componente se già esiste;
- `ThisWorkbook.VBProject.VBComponents.Add(3)`;
- controlli tramite `vbComp.Designer.Controls.Add`;
- proprietà form tramite `vbComp.Properties(...)`;
- preferire controlli semplici e robusti.

# Output richiesto

Quando generi codice:
1. spiega cosa fa;
2. indica dove incollarlo;
3. evidenzia dipendenze/riferimenti VBA;
4. indica come testarlo;
5. segnala rischi o limiti.
