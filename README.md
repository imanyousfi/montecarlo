# Monte Carlo Package: 
## Metadata:
Iman Yousfi's Monte Carlo Simulator Project

## Synopsis:

### Installing:
Copy https://github.com/imanyousfi/montecarlo.git, then `pip installe e.`
### Importing:
`from montecarlo import Die, Game, Analyzer`

### Creating dice objects:
- Dice Object: ` Dice_Object = [1,2,3,4,5,6] Dice = Die(Dice_Object)`
- Changing Wieghts: `Dice.weight_change(6,6)`
- Roll: `roll = Dice.roll(10) `

### Playing Games:
- Start Game: `Test_Game = Game(Dice)`
- Play Game: `Test_Game.play(10)`
- Show Game: `Test_DF = Test_Game.show()` 

### Analyzing Games:
- Start Analyzer: `Test_Analyzer = Analyzer(Test_Game)`
- Face Counts per Roll: `Test_Analyzer.face_counts_per_roll()`
- Jackpot: `Test_DF_JP = Test_Analyzer.jackpot()`
- Combo: `Test_DF_Combo = Test_Analyzer.combo()`
