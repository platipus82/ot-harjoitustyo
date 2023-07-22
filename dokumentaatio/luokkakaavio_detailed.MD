```mermaid
classDiagram
    class Database
    class DatabaseInteractions
    class DatabaseFileHandling
    class DatabaseUserInteractions

    Database --* DatabaseInteractions
    Database --* DatabaseFileHandling
    Database --* DatabaseUserInteractions
    DatabaseInteractions --|> DatabaseFileHandling
    DatabaseInteractions --|> DatabaseUserInteractions
    DatabaseFileHandling --|> DatabaseUserInteractions


```
