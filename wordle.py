from collections import Counter
import re
import random
def language_dic():
    dic=open("C:\\Users\\ritvikgoel\\OneDrive - KPMG\\Desktop\\English.txt","rt")
    l=dic.read().splitlines()

    for i in range(len(l)):
        if len(l[i]) == 5:
            word_list.append(l[i].lower())
    return word_list

contains=[]
notcontains=[]
word_list=[]



def check(code,guess):
    match=""
    for i in range(5):
        if code[i]==guess[i]:
            match=match+'1'
        elif guess[i] in code:
            match=match+'2'
        else:
            match=match+'3'
    return match
def checkInput(input,guess):
    for i in range(5):
        if input[i] == '1' or input[i] == '2':
            if guess[i] not in contains:
                contains.append(guess[i].lower())
        elif input[i] == '3':
            if guess[i] not in notcontains:
                notcontains.append(guess[i].lower())
def filter(contains,notcontains,word_list):
    lis=[]
    for word in reversed(word_list) :
        for j in notcontains:
            if j.lower() in word.lower():
                word_list.remove(word)
                break

    for word in reversed(word_list) :
        for j in range(len(contains)):
            if contains[j] in word and j==len(contains)-1:
                lis.append(word)
            elif contains[j] not in word:
                word_list.remove(word)
                break
    if len(lis)==0:

        return word_list
    else:
        return lis
def tryguess(code,guess,word_list):
    input=""
    for i in range(6):
        if i==0:
            input=check(code,guess)
            if input=="11111":
                print("word is guessed at try {}".format(i+1))
                exit(0)
        else:
            if guess in word_list:
                word_list.remove(guess)
            #populating contains and notcontains list
            checkInput(input,guess)
            #filtering the list.
            lis=filter(contains,notcontains,word_list)
            temp=[]
            word_list=lis
            for word in lis:
                for j in word:
                    if j not in contains and j not in temp :
                        temp.append(j)
            guess=""
            if len(temp)>=5:
                guess=temp[0]+temp[1]+temp[2]+temp[3]+temp[4]
            else:
                guess=random.choice(lis)

            print(temp)
            print(guess)
            print(lis)
            print(contains)

            input=check(code,guess)
            if input=="11111":
                print("word is guessed at try {}".format(i+1))
                exit(0)



code=input("enter the word")
guess=random.choice(['stone'])
word_list=language_dic()

tryguess(code,guess,word_list)

