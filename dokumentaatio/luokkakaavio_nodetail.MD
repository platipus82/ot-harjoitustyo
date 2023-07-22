```mermaid
classDiagram
    class UserInterface
    class MainView
    class DatabaseUserInteractions
    class DatabaseInteractions
    class DatabaseFileHandling
    class WindowParameters

    UserInterface --|> MainView
    UserInterface --|> DatabaseUserInteractions
    MainView --|> DatabaseInteractions
    DatabaseUserInteractions --|> DatabaseInteractions
    DatabaseFileHandling --|> DatabaseInteractions
    DatabaseUserInteractions --|> DatabaseFileHandling
    UserInterface --|> WindowParameters
    MainView --|> WindowParameters
```
