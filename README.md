# minigame
미니게임 모음집

 <img src="/image/1.png" alt="minigame main" width="300px"></img>

### 주의사항

- 이 게임은 python으로 제작하였습니다.
- pygame, random, time, copy의 모듈이 필요합니다.(없다면 실행이 안됩니다)
-----------------------------------------------------------------------
-----------------------------------------------------------------------
## 드래곤볼 게임
 <img src="/image/2.png" alt="dragonball main" width="300px"></img>

- 드래곤볼 게임은 턴제 게임입니다. 
- 영어로 a(기모으기, gathering), s(공격, attack), d(방어, Shield)를 누르면 컴퓨터도 세 개의 행동중 하나를 합니다.
- a(기모으기, gathering) : GatherCount가 올라갑니다.
- s(공격, attack) : GatherCount 1개가 감소하면서 공격을 합니다.
- d(방어, Shield) : 방어막으로 상대 공격을 막습니다.
- a(기모으기, gathering)를 5번 성공시키면 특수 공격을 사용할 수 있습니다.
- 특수 공격은 특수 공격으로만 막을 수 있습니다.

#### 승리조건

- 상대가 기를 모을 때, 공격을 적중시킨다.
- special 공격을 가한다.
-----------------------------------------------------------------------
## 땅따먹기 게임
 <img src="/image/3.png" alt="eatground main" width="300px"></img>

- 땅따먹기 게임은 총 7stage로 이루어져 있습니다.
- score 옆에 적힌 퍼센트를 100%로 채우면 다음 stage로 넘어갑니다.
- 화살표를 이동할 수 있습니다.
- 적을 피해 땅을 먹어야 합니다.
- 땅을 먹기 위해서는 땅에서 출발해 땅으로 이동을 성공해야만 먹을 수 있습니다.
- 중간에 적을 만나면 패배입니다.

#### 플레이 장면
 <img src="/image/4.png" alt="eatground 1" width="250px"></img>  
 <img src="/image/5.png" alt="eatground 2" width="250px"></img>  
 <img src="/image/6.png" alt="eatground 3" width="250px"></img>  
 <img src="/image/7.png" alt="eatground 4" width="250px"></img>  
 <img src="/image/8.png" alt="eatground 5" width="250px"></img>  
 
#### 땅따먹기 게임의 아쉬운 점

- 모든 오류를 잡았지만 게임 설계상 시간이 오래 걸리는 알고리즘을 사용해서 게임이 렉이 걸린다.
