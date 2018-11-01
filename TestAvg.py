#Mary Green
#03/18/2018
#Unit 6
#TestAvg.py
#A program that asks the user to enter 5 test scores, display a letter grade
#for each score and the average test score.


def main():
    Score_1 = getValidScore()
    Score_2 = getValidScore()
    Score_3 = getValidScore()
    Score_4 = getValidScore()
    Score_5 = getValidScore()
    calcAverage(Score_1,Score_2,Score_3,Score_4,Score_5)




def getValidScore():
    Score=float(input('Enter a test score:'))
    while isValidScore(Score) is False:
       Score=float(input('ERROR: Enter a valid test score:')) 
    if isValidScore(Score) is True:
       grade = determineGrade(Score)
       print ('This is your test score:', Score)
       print ('This is your letter grade:', grade)
       return Score
def isValidScore(Score):
    if Score >= 0 and Score <= 100:
        return True
    else:
        return False


def calcAverage(Score_1,Score_2,Score_3,Score_4,Score_5):
    Sum = Score_1 + Score_2 + Score_3 + Score_4 + Score_5
    Average = Sum / 5
    grade = determineGrade(Average)
    print ('This is your test score average:', Average)
    print ('This is your Average letter grade:', grade)

def determineGrade(S):
    if S >= 90 and S <= 100:
        return "A"
    if S >= 80 and S <= 89:
        return "B"
    if S >= 70 and S <= 79:
        return "C"
    if S >= 60 and S <= 69:
        return "D"
    if S < 60:
        return "F"
    
    
    
    




main()


#Input test scores: 78, 87, 76, 96, 87
# Output 78 = C, 87 = B, 76 = C, 96 = A, 87 = B
#Output Average score is 84.8, Average letter grade B









