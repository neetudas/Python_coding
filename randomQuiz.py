#This Script will generate 35 question and answer sheets, with multiple choice qusetions which are suffeled

import os, glob
import random


#Declaring state and capital dictionary

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New'
'Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West'
'Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

#Will crate a folder for storing all question and answers sheeets
if os.path.exists('./Questions'):
   os.chdir('./Questions')
   for file in glob.glob('.\*'):
    os.unlink(file)
      #  print (os.getcwd())
else:
    os.makedirs('./Questions')
    os.chdir('./Questions')
    print (os.getcwd())

totalQuestionPapers = 35
totalQusetions = 50

for questionNum in range(totalQuestionPapers):
    question = open('CapitalQuestion%s.txt' %(questionNum+1), 'w')
    question.write('Name \n\nclass\n\n')
    question.write((' '*40) + 'State Capital form %s' %(questionNum+1))   
    
    answer = open('CapitalAnswers%s.txt' %(questionNum+1), 'w')
    answer.write((' '*40) + 'State Capital Answer Sheet %s ' %(questionNum+1) )
    
    states = list(capitals.keys())
    random.shuffle(states)

    for questionNum in range(totalQusetions):
        stateName = states[questionNum]
        #print (stateName)   
        capitalName = capitals[stateName]
        allCapitals = list(capitals.values())
        allCapitals.remove(capitalName) 
        
        threeWrongOptions = random.sample(allCapitals, 3)
        totalOptions = threeWrongOptions + [capitalName]
        random.shuffle(totalOptions)
        
        question.write('\n\n')
        question.write('%s Which is the capital of %s ' %(questionNum+1, stateName))
        question.write('\n')
        
        answer.write('%s Correct answer is \n' %(questionNum+1))
        answer.write(capitalName)
        answer.write('\n\n')
        
        for options in range(4):
            question.write('%s %s \n' %('ABCD'[options], totalOptions[options]))
        
question.close()
        #answer.write('%s Correct Answer is ' + capitalName[questionNum]) 
answer.close()