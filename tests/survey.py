#class to be tested

class AnonymousSurvey:
    '''collect anonymous answers to a survey'''
    def __init__(self,question):
        '''store a question and prepare to store responses'''
        self.question=question
        self.responses=[]

    def show_question(self):
        '''show the survey question'''
        print(self.question)

    def store_response(self, new_response):
        '''store a single response'''
        self.responses.append(new_response)

    def show_result(self):
        '''print all responses that have been given'''
        print("survey result")
        for response in self.responses:
            print(f"- {response}")

