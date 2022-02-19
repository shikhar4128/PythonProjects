import random

capitals_dict = {
'Alabama': 'Montgomery','Alaska': 'Juneau','Arizona': 'Phoenix','Arkansas': 'Little Rock','California': 'Sacramento',
'Colorado': 'Denver','Connecticut': 'Hartford','Delaware': 'Dover','Florida': 'Tallahassee','Georgia': 'Atlanta',
}

capitals_list=list(capitals_dict.items())
def guessCapital():
    state,capital=random.choice(capitals_list)
    while True:
        cap=input(f'Please enter the capital city of {state}\n')
        if cap.lower()==capital.lower():
            print("Correct answer .Good job!!")
            break
        elif cap.lower()=='exit':
            print(f'The correct answer is {capital}. Goodbye!!')
            break
        else:
            print('That is not the correct answer .Please try again')



guessCapital()