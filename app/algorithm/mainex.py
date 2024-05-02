import random
import copy
from Classes import *
from math import ceil, log2
import math
import pandas as pd
import time
import json
import matplotlib.pyplot as plt

# Inisialisasi data kelas, dosen, mata kuliah, ruangan, dan jadwal
Kelas.kelas = [Kelas("11SI1", 20), Kelas("11SI2", 22), Kelas("12SI1", 30), 
               Kelas("12SI2", 30), Kelas("13SI1", 28), Kelas('13I2', 25)]

Dosen.dosen = [
    Dosen("Mr. Mario Simaremare"), 
    Dosen("Mr. Tennov"),  
    Dosen("Mrs. Parmonangan"),
    Dosen("Mrs. Junita"), 
    Dosen("Mr. Samuel"), 
    Dosen("Mr. Humasak")
]

MataKuliah.mata_kuliah = [
    MataKuliah("KUS1002"), MataKuliah("MAS1101"), MataKuliah("KUS2002"), MataKuliah("TIS1101"),
    MataKuliah("KUS1001"), MataKuliah("FIS1103"), MataKuliah("12S1101"), MataKuliah("TIS3001")
]

Ruangan.ruangan = [
    Ruangan("GD512", 40), Ruangan("GD513", 40), Ruangan("GD514", 40),
    Ruangan("GD522", 40, is_lab=True), Ruangan("GD523", 40, is_lab=True)
]

Jadwal.jadwal = [
    Jadwal("08:15", "10:00", "Mon"), Jadwal("10:15", "12:00", "Mon"),
    Jadwal("13:15", "15:00", "Mon"), Jadwal("15:15", "17:00", "Mon"), 
    Jadwal("08:15", "10:00", "Tue"), Jadwal("10:15", "12:00", "Tue"),
    Jadwal("13:15", "15:00", "Tue"), Jadwal("15:15", "17:00", "Tue"),
    Jadwal("08:15", "10:00", "Wed"), Jadwal("10:15", "12:00", "Wed"),
    Jadwal("13:15", "15:00", "Wed"), Jadwal("15:15", "17:00", "Wed"),
    Jadwal("08:15", "10:00", "Thu"), Jadwal("10:15", "12:00", "Thu"),
    Jadwal("13:15", "15:00", "Thu"), Jadwal("15:15", "17:00", "Thu")
]

max_score = None
cpg = []
lts = []
slots = []
bits_needed_backup_store = {}  

def bits_needed(x):
    global bits_needed_backup_store
    r = bits_needed_backup_store.get(id(x))
    if r is None:
        r = int(ceil(log2(len(x))))
        bits_needed_backup_store[id(x)] = r
    return max(r, 1)

def join_cpg_pair(_cpg):
    res = []
    for i in range(0, len(_cpg), 3):
        res.append(_cpg[i] + _cpg[i + 1] + _cpg[i + 2])
    return res

def convert_input_to_bin():
    global cpg, lts, slots, max_score

    cpg = [MataKuliah.find("KUS1002"), Dosen.find("Mr. Mario Simaremare"), Kelas.find("13SI1"),
           MataKuliah.find("FIS1103"), Dosen.find("Mr. Mario Simaremare"), Kelas.find("13SI1"),
           MataKuliah.find("KUS1001"), Dosen.find("Mrs. Junita"), Kelas.find("11SI1"),
           MataKuliah.find("TIS1101"), Dosen.find("Mr. Humasak"), Kelas.find("13SI2"),
           MataKuliah.find("KUS2002"), Dosen.find("Mr. Samuel"), Kelas.find("13SI2"),
           MataKuliah.find("MAS1101"), Dosen.find("Mr. Tennov"), Kelas.find("11SI2"),
           MataKuliah.find("KUS1001"), Dosen.find("Mrs. Junita"), Kelas.find("12SI1"),
           MataKuliah.find("KUS2002"), Dosen.find("Mrs. Parmonangan"), Kelas.find("13SI2"),
           MataKuliah.find("KUS1002"), Dosen.find("Mr. Mario Simaremare"), Kelas.find("13SI2"),
           MataKuliah.find("FIS1103"), Dosen.find("Mr. Mario Simaremare"), Kelas.find("13SI2"),
           MataKuliah.find("KUS1001"), Dosen.find("Mrs. Junita"), Kelas.find("11SI2"),
           MataKuliah.find("TIS3001"), Dosen.find("Mr. Humasak"), Kelas.find("13SI1"),
           MataKuliah.find("KUS2002"), Dosen.find("Mr. Samuel"), Kelas.find("13SI1"),
           MataKuliah.find("MAS1101"), Dosen.find("Mr. Tennov"), Kelas.find("11SI1"),
           MataKuliah.find("KUS1001"), Dosen.find("Mrs. Junita"), Kelas.find("12SI2"),
           MataKuliah.find("KUS2001"), Dosen.find("Mrs. Parmonangan"), Kelas.find("13SI2")
           ]

    for _c in range(len(cpg)):
        if _c % 3:  # CourseClass
            cpg[_c] = (bin(cpg[_c])[2:]).rjust(bits_needed(MataKuliah.mata_kuliah), '0')
        elif _c % 3 == 1:  # Dosen
            cpg[_c] = (bin(cpg[_c])[2:]).rjust(bits_needed(Dosen.dosen), '0')
        else:  # Kelas
            cpg[_c] = (bin(cpg[_c])[2:]).rjust(bits_needed(Kelas.kelas), '0')

    cpg = join_cpg_pair(cpg)
    for r in range(len(Ruangan.ruangan)):
        lts.append((bin(r)[2:]).rjust(bits_needed(Ruangan.ruangan), '0'))

    for t in range(len(Jadwal.jadwal)):
        slots.append((bin(t)[2:]).rjust(bits_needed(Jadwal.jadwal), '0'))

    max_score = (len(cpg) + len(lts) + len(slots)) * 2

def generate_initial_population(size):
    population = []
    for i in range(size):
        chromosome = []
        chromosome.extend(random.sample(cpg, len(cpg)))
        chromosome.extend(random.sample(lts, len(lts)))
        chromosome.extend(random.sample(slots, len(slots)))
        population.append(chromosome)
    return population

def decode(chromosome):
    decoded = {}
    cc_size = len(cpg) // 3
    for i in range(cc_size):
        idx = i * 3
        decoded[i] = {
            "mata_kuliah": MataKuliah.mata_kuliah[int(chromosome[idx], 2)],
            "dosen": Dosen.dosen[int(chromosome[idx + 1], 2)],
            "kelas": Kelas.kelas[int(chromosome[idx + 2], 2)]
        }
    for i in range(len(Ruangan.ruangan)):
        decoded[i]["ruangan"] = Ruangan.ruangan[int(chromosome[cc_size + i], 2)]
    for i in range(len(Jadwal.jadwal)):
        decoded[i]["jadwal"] = Jadwal.jadwal[int(chromosome[cc_size + len(Ruangan.ruangan) + i], 2)]
    return decoded

def score(chromosome):
    score = max_score
    decoded = decode(chromosome)
    counter = {}
    for k, v in decoded.items():
        cc = v['kelas']
        if counter.get(cc) is None:
            counter[cc] = {}
        counter[cc][v['jadwal'].hari] = counter[cc].get(v['jadwal'].hari, 0) + 1
        if counter[cc][v['jadwal'].hari] > 3:
            score -= 10
        if v['mata_kuliah'].is_lab:
            if not v['ruangan'].is_lab:
                score -= 5
        else:
            if v['ruangan'].is_lab:
                score -= 5
        if v['ruangan'].kapasitas < v['kelas'].kuota:
            score -= 1
    return score

def crossover(population):
    new_population = []
    for _ in range(len(population) // 2):
        parent1 = random.choice(population)
        parent2 = random.choice(population)
        pivot = random.randint(1, len(parent1) - 1)
        child1 = parent1[:pivot] + parent2[pivot:]
        child2 = parent2[:pivot] + parent1[pivot:]
        new_population.append(child1)
        new_population.append(child2)
    return new_population

def mutate(population):
    for chromosome in population:
        if random.uniform(0, 1) < 0.2:
            idx = random.randint(0, len(chromosome) - 1)
            chromosome[idx] = '0' if chromosome[idx] == '1' else '1'
    return population

def genetic_algorithm(population_size, generations):
    population = generate_initial_population(population_size)
    best_score = float('-inf')
    best_chromosome = None
    scores = []
    for generation in range(generations):
        population = sorted(population, key=lambda x: score(x), reverse=True)
        if score(population[0]) > best_score:
            best_score = score(population[0])
            best_chromosome = population[0]
        new_population = crossover(population)
        population = mutate(new_population)
        scores.append(best_score)
        print(f"Generation {generation + 1}, Best Score: {best_score}")
    return best_chromosome, best_score, scores

def plot_scores(scores):
    plt.plot(range(len(scores)), scores)
    plt.xlabel('Generations')
    plt.ylabel('Best Score')
    plt.title('Genetic Algorithm Optimization')
    plt.show()

if __name__ == "__main__":
    convert_input_to_bin()
    start_time = time.time()
    best_chromosome, best_score, scores = genetic_algorithm(10, 50)
    end_time = time.time()
    print(f"Execution Time: {end_time - start_time} seconds")
    plot_scores(scores)
    print("Best Schedule:")
    decoded_schedule = decode(best_chromosome)
    for k, v in decoded_schedule.items():
        print(f"CourseClass {k + 1}: {v['mata_kuliah']} - {v['dosen']} - {v['kelas']} - {v['ruangan']} - {v['jadwal']}")
