---
name: as-common-opencv-image-pipeline
description: "Usa questa skill per pipeline immagini di Alberto con OpenCV/Python/C++: debug visuale, QR, glitter, superfici, segmentazione, soglie, omografia e report intermedi."
---

# Scopo

Usa questa skill per pipeline immagini di Alberto con OpenCV, Python o C++, incluse immagini tecniche, QR, glitter, omografie, soglie, segmentazione e debug visuale.

# Quando usarla

Usala quando Alberto lavora su elaborazione immagini, DiamSign, AggloDetect, QR code, superfici glitterate, segmentazione di granuli, maschere, soglie o confronto tra immagini.

# Procedura

1. Descrivere chiaramente input, output e immagini intermedie.
2. Preferire pipeline a step, con salvataggio debug visuale.
3. Separare preprocessing, trasformazioni geometriche, segmentazione, misura e report.
4. Evitare algoritmi opachi se non necessari.
5. Per C++ OpenCV rispettare la preferenza di Alberto: usare namespace globali, senza prefissi `cv::` e `std::` quando possibile.
6. Per Python usare codice semplice, commentato e verificabile.
7. Evidenziare parametri sensibili e soglie da calibrare.

# Output atteso

- Pipeline proposta.
- Parametri principali.
- Immagini/debug intermedi consigliati.
- Codice o pseudocodice.
- Rischi tecnici.
- Prossima prova consigliata.