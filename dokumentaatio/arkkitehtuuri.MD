# Arkkitehtuurikuvaus


## Rakenne
Ohjelman rakenne on jäsennelty kahteen kerrokseen. Koodin pakkausrakenne on seuraavanlainen:


```mermaid
classDiagram
    main "1" --> "1" processes 
    processes "1" --> "1" repositories 
    repositories "1" --> "1" processes 
    ui "1" --> "1" processes 
    processes "1" --> "1" ui 
    ui "1" --> "1" repositories 
    repositories "1" --> "1" ui 

    class processes{
    
    }
    
    class repositories{ 
    
    }
    
    class ui{ 
    
    }
    
    class main{ 
    
    }
```
Pakkaus _ui_ sisältää käyttöliittymästä vastaavan koodin. Pakkaus _processes_ sisältää sovelluslogiikasta ja suorituksesta vastaavan koodin. Pakkaus _main_ sisältää ohjelman käynnistyskoodin joka on eriytetty omaksi skriptiksi _flashcards.py_. 



## Sovelluslogiikka
Sovelluksen rakenne modostuu kuudesta luokasta: _Play_, _App_, _UI_, _GUI_, _GUI_input_file_selection_ ja _Window_parameters_. Luokat kuvaavat sovelluksen toiminnallisia kokonaisuuksia ja niiden keskinäiset suhteet voidaan kuvata luokkadiagrammin avulla: 
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
    GUI "1" --> "1" GUI_input_file_selection
    GUI_input_file_selection "1" --> "1" UI
    GUI_input_file_selection "1" --> "1" GUI
    GUI "1" --> "1" UI
    GUI_input_file_selection "1" --> "1" Window_parameters
    GUI "1" --> "1" Window_parameters
    
    Window_parameters "1" --> "1" GUI
    Window_parameters "1" --> "1" GUI_input_file_selection

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
    
    class Window_parameters{
        width
        height 
    }
```

## Päätoiminnallisuudet
Päätoiminnallisuuksiin kuuluu korttipakan valinta sekä kysymysten kysyminen.

### Korttipakan valinta
Aluksi sovellus näyttää input-kansion tiedostot, joista käyttäjä voi valita sopivan syötetiedoston. Lisäksi käyttäjälle annetaan mahdollisuus valita toinen kansio tai muu tiedosto. 

### Kysymysten kysyminen
Kun syötetiedosto ja korttipakka on valittu, ohjelma käy läpi pakan kysymykset yksi kerrallaan. Kunkin kysymyksen kohdalla käyttäjä voi pyytää sovellusta näyttämään oikea vastaus valitsemalla painiketta _Proceed_, tai keskeyttää ohjelman suoritus klikkaamalla painiketta _Exit_.

Tämä prosessi voidaan havainnollistaa sekvenssidiagrammin avulla:
```mermaid
sequenceDiagram

    Play->>UI: The question is: 1+1=? Proceed or exit?
    UI-->>GUI: The question is: 1+1=? Proceed or exit?
    GUI-->>Window_parameters: what are correct window dimensions?
    Window_parameters-->> GUI: 400 x 300
    actor User
    GUI-->>User: The question is: 1+1=? Proceed or exit?
    User-->>GUI: Proceed
    GUI-->>UI: Proceed
    UI-->>Play: Proceed
    Play->>UI: Question: 2+2=? Answer: 4.  Proceed or exit?
    UI-->>GUI: Question: 2+2=? Answer: 4.  Proceed or exit?
    GUI-->>Window_parameters: what are correct window dimensions?
    Window_parameters-->> GUI: 400 x 300
    GUI-->>User: Question: 2+2=? Answer: 4.  Proceed or exit?
    User-->>GUI: exit
    GUI-->>UI: exit
    UI-->>Play: exit
    Play->>UI: Game over
    UI-->>GUI: Game over
    GUI-->>Window_parameters: what are correct window dimensions?
    Window_parameters-->> GUI: 400 x 300
    GUI-->>User: Game over
```    
