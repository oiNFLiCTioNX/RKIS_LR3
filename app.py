from flask import Flask, render_template

app = Flask(__name__)

portfolio_data = {
    "about": {
        "name": "Александр Козлов",
        "bio": [
            "Приветствую! Меня зовут Александр Козлов.",
            "Я студент обучающийся на IT направлении в Липецком Государственном Техническом Университете.",
            "Родился 25.04.2006 в г. Липецк, начинающий программист с навыками Python и C. Увлекаюсь видеоиграми и планирую создавать свои собственные."
        ]
    },
    "skills": [
        "- Python",
        "- Flask",
        "- C/C#",
        "- HTML/CSS"
    ],
    "projects": [
        {
            "title": "Проект 1",
            "image": "images/project1.png",
            "description": "Простая RPG игра на Python с опцией генерации карты.",
            "github_link": "https://github.com/oiNFLiCTioNX/RKIS_LR1 "
        },
        {
            "title": "Проект 2",
            "image": "images/project2.png",
            "description": "Продолжение первого проекта с возможностью прохождения игры, несколькими картами и другими возможностями.",
            "github_link": "https://github.com/oiNFLiCTioNX/RKIS_LR2 "
        }
    ],
    "contact": {
        "email": "sashakozlov185@gmail.com",
        "telegram": "@bigsanyatape"
    }
}

@app.route('/')
def home():
    return render_template('index.html', data=portfolio_data)

if __name__ == '__main__':
    app.run(debug=True)
