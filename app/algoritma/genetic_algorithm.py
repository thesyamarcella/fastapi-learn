# genetic_algorithm.py

import random
import copy
from Classes import *
from data_initializer import *
from fitness_functions import *


def evaluate(chromosomes):
    global max_score
    score = 0
    score = score + use_spare_classroom(chromosomes)
    score = score + faculty_member_one_class(chromosomes)
    score = score + classroom_size(chromosomes)
    score = score + kelas_member_one_class(chromosomes)
    score = score + appropriate_room(chromosomes)
    score = score + appropriate_timeslot(chromosomes)
    score += dosen_preferred_time_slots(chromosomes)

    # Tambahkan evaluasi khusus untuk jadwal kelas malam
    for chromosome in chromosomes:
        class_index = int(kelas_bits(chromosome), 2)
        slot_index = int(slot_bits(chromosome), 2)
        if not is_evening_class(class_index, slot_index):
            score -= 1  # Penalti untuk jadwal kelas malam di bawah jam 18:00
    return score / max_score

def cost(solution):
    return 1 / float(evaluate(solution))

def init_population(n):
    global cpg, lts, slots
    chromosomes = []
    for _n in range(n):
        chromosome = []
        for _c in cpg:
            chromosome.append(_c + random.choice(slots) + random.choice(lts))
        chromosomes.append(chromosome)
    return chromosomes


# Modified Combination of Row_reselect, Column_reselect
def mutate(chromosome):
    rand_slot = random.choice(slots)
    rand_lt = random.choice(lts)
    a = random.randint(0, len(chromosome) - 1)
    chromosome[a] = course_bits(chromosome[a]) + dosen_bits(chromosome[a]) +\
        kelas_bits(chromosome[a]) + rand_slot + rand_lt

def crossover(population):
    a = random.randint(0, len(population) - 1)
    b = random.randint(0, len(population) - 1)
    cut = random.randint(0, len(population[0]))  # assume all chromosome are of same len
    population.append(population[a][:cut] + population[b][cut:])
    

def selection(population, n):
    population.sort(key=evaluate, reverse=True)
    while len(population) > n:
        population.pop()


def genetic_algorithm():
    start_time = time.time() 
    generation = 0
    convert_input_to_bin()
    population = init_population(3)
    best_solution = None

    print("\n---------------- Genetic Algorithm ------------------\n")
    while True:
        
        # if termination criteria are satisfied, stop.
        if evaluate(max(population, key=evaluate)) == 1 or generation == 500:
            end_time = time.time()  # End time for tracking execution time
            best_solution = max(population, key=evaluate)
            print("Generations:", generation)
            print("Best Chromosome fitness value", evaluate(best_solution))
            print("Best Chromosome: ", best_solution)
            for lec in best_solution:
                print_chromosome(lec)
            print_schedule_per_class(best_solution)
            print("Time taken for Genetic Algorithm: {:.4f} seconds".format(end_time - start_time))
            break
        
        # Otherwise continue
        else:
            for _c in range(len(population)):
                crossover(population)
                selection(population, 5)
                mutate(population[_c])
        generation = generation + 1
        
    # Convert the best solution to JSON
    if best_solution:
        json_data = chromosome_to_json(best_solution)
        # Save JSON data to file
        with open("schedule_data.json", "w") as json_file:
            json.dump(json_data, json_file, indent=4)

