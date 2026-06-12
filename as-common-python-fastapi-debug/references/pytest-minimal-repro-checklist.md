# Pytest Minimal Repro Checklist

## Prima del fix

- Eseguire il test gia fallente, se esiste.
- Se il fallimento e' ampio, isolare un solo endpoint o fixture.
- Annotare comando, exit code e sintesi errore.
- Non cambiare fixture globali senza capire impatto.

## Test mirato

- Preferire un test su route o funzione coinvolta.
- Usare client FastAPI esistente se presente.
- Controllare status code, contenuto essenziale e branch errore.
- Per template, verificare testo o contesto minimo, non tutto l'HTML.

## Dopo il fix

- Rieseguire test mirato.
- Rieseguire suite del modulo toccato.
- Segnalare se full pytest non e' stato eseguito.
