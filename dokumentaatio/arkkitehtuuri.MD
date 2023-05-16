# Arkkitehtuurikuvaus


## Rakenne
Ohjelman rakenne on jäsennelty kahteen kerrokseen. Koodin pakkausrakenne on seuraavanlainen:


```mermaid
classDiagram
    main "1" --> "1" processes 
    processes "1" --> "1" repositories 
    repositories "1" --> "1" processes 
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
```
Pakkaus _ui_ sisältää käyttöliittymästä vastaavan koodin. Pakkaus _processes_ sisältää kaiken muun koodin joka vastaa sovelluslogiikasta,  suorituksesta, sekä tiedon pysyväistallennuksesta. Pakkaus _main_ sisältää ohjelman käynnistyskoodin joka on eriytetty omaksi skriptiksi _flashcards.py_. Pakkaus _repositories_ sisältää  pysyväistallennetun tiedon _.csv_ tai _sql_ muodossa. Pakkaus _inputs_ sisältää korttipakat eli syötetiedostot.


## Sovelluslogiikka
Sovelluksen rakenne modostuu seitsemästä luokasta: _Play_, _Database_, _App_, _UI_, _GUI_, _GUI_input_file_selection_ ja _Window_parameters_. Luokat kuvaavat sovelluksen toiminnallisia kokonaisuuksia ja niiden keskinäiset suhteet voidaan kuvata luokkadiagrammin avulla: 
Luokkadiagrammi: 

```mermaid
classDiagram
    Play "1" --> "1" App 
    Play "1" --> "1" Database
    Database "1" --> "1" UI 
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
        default_input
        output_allowed
        input_dir
        input_path 
        data
        filelist       
        set_input_dir()
        set_parameters()
        give_input_filename()
        get_input_filelist()
        set_input_path()
        set_input_path_default()
        get_input_data()
        shuffle_questions()
    }
    class Play{
        use_default_input
        output_allowed
        start_time
        end_time
        mode
        __exit 
        game
        questions_n_total
        questions_n_checked
        questions_n_answered
        questions_n_correct
        __ui
        database      
        set_mode()
        update_question_counters()
        ask()
        save_results()       
    }
    
    class Database{
        db_dir
        output_allowed
        db_path
        data
        sql_db_path 
        summary
        
        make_new_db_file()
        make_new_sql_db_file()
        make_db_dir()
        tell_db_colnames()
        write_to_db()
        write_to_sql_db()
        write_file()
        get_db_data()
        get_sql_db_data()
        make_summary()
        give_summary_data()
        print_summary()
        give_summary_of_last_session()
        give_summary_of_db()
        give_summary()   
        __describe_n_of_users()
        __describe_n_of_input_files()
        __describe_total_time()
        __total_checked_questions()
        __total_answered_questions()
        __correctly_answered_questions()
        __percentage_of_correct()
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
