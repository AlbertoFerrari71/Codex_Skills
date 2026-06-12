# Prompt Integrity Rules

Un prompt Codex operativo deve essere verificabile prima dell'uso.

Controlli minimi:

- `END_OF_PROMPT_XXXX` presente, idealmente come ultima riga non vuota;
- sezione `CONTROLLO INTEGRITÀ PROMPT` presente quando il prompt e' lungo o
  critico;
- sezione `REGOLE FINALI` presente;
- code fence Markdown chiusi;
- report finale deterministico;
- vincoli Git espliciti: commit, push, PR, merge e deploy vietati salvo
  autorizzazione esplicita;
- nessun path Windows spezzato o comando PowerShell multilinea apparentemente
  non chiuso;
- nessun elenco numerato che termina in modo sospetto.

Se manca la sentinella finale o la sezione `REGOLE FINALI`, trattare il prompt
come potenzialmente troncato. In quel caso fermarsi, non modificare file e
produrre un report con stato `PROMPT_TRUNCATED` o equivalente richiesto dal
prompt.
