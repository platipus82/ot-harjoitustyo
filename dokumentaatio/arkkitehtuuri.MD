Luokkadiagrammi: 

```mermaid
classDiagram
    Play "1" --> "1" App 
    Play "1" --> "1" UI 
    App "1" --> "1" UI
    App "1" --> "1" Play
    UI "1" --> "1" App
    UI "1" --> "1" GUI
    UI "1" --> "1" GUI_input_file_selection
    GUI_input_file_selection "1" --> "1" UI
    GUI "1" --> "1" UI
    
    class App{
        input_dir
        input_path 
        data
        filelist
    }
    class Play{
        ask()
    }
    class UI{
        show_output()
        ask_for_input()
        ask_for_input_file()
    }

    class GUI{
        show_output()
        ask_for_input()
        ask_for_file()
        set_result()

    }
    
    class GUI_input_file_selection{
        select_file()
        choose_file()
        choose_directory()
    }    
```

# Päätoiminnallisuudet
Päätoiminnallisuuksiin kuuluu korttipakan valinta sekä kysymysten kysyminen.

## Korttipakan valinta
Aluksi sovellus näyttää input-kansion tiedostot, joista käyttäjä voi valita sopivan syötetiedoston. Lisäksi käyttäjälle annetaan mahdollisuus valita toinen kansio tai muu tiedosto. 

## Kysymysten kysyminen
Kun syötetiedosto ja korttipakka on valittu, ohjelma käy läpi pakan kysymykset yksi kerrallaan. Kunkin kysymyksen kohdalla käyttäjä voi pyytää sovellusta näyttämään oikea vastaus valitsemalla painiketta _Proceed_, tai keskeyttää ohjelman suoritus klikkaamalla painiketta _Exit_.

Tämä prosessi voidaan havainnollistaa sekvenssidiagrammin avulla:
```mermaid
sequenceDiagram
    Play->>UI: The question is: 1+1=? Proceed or exit?
    UI-->>GUI: The question is: 1+1=? Proceed or exit?
    GUI-->>UI: Proceed
    UI-->>Play: Proceed
    Play->>UI: Question: 2+2=? Answer: 4.  Proceed or exit?
    UI-->>GUI: Question: 2+2=? Answer: 4.  Proceed or exit?
    GUI-->>UI: exit
    UI-->>Play: exit
    Play->>UI: Game over
    UI-->>GUI: Game over
```    
