```mermaid
sequenceDiagram
    main->>HKLLaitehallinto: create
    main->>Lataajalaite: create
    main->>Lukijalaite: create
    main->>Lukijalaite: create
    HKLLaitehallinto->>rautatientori: lisaa_lataaja
    HKLLaitehallinto->>ratikka6: lisaa_lukija
    HKLLaitehallinto->>bussi244: lisaa_lukija
    main->>Kioski: create
    Kioski->>matkakortti: buy
    rautatientori->>matkakortti: lataa_arvoa(3)
    ratikka6->>matkakortti: osta_lippu(0)
    bussi244->>matkakortti: osta_lippu(2)
    

```
