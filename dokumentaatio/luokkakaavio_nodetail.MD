```mermaid
classDiagram
    class App
    class Play
    class UserInterface
    class Database
    class DatabaseInteractions
    class DatabaseFileHandling
    class DatabaseUserInteractions

    App --> UserInterface
    App --> Play
    Play --> UserInterface
    Play --> Database
    Database --> DatabaseInteractions
    Database --> DatabaseFileHandling
    Database --> DatabaseUserInteractions
    DatabaseUserInteractions --> DatabaseInteractions
    DatabaseFileHandling --> DatabaseInteractions
    UserInterface --> MainView
    UserInterface --> FileSelectionView
```
