sequenceDiagram
    participant main
    participant Machine
    participant FuelTank
    participant Engine
    main ->>Machine
    Machine ->>FuelTank: fill 40L
    Machine ->>Engine: start
