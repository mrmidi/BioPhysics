import os
import django
import json

# Set up the Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BioPhysics.settings")
django.setup()

from quiz.models import Topic, Question, Answer

def import_json_to_django(json_file_path):
    # Open and load the JSON file
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    # Loop through questions
    for q_data in data['questions']:
        # Create a new question instance
        question = Question(text=q_data['text'])
        question.save()

        # Loop through options for this question
        for option_data in q_data['options']:
            # Create a new answer instance
            answer = Answer(
                text=option_data['text'],
                is_correct=option_data['isCorrect'],
                question=question
            )
            answer.save()

    print("Data imported successfully!")

# Usage
import_json_to_django('bf1.json')
