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
