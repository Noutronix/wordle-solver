import copy
import csv
import random as rd
import time


with open("wordle-answers-alphabetical.txt", "r") as f:
    words = list(csv.reader(f))


class wordle:
    def __init__(self): 
        self.words = [x[0] for x in words]
        self.yellows = {}
        self.greys = []
    
    def reduce(self, prev_input, results):
        #creates all of the new letters that were "yellow"
        for num, r in enumerate(results):
            if r == "1":
                item = self.yellows.get(prev_input[num])
                if item == None:
                    self.yellows[prev_input[num]] = [n for n in range(5) if n != num]
                else:
                    self.yellows[prev_input[num]] = [i for i in item if i != num]
        
        #reduces the number of places the yellow letters can go
        for num, r in enumerate(results):
            if r == "2":
                for k in copy.copy(list(self.yellows.keys())):
                    if prev_input[num] == k:
                        self.yellows.pop(k)

        for num, r in enumerate(results):   
            if r == "2":
                for k in self.yellows.keys():
                    self.yellows[k] = [x for x in self.yellows[k] if x != num]  
        #if there is only one place a yellow letter can go, it is marked as "green"
        for k in self.yellows.keys():
            if len(self.yellows[k]) == 1:
                for word in self.words.copy():
                    if k != word[self.yellows[k][0]]:
                        self.words.remove(word)

        
        
        #removes words depending on what letters they contain
        for word in copy.copy(self.words):
            if not referee(prev_input, word) == results:
                self.words.remove(word)



        return None


def referee(word1: str, word2: str):
    results = ["0" for x in range(5)]
    word1 = list(enumerate(word1)) #guess
    w2c = copy.copy(word2)

    for num, l in copy.copy(word1):
        if w2c[num] == l:
            results[num] = "2"
            word1 = word1[:word1.index((num, l))]+word1[word1.index((num, l))+1:]
            word2 = word2[:word2.index(l)]+word2[word2.index(l)+1:]
    for num, tp in enumerate(copy.copy(word1)):
        if tp[1] in word2:
            results[tp[0]] = "1"
            word1 = word1[:word1.index(tp)]+word1[word1.index(tp)+1:]
            word2 = word2[:word2.index(tp[1])]+word2[word2.index(tp[1])+1:]
    
    return "".join(results)

def choose_word(game):

    with open("wordle-possible-answers.txt", "r") as f:
        w = [y for x in csv.reader(f) for y in x]
        scores = {}
        for ans in w:
            results = {}
            for word in game.words:
                result = referee(ans, word)
                if result in results.keys():
                    results[result] += 1
                else:
                    results[result] = 1
            scores[ans] = sum([x**2 for x in results.values()])/len(results)
        return min(scores, key=lambda x:scores[x]-(1 if x in game.words else 0)) 




def solve():
    print("salet")
    game = wordle()
    results = input("results:") #format: xxxxx (0 for grey, 1 for yellow and 2 for green) ex: 02011
    game.reduce("salet", results)
    print(len(game.words))
    while True:
        word = choose_word(game)
        print(word)
        results = input("results:")
        game.reduce(word, results)
        print(len(game.words))
        if len(game.words) == 1:
            return game.words[0]


def benchmark():
    start = time.time()
    scores1 = []
    scores2 = []
    fails = 0
    for x in range(100):
        game = wordle()
        word_h = rd.choice(game.words)
        game.reduce("salet", referee("salet", word_h))
        for i in range(5):
            word = choose_word(game)
            game.reduce(word, referee(word, word_h))
            if len(game.words) == 1:
                if word == word_h:
                    scores1.append(i+2)
                    break
                if game.words[0] == word_h:
                    scores1.append(i+3)
                    break
                else:
                    raise ValueError

         
    average1 = sum(scores1)/len(scores1)
    print(time.time()-start)
    print("av1:", average1)
    

solve()

'''
g = wordle()
with open("bot-results.csv", "w") as results:
    for word in g.words:
        game = wordle()
        game.reduce("salet", referee("salet", word))
        results.write("salet")
        
        for i in range(5):
            ans = choose_word(game)
            if ans == word:
                results.write(","+word+"\n")
                break
            game.reduce(ans, referee(ans, word))
            results.write(","+ans)
'''


