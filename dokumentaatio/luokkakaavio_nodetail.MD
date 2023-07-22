classDiagram
    class App
    class Play
    class UserInterface
    class Database
    class DatabaseUserInteractions
    class DatabaseFileHandling
    class DatabaseInteractions
    
    App --> UserInterface
    App --> Play
    Play --> App
    Play --> UserInterface
    Play --> Database
    Database --> DatabaseInteractions
    Database --> DatabaseFileHandling
    Database --> DatabaseUserInteractions
