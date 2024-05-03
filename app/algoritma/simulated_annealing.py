# simulated_annealing.py

import random
import copy
import time
from genetic_algorithm import *
from Classes import *
from data_initializer import *
from fitness_functions import *
from utils import *

def ssn(solution):
    rand_slot = random.choice(slots)
    rand_lt = random.choice(lts)
    a = random.randint(0, len(solution) - 1)
    new_solution = copy.deepcopy(solution)
    new_solution[a] = course_bits(solution[a]) + dosen_bits(solution[a]) +\
        kelas_bits(solution[a]) + rand_slot + lt_bits(solution[a])
    return [new_solution]


# It randomy selects two classes 
def swn(solution):
    a = random.randint(0, len(solution) - 1)
    b = random.randint(0, len(solution) - 1)
    new_solution = copy.deepcopy(solution)
    temp = slot_bits(solution[a])
    new_solution[a] = course_bits(solution[a]) + dosen_bits(solution[a]) +\
        kelas_bits(solution[a]) + slot_bits(solution[b]) + lt_bits(solution[a])

    new_solution[b] = course_bits(solution[b]) + dosen_bits(solution[b]) +\
        kelas_bits(solution[b]) + temp + lt_bits(solution[b])
    return [new_solution]

def acceptance_probability(old_cost, new_cost, temperature):
    if new_cost < old_cost:
        return 1.0
    else:
        return math.exp((old_cost - new_cost) / temperature)

def simulated_annealing():
    global population 
    alpha = 0.9
    T = 1.0
    T_min = 0.00001
    start_time = time.time()  
    
    convert_input_to_bin()
    population = init_population(1) # as simulated annealing is a single-state method
    old_cost = cost(population[0])
    simulated_annealing_scores = []  # List to store scores of each iteration
    # Simulated annealing iteration
    for __n in range(500):
        new_solution = swn(population[0])
        new_solution = ssn(population[0])
        new_cost = cost(new_solution[0])
        ap = acceptance_probability(old_cost, new_cost, T)
        if ap > random.random():
            population = new_solution
            old_cost = new_cost
        T = T * alpha
        # Calculate and store score of the current iteration
        simulated_annealing_scores.append(evaluate(population[0]))
    end_time = time.time()  
    print("\n----------------------- -----------------------\n")
    for lec in population[0]:
        print_chromosome(lec)
    print("Score: ", evaluate(population[0]))
    print("Time taken for Simulated Annealing: {:.4f} seconds".format(end_time - start_time))
    
population = [] 