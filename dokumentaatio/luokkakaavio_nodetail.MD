```mermaid
classDiagram
    class UserInterface
    class MainView
    class DatabaseUserInteractions
    class DatabaseInteractions
    class DatabaseFileHandling
    class Window_parameters

    UserInterface --|> MainView
    UserInterface --|> DatabaseUserInteractions
    MainView --|> DatabaseInteractions
    DatabaseUserInteractions --|> DatabaseInteractions
    DatabaseFileHandling --|> DatabaseInteractions
    DatabaseUserInteractions --|> DatabaseFileHandling
    UserInterface --|> Window_parameters
    MainView --|> Window_parameters
```
