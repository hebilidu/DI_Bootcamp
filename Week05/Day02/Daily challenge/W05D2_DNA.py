# Week05 Day2 - OOP - Daily challenge - DNA
# Created on  : 210503 by : lidu
# Modified on : 210504 by : lidu

import random

class Gene(): # Not used in the program
    def __init__(self):
        self.bit = random.getrandbits(1) # generate a random gene

    def flip(self): # flip means move to 1, not the other way around
        bit = 1


class Chromosome():
    def __init__(self,ten_genes):
        self.ten_genes = ten_genes
        
    def __repr__(self):
        return str(self.ten_genes)

    def mutate(self):
        mutated = []
        for g in self.ten_genes:
            if g == 0:
                mutated.append(random.getrandbits(1)) # half of the time, stays at zero
            else:
                mutated.append(g) # keep 1's as is
        return mutated

    def is_all_1(self):
        for g in self.ten_genes:
            if g == 0:
                return False
        return True


class DNA():
    def __init__(self, ten_chrom):
        self.ten_chrom = ten_chrom

    def __repr__(self):
        out_str = ''
        for c in self.ten_chrom:
            out_str += c.__repr__() + '\n'
        return out_str

    def mutate(self):
        mutated_DNA = []
        for c in self.ten_chrom:
            new_chrom = c.mutate()
            mutated_DNA.append(Chromosome(new_chrom))
        return mutated_DNA

    def is_all_1(self):
        for c in self.ten_chrom:
            if c.is_all_1() == False:
                return False
        return True


class Organism():
    def __init__(self, dna, env): # env is a probability (between 0 and 100. E.g. 60% is 0.6)
        self.dna = dna
        self.env = env

    def evolve(self):
        if random.random() < self.env: # mutate if the random draw is inferior to env otherwise do not mutate
            self.dna = DNA(self.dna.mutate())

def generate_dna():
    # each chromosome is initialized with a group of ten random genes
    ten_chrom = []
    for c in range(10): # Ten chromosomes
        ten_genes = []
        for g in range(10): # Tem genes
            ten_genes.append(random.getrandbits(1))
        ten_chrom.append(Chromosome(ten_genes))
    return DNA(ten_chrom)

research_book = []
dna = generate_dna()
print("\ndna initial:\n============")
print(dna)
prob = [0.2, 0.4, 0.6]
for p in prob:
    for i in range(5): # 5 times with same DNA and probability 
        trial = Organism(dna, p) 
        count = 0 # count the number of loops to reach final state (all 1's)
        while True:
            count += 1
            trial.evolve()
            if trial.dna.is_all_1():
                break
        research_book.append({'Probability':p, 'Trial #':i, 'Number of generations': count})
print("Report:\n=======")
for line in research_book:
    print(line)
print("\nAnalysis:\n=========")
for p in prob:
    result = []
    for line in research_book:
        if line['Probability'] == p:
            result.append(line['Number of generations'])
    avg = round(sum(result) / len(result))
    print(f"For probability {p}, average number of generations is {avg}")
print('\n')
