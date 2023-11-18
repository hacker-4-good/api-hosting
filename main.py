from fastapi import FastAPI 

app = FastAPI()

data = {
    1: {
        'question': 'What is the speed of the light',
        'subject': 'Physics',
        'topic': 'Waves',
        'difficulty': 'Easy',
        'marks': 5
    },
    2: {
        "question": "What is the formula for kinetic energy?",
        "subject": "Physics",
        "topic": "Mechanics",
        "difficulty": "Easy",
        "marks": 3
    },
    3: {
        "question": "What is the first law of thermodynamics?",
        "subject": "Physics",
        "topic": "Thermodynamics",
        "difficulty": "Medium",
        "marks": 4
    },
    4: {
        "question": "What is the relationship between electric charge and electric force?",
        "subject": "Physics",
        "topic": "Electromagnetism",
        "difficulty": "Hard",
        "marks": 5
    },
    5: {
        "question": "What is the formula for the wavelength of light?",
        "subject": "Physics",
        "topic": "Waves",
        "difficulty": "Medium",
        "marks": 3
    },
    6: {
        "question": "What is the relationship between mass and energy according to Einstein's famous equation?",
        "subject": "Physics",
        "topic": "Relativity",
        "difficulty": "Hard",
        "marks": 5
    },
    7: {
        "question": "What is the difference between nuclear fission and nuclear fusion?",
        "subject": "Physics",
        "topic": "Nuclear Physics",
        "difficulty": "Medium",
        "marks": 4
    },
    8: {
        "question": "What are the four fundamental forces of nature?",
        "subject": "Physics",
        "topic": "Forces",
        "difficulty": "Easy",
        "marks": 3
    },
    9: {
        "question": "What is the principle of superposition for waves?",
        "subject": "Physics",
        "topic": "Waves",
        "difficulty": "Medium",
        "marks": 4
    },
    10: {
        "question": "What is the Doppler effect?",
        "subject": "Physics",
        "topic": "Waves",
        "difficulty": "Medium",
        "marks": 3
    },
    11: {
        "question": "What is the difference between a scalar quantity and a vector quantity?",
        "subject": "Physics",
        "topic": "Measurement",
        "difficulty": "Easy",
        "marks": 3
    }
}

@app.get('/all_question/{difficulty}')
async def get_all_question(difficulty):
    query = dict()
    for i in data:
        if data[i]['difficulty'].lower() == difficulty:
            query[i] = data[i]
    return query
