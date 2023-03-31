```mermaid
classDiagram
    Pelilauta "1" --> "*" Pelaaja 
    Pelilauta "1" --> "*" Ruutu

    class Ruutu{
        seuraava_ruutu
    }

    class Pelaaja{
        pelinappula
        ruutu
    }

    class Pelilauta{
        ruudut
    }

  



```
