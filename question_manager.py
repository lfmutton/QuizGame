import json

class QuestionManager:
    def __init__(self, questions_file):
        self.questions_file = questions_file
        self.questions = self.load_questions()
        
    def load_questions(self):
        with open(self.questions_file, 'r') as f:
            return json.load(f)
            
    def get_questions(self):
        return self.questions
        
    # def add_question(self, question, options, answer):
    #     new_question = {
    #         'question': question,
    #         'options': options,
    #         'answer': answer
    #     }
    #     self.questions.append(new_question)
    #     self.save_questions()
        
    # def save_questions(self):
    #     with open(self.questions_file, 'w') as f:
    #         json.dump(self.questions, f, indent=2)