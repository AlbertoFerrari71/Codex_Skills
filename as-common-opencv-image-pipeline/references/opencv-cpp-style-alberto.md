# OpenCV C++ Style Alberto

Quando Alberto chiede esempi C++ OpenCV, rispettare lo stile del progetto se
visibile. In assenza di stile locale, preferire:

- namespace globali quando coerente con il file;
- evitare prefissi `cv::` e `std::` negli esempi se Alberto lo ha richiesto;
- funzione principale all'inizio;
- prototipi prima della funzione principale;
- sub-function dopo la funzione principale;
- codice breve e verificabile;
- debug visuale e salvataggio immagini intermedie.

## Limiti

- Non forzare questo stile se il repository usa chiaramente una convenzione diversa.
- Non introdurre OCR salvo necessita esplicita.
- Non nascondere parametri sensibili dentro costanti non spiegate.
