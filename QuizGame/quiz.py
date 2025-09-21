quizzes = {
    "What is the chemical element with the symbol Fe?":[
        "A. Iron",
        "B. Gold",
        "C. Uranium",
        "D. Oxygen",
    ],
    "Which planet in our solar system is known as the 'Red Planet'?":[
        "A. Earth",
        "B. Jupiter",
        "C. Venus",
        "D. Mars",
    ],
    "Which planet is closest to the sun?":[
        "A. Venus",
        "B. Mercury",
        "C. Earth",
        "D. Uranus",
    ],
    "What scientific theory explains the origin of the universe?":[
        "A. The Big Bang Theory",
        "B. Flat Earth Theory",
        "C. Geocentric Model",
        "D. Heliocentric Model",
    ],
    "What is the name of the world's first artificial satellite":[
        "A. Hubble Space Telescope",
        "B. GPS Satellites",
        "C. Sputnik 1",
        "D. International Space Station (ISS)",
    ]
}

answers = ['A', 'D', 'B', 'A', 'C']
total = 0
i = -1

for quiz, options in quizzes.items():
    print(quiz)
    i += 1
    for option in options:
        print(option)
    
    answer = input("Answer: ").upper()
    if answer == answers[i]:
        total += 1
    print()

print(f"You answered {total} questions right!")