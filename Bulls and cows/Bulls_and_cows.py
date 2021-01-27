from collections import Counter
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        #Initializing bulls and cows with 0
        bulls=0
        cows=0
        #converting secret and guess strings to lists of characters as in Python strings are Immutable
        ls=list(secret)
        lg=list(guess)
        #looping through every index of ls and gs which are secret and guess respectively
        for i in range(len(secret)):
            if ls[i]==lg[i]:
                bulls+=1         #If both indices values are same then increasing bulls value by 1
                lg[i]='a'        #Replacing that index value with 'a' because we are marking it as bull in list secret
                ls[i]='b'        #Replacing that index value with 'b' because we are marking it as bull in list guess
        #Using Counter function to find out how many times each letter is repeating and creating a dictionary
        d2=Counter(lg)
        d1=Counter(ls)
        #looping through the keys in dictionary2(d2) to find out if this key is in d1 
        # Increase cows value with minimum value because it says how many ways we can arrange to change cows to bulls
        for key,value in d2.items():
            if key in d1:
                cows+=min(d1[key],value)  
        return str(bulls)+'A'+str(cows)+'B'