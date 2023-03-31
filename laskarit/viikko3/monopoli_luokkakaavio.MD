```mermaid
classDiagram
    Pelilauta "1" --> "*" Pelaaja 
    Pelilauta "1" --> "*" Ruutu
    Ruutu "1" --> "*" Pelaaja

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
