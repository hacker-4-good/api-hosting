from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI() 

origin = [
    'http://localhost:5173',
    'https://question-bank-application.netlify.app'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origin,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

data = [
    {
        'question': 'What is the speed of the light',
        'subject': 'Physics',
        'topic': 'Waves',
        'difficulty': 'Easy',
        'marks': 4
    },
    {
        "question": "What is the formula for kinetic energy?",
        "subject": "Physics",
        "topic": "Mechanics",
        "difficulty": "Easy",
        "marks": 4
    },
    {
        "question": "What is the first law of thermodynamics?",
        "subject": "Physics",
        "topic": "Thermodynamics",
        "difficulty": "Medium",
        "marks": 5
    },
    {
        "question": "What is the relationship between electric charge and electric force?",
        "subject": "Physics",
        "topic": "Electromagnetism",
        "difficulty": "Hard",
        "marks": 6
    },
    {
        "question": "What is the formula for the wavelength of light?",
        "subject": "Physics",
        "topic": "Waves",
        "difficulty": "Medium",
        "marks": 5
    },
    {
        "question": "What is the relationship between mass and energy according to Einstein's famous equation?",
        "subject": "Physics",
        "topic": "Relativity",
        "difficulty": "Hard",
        "marks": 6
    },
    {
        "question": "What is the difference between nuclear fission and nuclear fusion?",
        "subject": "Physics",
        "topic": "Nuclear Physics",
        "difficulty": "Medium",
        "marks": 5
    },
    {
        "question": "What are the four fundamental forces of nature?",
        "subject": "Physics",
        "topic": "Forces",
        "difficulty": "Easy",
        "marks": 4
    },
    {
        "question": "What is the principle of superposition for waves?",
        "subject": "Physics",
        "topic": "Waves",
        "difficulty": "Medium",
        "marks": 5
    },
    {
        "question": "What is the Doppler effect?",
        "subject": "Physics",
        "topic": "Waves",
        "difficulty": "Medium",
        "marks": 5
    },
    {
        "question": "What is the difference between a scalar quantity and a vector quantity?",
        "subject": "Physics",
        "topic": "Measurement",
        "difficulty": "Easy",
        "marks": 4
    },
    {
        "question": "What is the difference between speed, velocity, and acceleration?",
        "subject": "Physics",
        "topic": "Motion",
        "difficulty": "Easy",
        "marks": 4
    },
    {
        "question": "What is the law of conservation of energy?",
        "subject": "Physics",
        "topic": "Energy",
        "difficulty": "Medium",
        "marks": 5
    },
    {
        "question": "What is the relationship between force, mass, and acceleration?",
        "subject": "Physics",
        "topic": "Newton's Laws of Motion",
        "difficulty": "Medium",
        "marks": 5
    },
    {
        "question": "What is the difference between mechanical waves and electromagnetic waves?",
        "subject": "Physics",
        "topic": "Waves",
        "difficulty": "Medium",
        "marks": 5
    },
    {
        "question": "What is the photoelectric effect?",
        "subject": "Physics",
        "topic": "Quantum Mechanics",
        "difficulty": "Hard",
        "marks": 6
    },
    {
        "question": "What is the wave-particle duality?",
        "subject": "Physics",
        "topic": "Quantum Mechanics",
        "difficulty": "Hard",
        "marks": 6
    }, 
    {
        "question": "What is the difference between a conductor and an insulator?",
        "subject": "Physics",
        "topic": "Electromagnetism",
        "difficulty": "Medium",
        "marks": 5
    },
    {
        "question": "What is the difference between a series circuit and a parallel circuit?",
        "subject": "Physics",
        "topic": "Electromagnetism",
        "difficulty": "Medium",
        "marks": 5
    },
    {
        "question": "What is the Schrödinger equation?",
        "subject": "Physics",
        "topic": "Quantum Mechanics",
        "difficulty": "Hard",
        "marks": 6
    }
]

query = list()

@app.get('/all_question')
async def all_question():
    return data
