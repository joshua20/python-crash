from survey import AnonymousSurvey

#define a question, and make a survey
question="what language did you first learn to speak?"
language_survey=AnonymousSurvey(question)

#show the question and store responses to the question

language_survey.show_question()
print("enter 'q' at anytime to quit.\n")
while True:

    response=input("language: ")
    if response == 'q':
        break
    language_survey.store_response(response)

#show the survey results
print("\n Thank you to everyone who participated in the survey!")
language_survey.show_result()
