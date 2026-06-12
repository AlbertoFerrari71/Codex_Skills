---
name: as-common-opencv-image-pipeline
description: "Usa questa skill per pipeline immagini di Alberto con OpenCV Python/C++: QR code, omografia, binarizzazione, istogrammi, segmentazione, soglie, debug visuale, output intermedi e confronto immagini. DiamSign e' un esempio, non un vincolo. Non usarla per generazione immagine creativa, UI review, FastAPI, email, prompt Codex o analisi brevettuale."
---

# Scopo

Usa questa skill per progettare o debuggare pipeline immagini di Alberto con OpenCV, Python o C++, incluse immagini tecniche, QR, glitter, omografie, soglie, segmentazione, confronto output e debug visuale.

# Quando usarla

Usala quando Alberto lavora su:
- pipeline immagini;
- OpenCV C++ o Python;
- QR code e marker;
- omografia, prospettiva e registrazione immagini;
- binarizzazione, soglie, istogrammi e morfologia;
- segmentazione, maschere e misure;
- debug immagini intermedie;
- confronto tra output atteso e output reale;
- DiamSign, AggloDetect o superfici glitterate come esempi concreti, non come vincolo.

# Quando NON usarla

Non usarla per:
- generazione immagine creativa o asset bitmap;
- review visuale UI/web: usa `as-common-web-ui-design-review`;
- email o comunicazioni commerciali: usa `as-common-business-email-draft`;
- backend FastAPI, pytest o template: usa `as-common-python-fastapi-debug`;
- prompt Codex operativo: usa `as-common-codex-command-pack`;
- disclosure brevettuale o analisi legale: usa `as-common-technical-patent-draft`;
- VBA/Excel/Access: usa `as-common-vba-excel-access-alberto`.

# Procedura

1. Descrivere chiaramente input, output e immagini intermedie.
2. Preferire pipeline a step, con salvataggio debug visuale.
3. Separare preprocessing, trasformazioni geometriche, segmentazione, misura e report.
4. Evitare algoritmi opachi se non necessari.
5. Per C++ OpenCV rispettare la preferenza di Alberto: usare namespace globali, senza prefissi `cv::` e `std::` quando possibile.
6. Negli esempi C++ mettere funzione principale all'inizio, prototipi prima e sub-function dopo, se coerente con il file.
7. Per Python usare codice semplice, commentato e verificabile.
8. Evidenziare parametri sensibili e soglie da calibrare.
9. Non usare OCR salvo necessita esplicita o evidenza che sia il problema giusto.

# Output atteso

- Pipeline step-by-step.
- Parametri principali da tarare.
- Metriche o criteri di confronto.
- Immagini/debug intermedi attesi.
- Codice o pseudocodice solo se richiesto.
- Rischi tecnici e casi limite.
- Test con immagini o fixture consigliate.
- Prossima prova consigliata.

# References

- `references/image-pipeline-debug-checklist.md`
- `references/opencv-cpp-style-alberto.md`

# Regole

- Non inventare dimensioni, DPI, camera, lente o illuminazione se non forniti.
- Distinguere sempre dati osservati, ipotesi e parametri da stimare.
- Se mancano immagini, chiedere sample o proporre una fixture minima.
