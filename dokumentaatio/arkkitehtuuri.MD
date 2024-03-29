# Arkkitehtuurikuvaus


## Rakenne
Ohjelman rakenne on jäsennelty kahteen kerrokseen. Koodin pakkausrakenne on seuraavanlainen:


```mermaid
classDiagram
    main "1" --> "1" processes 
    processes "1" --> "1" repositories 
    repositories "1" --> "1" processes 
    repositories "1" --> "1" data
    data "1" --> "1" repositories 
    ui "1" --> "1" repositories 
    repositories "1" --> "1" ui
    processes "1" --> "1" inputs 
    inputs "1" --> "1" processes 
    ui "1" --> "1" processes 
    processes "1" --> "1" ui 


    class processes{
    }
    
    class repositories{ 
    }
    
    class inputs{ 
    }
    
    class ui{ 
    }
    
    class main{ 
    }

    class data{
    }
```
Pakkaus _ui_ sisältää käyttöliittymästä vastaavan koodin. Pakkaus _processes_ sisältää kaiken muun koodin joka vastaa sovelluslogiikasta,  suorituksesta, sekä tiedon pysyväistallennuksesta. Pakkaus _main_ sisältää ohjelman käynnistyskoodin joka on eriytetty omaksi skriptiksi _flashcards.py_. Pakkaus _repositories_ sisältää tietokantaa käsittelevän koodin. Pakkaus _data_ sisältää  pysyväistallennetun tiedon _.csv_ tai _sql_ muodossa. Pakkaus _inputs_ sisältää korttipakat eli syötetiedostot.


## Sovelluslogiikka
Sovelluksen rakenne modostuu seitsemästä luokasta: _Play_, _Database_, _DatabaseFileHandling_, _DatabaseInteractions_, _App_, _UserInterface_, _MainView_, _FileSelectionView_, _DatabaseUserInteractions_ ja _Window_parameters_. Luokat kuvaavat sovelluksen toiminnallisia kokonaisuuksia ja niiden keskinäiset suhteet voidaan kuvata luokkadiagrammin avulla: 
Luokkadiagrammi: 

```mermaid
classDiagram
    class UserInterface
    class MainView
    class DatabaseInteractions
    class DatabaseFileHandling
    class DatabaseUserInteractions
    class WindowParameters
    class FileSelectionView
    class Database
    class App
    class Play

    UserInterface --|> MainView
    MainView --|> WindowParameters
    FileSelectionView --|> WindowParameters
    Database --|> DatabaseInteractions
    Database --|> DatabaseFileHandling
    Database --|> DatabaseUserInteractions
    App --|> UserInterface
    App --|> FileSelectionView
    Play --|> UserInterface
    App --|> Database
    Play --|> App
```

Yksityiskohtaisempi versio missä näkyy myös luokkien attribuutit ja metodit löytyy [täältä](https://github.com/platipus82/ot-harjoitustyo/blob/main/dokumentaatio/class_diagram_detailed.MD). 


Ohjelman rakenteeseen jääneet heikkoudet

Päätoiminnallisuuksiin kuuluu korttipakan valinta, kysymysten järjestäminen sekä kysymysten kysyminen.

### Korttipakan valinta
Aluksi sovellus näyttää input-kansion tiedostot, joista käyttäjä voi valita sopivan syötetiedoston. Lisäksi käyttäjälle annetaan mahdollisuus valita toinen kansio tai muu tiedosto. 

### Kysymysten järjestäminen
Sovellus järjestää kysymykset satunnaisjärjestykseen. 

### Kysymysten kysyminen
Kun syötetiedosto ja korttipakka on valittu, ohjelma käy läpi pakan kysymykset yksi kerrallaan. Kunkin kysymyksen kohdalla käyttäjä voi pyytää sovellusta näyttämään oikea vastaus valitsemalla painiketta _Proceed_, tai keskeyttää ohjelman suoritus klikkaamalla painiketta _Exit_.

Tämä prosessi voidaan havainnollistaa sekvenssidiagrammin avulla:
```mermaid
sequenceDiagram

    Play->>UserInterface: The question is: 1+1=? Proceed or exit?
    UserInterface-->>MainView: The question is: 1+1=? Proceed or exit?
    MainView-->>WindowParameters: what are correct window dimensions?
    WindowParameters-->> MainView: 400 x 300
    actor User
    MainView-->>User: The question is: 1+1=? Proceed or exit?
    User-->>MainView: Proceed
    MainView-->>UserInterface: Proceed
    UserInterface-->>Play: Proceed
    Play->>UserInterface: Question: 2+2=? Answer: 4.  Proceed or exit?
    UserInterface-->>MainView: Question: 2+2=? Answer: 4.  Proceed or exit?
    MainView-->>WindowParameters: what are correct window dimensions?
    WindowParameters-->> MainView: 400 x 300
    MainView-->>User: Question: 2+2=? Answer: 4.  Proceed or exit?
    User-->>MainView: exit
    MainView-->>UserInterface: exit
    UserInterface-->>Play: exit
    Play->>UserInterface: Game over
    UserInterface-->>MainView: Game over
    MainView-->>WindowParameters: what are correct window dimensions?
    WindowParameters-->> MainView: 400 x 300
    MainView-->>User: Game over
```    

## Sovelluksen heikkoudet ja rajoitukset 
### Käyttöliittymä
Tällä hetkellä sovellus mahdollistaa tietojen tallentamisen myös ihmisluettavassa muodossa .csv-formaattiin, mutta sitä ei ole tuettu käyttöliittymän tasolla. Myös käyttäjälle näytettävä ikkuna voisi toteuttaa visuaalisesti miellyttävämmällä tavalla. 

### Tietoturva
Käyttäjätietoja tai syötetiedostoja ei ole suojattu millään lailla, vaikka niiden suojaaminen esim. salasanalla olisi  helppoa toteuttaa.

### Datan käsittely
Datan käsittely olisi voinut luontevammin eriyttää omaksi luokaksi. Nyt sitä tehdään useassa luokassa ja koodissa on päällekkäisyyksiä. Myös käyttäjälle näytettävä pelin yhteenveto voisi olla visuaalisesti viimeistellympi ja sisältää esimerkiksi edistystä ja kehitystä näyttäviä kuvaajia.

### Kysymysten järjestys
Tällä hetkellä ainoa tuettu kysymysten järjestys on satunnaisjärjestys. Kuitenkin myös muunlaiset järjestykset olisi mahdollista toteuttaa ja niiden avulla säädellä kysymysten vaikeusastetta. 
