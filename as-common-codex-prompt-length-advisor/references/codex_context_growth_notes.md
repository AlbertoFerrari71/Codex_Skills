# Codex Context Growth Notes

La lunghezza del prompt iniziale non e' l'unico rischio. Durante il run Codex
puo' generare molto piu' contesto leggendo file, stampando log, aprendo diff e
accumulando report.

Segnali di crescita incontrollata:

- leggere tutto il repository senza filtro;
- aprire intere directory o file enormi senza criteri;
- stampare output completi di test lunghi;
- usare diff lunghi senza sintesi o senza `git --no-pager`;
- fare scansioni esplorative senza pattern mirati;
- salvare log completi nel Bridge;
- chiedere report troppo prolissi;
- ripetere verifiche senza limiti.

Mitigazioni:

- preferire `rg` con pattern mirati;
- leggere solo file rilevanti;
- usare `git --no-pager` per output Git;
- riportare sintesi e righe chiave invece di log completi;
- separare storico e materiali lunghi in file riferimento;
- usare prompt packetization solo quando alleggerire il prompt monolitico non
  basta.
