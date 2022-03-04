#Write a program that reads the data from this CSV file and creates a new file called high_scores.csv in which each row contains the player’s
#name and their highest score.

import csv

def readScore(file_location):
    with open(file_location,encoding='utf-8-sig') as file:
        reader=csv.DictReader(file)
        score=[row for row in reader]
        return score

score=readScore('scores.csv')

def processData(score):
    high_score={}
    for item in score:
        name=item['name']
        score=item['score']

        if name not in high_score:
            high_score[name]=score
        elif score > high_score[name]:
            high_score[name]=score

    return high_score

high_score=processData(score)

def writeFile(high_score,new_file):
    with open(new_file,'w',newline='') as file:
        writer=csv.DictWriter(file,fieldnames=['name','score'])
        writer.writeheader()
        for name in high_score.items():
            rd = {'name': name[0], 'score': name[1]}
            writer.writerow(rd)

writeFile(high_score,'high_scores.csv')

