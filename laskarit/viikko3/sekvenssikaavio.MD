```mermaid
sequenceDiagram
    main->>Machine: create
    Machine->>FuelTank: has
    Machine->>FuelTank: fill 40L
    Machine->>Engine: has   
    Machine->>Engine: start
    main->>Machine: drive
```
