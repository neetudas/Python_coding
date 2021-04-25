import random
import os
import shutil

#50 countries  and their capitals
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 
'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 
'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}
 
#Make a dir to store the question papers in the current path, DELETE if path exists
current_path = os.getcwd()
file_path = os.path.join(current_path + "/random_quizes/")
if os.path.exists(file_path) and os.path.isdir(file_path):
    shutil.rmtree(file_path)
os.mkdir(file_path)

#Make a dict with question and 3 choices with one correct
question  = {}

for quest in capitals:
    all_answers =[] 
    answer = []
    all_answers = list(capital for capital in list(capitals.values()) if capital != capitals[quest])
    answer = list(all_answers[i] for i in random.sample(range(0, 49), 2)) # Append anyother 2 ans
    answer.append(capitals[quest]) #Append the correct answer 
    question[quest] = answer # store the question and 3 choices in a dict 

#shuffle each time the answers in the dict and write it on 35 diff files
for question_paper in range(1,35):
        question_number = 1
        temp_qp = ()
        f = open(file_path + "Question_Paper " + str(question_paper), 'a+')
        #shuffle the answer choices
        for i in question:
            random.shuffle(question[i])
        # create a temp tupule and shuffle the position of questions to be printed 
        temp_qp = list(question.items())
        random.shuffle(temp_qp)
        
        # write the question and choices in the file
        for key,choices in temp_qp:  
            f.write(str(question_number) + ">>  What is the capital of " + key + "?")
            f.write("\n")
            for choice in choices:
                f.write("\t" + choice + "\n")
            f.write("\n\n")
            question_number = question_number + 1
        f.close()


        







# put all 50 questions in 35 files in random order




