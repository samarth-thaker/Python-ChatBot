import random
R_Eating = "I don't eat anything"
R_Advice = "I would type the same in google"
def unknown():
    response = ['Could you please rephrase that?',
                '...',
                'What does that mean?'][random.randrange(3)]
    return response