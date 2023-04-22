```mermaid
sequenceDiagram
    Play->>UI: The question is: 1+1=? Proceed or exit?
    UI-->>GUI: The question is: 1+1=? Proceed or exit?
    GUI-->>UI: Proceed
    UI-->>Play: Proceed
    Play->>UI: Question: 1+1=? Answer: 2.  Proceed or exit?
    UI-->>GUI: Question: 1+1=? Answer: 2.  Proceed or exit?
    GUI-->>UI: exit
    UI-->>Play: exit
    Play->>UI: Game over
    UI-->>GUI: Game over
```    
