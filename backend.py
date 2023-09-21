class Question:
    def __init__(self,que,correct_ans):
        self.que=que
        self.correct_ans=correct_ans
    def display(self):
        print(self.que)

    def correct(self,user_ans):
        return user_ans==self.correct_ans.lower()
    
class Quiz:
    def __init__(self,question_data):
        self.questions=[]
        for que,correct_ans in question_data:
            self.questions.append(Question(que,correct_ans))
        self.score=0
        self.current_question=0

    def next_question(self):
        if self.current_question<len(self.questions):
            question=self.questions[self.current_question]
            self.current_question+=1
            return question
        else:
            return None
    def check_ans(self,user_ans):
        current_question=self.questions[self.current_question-1]
        if current_question.correct(user_ans):
            self.score+=2
        else:
            self.score-=1

    def question_remain(self):
         return self.current_question < len(self.questions)
    def display_score(self):
        print(self.score)


    
question_data = [

( "A slug's blood is green.","True"),

( "The loudest animal is the African Elephant.", "False"),

( "Approximately one quarter of human bones are in the feet.", "True"),

( "The total surface area of a human lungs is the size of a football pitch.",  "True"),

( "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.",  "True"),

( "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.", "False"),

("It is illegal to pee in the Ocean in Portugal.", "True"),

( "You can lead a cow down stairs but not up stairs.",  "False"),

( "Google was originally called 'Backrub'.", "True"),

( "Buzz Aldrin's mother's maiden name was 'Moon'.",  "True"),

( "No piece of square dry paper can be folded in half more than 7 times.",  "False"),

( "A few ounces of chocolate can to kill a small dog.",  "True")

]

quiz=Quiz(question_data)
print("Quiz Game")
while quiz.question_remain():
    current_question=quiz.next_question()
    current_question.display()
    user_ans=input("enter the ans  ")
    quiz.check_ans(user_ans)

quiz.display_score()










