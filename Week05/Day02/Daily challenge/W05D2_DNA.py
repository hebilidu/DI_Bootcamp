# Week05 Day2 - OOP - Daily challenge - DNA
# Created on  : 210503 by : lidu
# Modified on : 210503 by : lidu
'''
This challenge is about Biology.

    Build a DNA object. DNA is composed of chromosomes which is itself composed of Genes.
        A Gene is a single value 0 or 1, it can mutate (flip).
        A Chromosome is a series of 10 Genes. It also can mutate, meaning a random number of genes can randomly flip (1/2 chance to flip).
        A DNA is a series of 10 chromosome, and it can also mutate the same way Chromosomes can mutate.

    Implement these classes as you see fit.
    Create a new class called Organism that accepts a DNA object and an environment parameter that sets the probability for its DNA to mutate.
    Instantiate a number of Organims and let them mutate until one gets to a DNA which is only made of 1s. Then stop and record the number of generations (iterations) it took.

Write your results in you personal biology research notebook and tell us your conclusion :).
'''