# 🎯 Ultimate Number Guessing Game

An interactive console-based game built using Python where players guess a hidden number across multiple levels and earn points based on performance.

---

## 🚀 Overview
This game challenges the player to guess a randomly generated number within a limited number of attempts.  
As the player progresses, the difficulty increases with larger number ranges and more attempts.

---

## 🎮 Features
- 🎯 Multiple levels with increasing difficulty  
- 🧠 Intelligent hints (Too High / Too Low)  
- 🏆 Score system based on remaining attempts  
- 🔄 Replay option after game over  
- 💻 Clean terminal interface with screen refresh  

---

## ⚙️ How the Game Works
1. The game starts at Level 1.
2. Each level has:
   - A number range
   - Limited attempts
3. The player guesses the number:
   - 📈 Too low → try higher  
   - 📉 Too high → try lower  
   - ✅ Correct → move to next level  
4. Points are awarded based on remaining attempts.
5. Game continues until:
   - All levels are completed 🎉  
   - Or player loses ❌  

---

## 🧩 Levels Configuration
| Level | Range        | Attempts | Difficulty |
|------|-------------|---------|------------|
| 1    | 1 – 10      | 4       | Easy       |
| 2    | 1 – 50      | 6       | Medium     |
| 3    | 1 – 100     | 8       | Medium+    |
| 4    | 1 – 500     | 10      | Hard       |
| 5    | 1 – 1000    | 12      | Expert     |

---

## 🛠 Technologies Used
- Python 🐍  
- Built-in Libraries:
  - `random` 🎲 (number generation)
  - `os` 💻 (clear screen)
  - `time` ⏳ (delay effects)

---

## ▶️ How to Run
1. Make sure Python is installed  
2. Run the file:
```bash
python number_guessing_game.py