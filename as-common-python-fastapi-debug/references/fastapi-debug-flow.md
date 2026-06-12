# FastAPI Debug Flow

## Sequenza minima

1. Leggere trace reale o errore osservato.
2. Identificare endpoint, template, fixture o dipendenza coinvolta.
3. Riprodurre con il test piu piccolo disponibile.
4. Separare ambiente locale, server e deploy.
5. Proporre patch minima.
6. Rieseguire test mirato.
7. Solo dopo, valutare gate piu ampio.

## Domande utili

- L'errore e' HTTP status, exception Python, template rendering o fixture?
- Il test fallisce prima o dopo la route?
- La dipendenza e' mockata, fixture o database reale?
- Uvicorn mostra un trace diverso da pytest?
- Il problema e' locale o server?

## Output

Scrivere diagnosi probabile, file coinvolti, comando di verifica e rollback/stop
se la patch non conferma l'ipotesi.
