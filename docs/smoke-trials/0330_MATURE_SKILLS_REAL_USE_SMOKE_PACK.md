# 0330) Mature Skills Real-Use Smoke Pack

Data: 2026-06-12

Modalita: smoke trial documentale, senza modifiche a repository target, senza
web search reale e senza codice complesso.

## 1. as-common-deep-research-industriale

| Campo | Valore |
|---|---|
| Prompt realistico Alberto | "Valuta un coating industriale per glitter/microdiamanti: voglio fonti, fornitori, norme, incertezze, rischi e piano prove." |
| Perche deve attivarsi | Richiede ricerca tecnica industriale con fonti, dati, incertezze e decisione pratica. |
| Perche non skill vicine | Non e' email, non e' disclosure per consulente, non e' OpenCV. |
| Output atteso | Sintesi esecutiva, tabella fonti, dati, ipotesi, rischi, piano prove e decisione consigliata. |
| Rischi | Senza web reale va dichiarato che fonti aggiornate sono da raccogliere. |
| Verdict | PASS |

## 2. as-common-technical-patent-draft

| Campo | Valore |
|---|---|
| Prompt realistico Alberto | "Prepara disclosure tecnica per consulente brevettuale su algoritmo QR/glitter, con problema, soluzione, varianti, figure e domande." |
| Perche deve attivarsi | Serve materiale tecnico per consulente e boundary legale esplicito. |
| Perche non skill vicine | Non e' ricerca mercato; non e' codice OpenCV operativo; non e' email. |
| Output atteso | Problema tecnico, stato dell'arte da verificare, soluzione, varianti, vantaggi, figure, dati mancanti e domande al consulente. |
| Rischi | Claim/FTO/prior art non sono pareri legali e vanno verificati professionalmente. |
| Verdict | PASS |

## 3. as-common-business-email-draft

| Campo | Valore |
|---|---|
| Prompt realistico Alberto | "Riscrivi una email delicata a un fornitore: devo essere logico, empatico e fermo su una consegna in ritardo." |
| Perche deve attivarsi | Output e' comunicazione business delicata con tono Alberto. |
| Perche non skill vicine | Non e' runbook, ricerca, prompt Codex o documento brevettuale. |
| Output atteso | Oggetto, bozza pronta, tono, versione piu ferma/morbida, rischi relazionali e punti da evitare. |
| Rischi | Non inventare fatti, prezzi, responsabilita o promesse. |
| Verdict | PASS |

## 4. as-common-docs-runbook-builder

| Campo | Valore |
|---|---|
| Prompt realistico Alberto | "Crea un runbook di manutenzione mensile con prerequisiti, passi, comandi, verifiche, stop, rollback e ownership." |
| Perche deve attivarsi | Richiede documentazione operativa persistente e ripetibile. |
| Perche non skill vicine | Non sono Project Instructions, non e' handoff chat, non e' lifecycle step. |
| Output atteso | Scopo, prerequisiti, passi, comandi, verifiche, rollback/stop, troubleshooting, ownership e aggiornamento futuro. |
| Rischi | Comandi non verificati vanno marcati come da verificare. |
| Verdict | PASS |

## 5. as-common-opencv-image-pipeline

| Campo | Valore |
|---|---|
| Prompt realistico Alberto | "Il QR non si legge dopo omografia: proponi pipeline OpenCV con binarizzazione, debug immagini intermedie, metriche e parametri." |
| Perche deve attivarsi | Dominio OpenCV/QR/omografia/soglie/debug visuale. |
| Perche non skill vicine | Non e' UI review, non e' FastAPI, non e' disclosure brevettuale. |
| Output atteso | Pipeline step-by-step, immagini diagnostiche, parametri, metriche, rischi e test con immagini. |
| Rischi | Senza sample immagini non si devono inventare soglie o condizioni di acquisizione. |
| Verdict | PASS |

## 6. as-common-python-fastapi-debug

| Campo | Valore |
|---|---|
| Prompt realistico Alberto | "FastAPI torna 500 su una route Jinja in pytest: leggi trace, distingui template/route, proponi fix minimo e gate." |
| Perche deve attivarsi | Richiede debug FastAPI/pytest/template con patch minima. |
| Perche non skill vicine | Non e' UI visual review; non e' OpenCV; non e' Git publish flow. |
| Output atteso | Diagnosi probabile, passi minimi, test mirato, comando, rollback/stop e gate prima del commit. |
| Rischi | Separare trace reale da ipotesi e ambiente locale/server. |
| Verdict | PASS |

## Conclusione

Tutte le sei skill producono output utile e delimitato nello smoke documentale.
Il limite comune e' che non sono stati eseguiti web search, repository target o
codice applicativo reale.
