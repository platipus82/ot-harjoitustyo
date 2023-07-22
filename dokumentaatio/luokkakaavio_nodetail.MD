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

    UserInterface --|> MainView
    MainView --|> WindowParameters
    FileSelectionView --|> WindowParameters
    Database --|> DatabaseInteractions
    Database --|> DatabaseFileHandling
    Database --|> DatabaseUserInteractions
```
