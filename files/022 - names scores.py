#! Python3
#Using [names.txt](https://projecteuler.net/project/resources/p022_names.txt) (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.
#For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.
#What is the total of all the name scores in the file?
# https://projecteuler.net/problem=22

def readinfile(file_name):
    'returns sorted list of the names from the file'
    with open (file_name, "r") as f:
        for line in f:
            names = line.split(",")
            for i in range(len(names)):
                names[i] = names[i].replace('"', "")
            names = sorted(names)
    return names

def getnamescore(name):
    "returns single name's score as int"
    score = 0
    for letter in name:
        score += ord(letter)-64
    return score

if __name__ == "__main__":
    names = readinfile("p022_names.txt")
    total_score = 0
    for i in range(len(names)):
        total_score += getnamescore(names[i]) * (i+1)
    print(total_score)
