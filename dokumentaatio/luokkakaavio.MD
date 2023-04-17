**```mermaid
classDiagram
    Play "1" --> "1" App 
    App "1" --> "1" UI
    UI "1" --> "1" App
    class App{
        aloitusruutu
        input_dir
        input_path 
        data
        filelist
    }
    class Play{
        app
    }
    class UI{
        currently_empty
    }


```
**
