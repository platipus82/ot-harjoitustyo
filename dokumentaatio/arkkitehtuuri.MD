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
    Play "1" --> "1" App 
    Play "1" --> "1" Database
    Database "1" --> "1" UserInterface 
    DatabaseFileHandling o-- DatabaseInteractions
    DatabaseInteractions o-- DatabaseUserInteractions
    Database o--|> DatabaseFileHandling
    Database o--|> DatabaseInteractions
    Database o--|> DatabaseUserInteractions

    Play "1" --> "1" UserInterface 
    App "1" --> "1" UserInterface
    App "1" --> "1" Play
    UserInterface "1" --> "1" App
    UserInterface "1" --> "1" MainView
    UserInterface "1" --> "1" FileSelectionView
    MainView "1" --> "1" FileSelectionView
    FileSelectionView "1" --> "1" UserInterface
    FileSelectionView "1" --> "1" MainView
    MainView "1" --> "1" UserInterface
    FileSelectionView "1" --> "1" Window_parameters
    MainView "1" --> "1" Window_parameters
    
    Window_parameters "1" --> "1" MainView
    Window_parameters "1" --> "1" FileSelectionView

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
    
    class DatabaseFileHandling{
        - sql_db_path: str
        - db_dir: str
        - db_path: str
        - data: list

        + __init__(sql_db_path: str, db_dir: str, db_path: str)
        + make_new_sql_db_file()
        + make_db_dir()
        + make_new_db_file()
        + write_to_db(output_csv_file: str, rows_to_write: list, mode: str)
        + write_to_sql_db(rows_to_write: list)
        + write_file(output_csv_file: str, rows_to_write: list, mode: str)
    }
    class DatabaseInteractions{
        - sql_db_path: str
        - db_path: str
        - data: list

        + __init__(sql_db_path: str, db_path: str)
        + tell_db_colnames(): list
        + get_db_data(): bool
        + get_sql_db_data()
    }
    class DatabaseUserInteractions{
        - data: list
        - summary: str

        + __init__()
        + give_summary_data(): list
        + give_summary(): str
        + give_summary_of_last_session(): str
        + __describe_n_of_users(dat: list): str
        + __describe_n_of_input_files(dat: list): str
        + __describe_total_time(dat: list): str
        + __total_checked_questions(dat: list): str
        + __total_answered_questions(dat: list): str
        + __correctly_answered_questions(dat: list): str
        + __percentage_of_correct(dat: list): str
        + give_summary_of_db(): str
        + make_summary()
    }
    class Database{
        - db_dir: str
        - output_allowed: bool
        - db_path: str
        - data: list
        - sql_db_path: str
        - summary: str

        + __init__(output_allowed: bool)
        + make_new_db_file()
        + make_new_sql_db_file()
        + write_file(output_csv_file: str, rows_to_write: list, mode: str)
        + get_db_data(): bool
        + get_sql_db_data()
        + give_summary_data(): list
        + give_summary(): str
        + give_summary_of_last_session(): str
        + __describe_n_of_users(dat: list): str
        + __describe_n_of_input_files(dat: list): str
        + __describe_total_time(dat: list): str
        + __total_checked_questions(dat: list): str
        + __total_answered_questions(dat: list): str
        + __correctly_answered_questions(dat: list): str
        + __percentage_of_correct(dat: list): str
        + give_summary_of_db(): str
        + make_summary()
    }


    
    class UserInterface{
        show_output()
        ask_for_input()
        ask_for_input_file()
    }

    class MainView{
        show_output()
        ask_for_input()
        ask_for_file()
        set_result()

    }
    
    class FileSelectionView{
        window
        root
        width
        height
        screen_width
        screen_height
        input_path
        check_that_input_folder_exists()
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
