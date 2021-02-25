class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list # a list of object
        self.score = 0


    def next_question(self):
        current_question = self.question_list[self.question_number]

        player_answer = input(f"Q.{self.question_number + 1}:{current_question.text} (True/False): ")
        self.check_answer_correct(player_answer)
        #note you can use another method in one method
        self.question_number += 1

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer_correct(self, player_answer):
        current_question = self.question_list[self.question_number]
        if player_answer.lower() == current_question.answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong")
        print(f"The correct answer was {player_answer}")
        print(f"Your current score is {self.score}/{self.question_number + 1}")
        print('\n')

