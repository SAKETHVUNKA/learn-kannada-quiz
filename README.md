# Learn Kannada Quiz 🌿

An interactive Django web application to help people learn and test their Kannada vocabulary through fun word-matching quizzes with audio support.

---

## 📚 About

This project is designed to help users understand, learn, and test their knowledge of Kannada words by matching English words to their correct Kannada equivalents.

Features include:
- ✅ Multiple-choice quizzes for word-to-word matching.
- 🔊 Audio pronunciation for each Kannada option (using Google Text-to-Speech).
- 🎯 Score tracking and high score leaderboard.
- 💡 Simple, responsive UI for an easy learning experience.

---

## 🚀 Features
- English word shown as a question, user selects the correct Kannada word.
- Speaker icons to listen to each Kannada option before selecting.
- Score updates and final score display after each game.
- High score table to motivate learning.
- Automatic cleanup of audio files to keep the server clean.

---

## 🛠️ Tech Stack
- Backend: Django (Python)
- Audio: gTTS (Google Text-to-Speech)
- Frontend: HTML, CSS, Bootstrap
- Database: SQLite (default for Django)

---

## ⚙️ Setup & How to Run

1️⃣ Clone the project into a folder in your local system using:
```bash
git clone https://github.com/SAKETHVUNKA/learn-kannada-quiz.git
```

2️⃣ Open the folder containing the project in your terminal.

3️⃣ Create a virtual environment in the same folder (optional but recommended):
```bash
python -m venv venv
```

4️⃣ Activate the virtual environment:
- Windows:
```bash
venv\Scripts\activate
```
- macOS/Linux:
```bash
source venv/bin/activate
```

5️⃣ Install all required Python modules:
```bash
pip install -r requirements.txt
```

6️⃣ Change current directory to /KK_Hackathon.

7️⃣ Start the web app using:
```bash
python manage.py runserver
```

8️⃣ Open your browser and go to:
```
http://127.0.0.1:8000/start
```
to start using the app.

---

## 💬 Usage
- Start the quiz from the home page.
- Click on speaker icons next to each option to listen to pronunciations.
- Submit answers to progress through questions and see your score.
- Check your high score and replay to improve.

---

## ✨ Future Improvements
- Add different levels (Beginner, Intermediate, Advanced).
- Include example images or sentences for context.
- Support additional languages (e.g., Telugu, Tamil).

---

## 👥 Authors

 - [Naga Saketh V](https://github.com/SAKETHVUNKA)
 - [Space-Gamer](https://github.com/Space-Gamer)
 - [Manas](https://github.com/Manas-Gowda)
 - [Nandan](https://github.com/NANDANNPRABHU)

---

## 📄 License
This project is open source and available under the MIT License.

---

🎉 **Happy Learning! Learn Kannada the fun and interactive way.**