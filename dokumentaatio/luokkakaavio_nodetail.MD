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
    FileSelectionView -- tk
    Database --|> DatabaseInteractions
    Database --|> DatabaseFileHandling
    Database --|> DatabaseUserInteractions
    App --|> UserInterface
    App --|> FileSelectionView
    Play --|> UserInterface
    App --|> Database
    Play --|> App
```
