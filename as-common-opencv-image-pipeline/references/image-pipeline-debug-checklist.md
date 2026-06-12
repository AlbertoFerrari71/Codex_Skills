# Image Pipeline Debug Checklist

## Prima di cambiare algoritmo

- Confermare input reali, formato, risoluzione e canali.
- Salvare immagine originale e ogni step intermedio rilevante.
- Separare preprocessing, geometria, segmentazione, misura e report.
- Annotare parametri: soglie, kernel, blur, area minima, tolleranze.
- Verificare output atteso su almeno un caso buono e un caso difficile.

## Debug intermedi consigliati

- Grayscale o canale scelto.
- Immagine equalizzata o filtrata.
- Istogramma.
- Maschera binaria.
- Contorni o componenti con overlay.
- Omografia/warp prima e dopo.
- Error map o differenza tra output.

## Metriche utili

- Numero componenti.
- Area, perimetro, bounding box.
- Percentuale pixel maschera.
- Distanza o reprojection error.
- Precisione manuale su sample piccolo.
