import random, copy
from Classes import *
from math import ceil, log2
import math
import matplotlib.pyplot as plt
import pandas as pd
import time
import json

Kelas.kelas = [Kelas("TI-20-PA", 40), Kelas("TI-20-PA1", 22), Kelas("TI-20-PA2", 20), 
               Kelas("TI-21-PA", 30), Kelas("TI-21-KA", 30), Kelas('TI-20-KA', 25)]

Dosen.dosen = [Dosen("Septian Cahyadi S.Kom., M.Kom."), Dosen("Damatraseta ST., M.Kom."), Dosen("Edi Nurachmad	S.Kom., M.Kom."),
                Dosen("Jemy	Arieswanto S.Kom., M.Kom."), Dosen("Isnan Mulia S.Komp., M.Kom."), Dosen("Anton	Sukamto	S.Kom., M.T.I.")]

MataKuliah.mata_kuliah = [MataKuliah("TIS10001"),MataKuliah("TIS10002"),MataKuliah("TIS10003"),MataKuliah("TIS10004"),
                       MataKuliah("TIS10005"),MataKuliah("TIS10006"),MataKuliah("TIS10086"),MataKuliah("TIS10084")]

Ruangan.ruangan = [
    Ruangan("B301", 25), Ruangan("B302", 25), Ruangan("B303", 25),
    Ruangan("B304", 25), Ruangan("B305", 25), Ruangan("B306", 25),
    Ruangan("B307", 25), Ruangan("B308", 25), Ruangan("B309", 25),
    Ruangan("B310", 25), Ruangan("B311", 25), Ruangan("B312", 25),
    Ruangan("B313", 25), Ruangan("B314", 25), Ruangan("B315", 25),
    Ruangan("B316", 25), Ruangan("B317", 25), Ruangan("B318", 25),
    Ruangan("B319", 25), Ruangan("B320", 25)
]

Jadwal.jadwal = [
    Jadwal("07:30", "09:15", "Mon"), Jadwal("09:30", "11:15", "Mon"),
    Jadwal("11:30", "13:15", "Mon"), Jadwal("13:30", "15:15", "Mon"),
    Jadwal("15:30", "17:15", "Mon"), Jadwal("17:30", "19:15", "Mon"),
    Jadwal("19:30", "21:00", "Mon"),
    
    Jadwal("07:30", "09:15", "Tue"), Jadwal("09:30", "11:15", "Tue"),
    Jadwal("11:30", "13:15", "Tue"), Jadwal("13:30", "15:15", "Tue"),
    Jadwal("15:30", "17:15", "Tue"), Jadwal("17:30", "19:15", "Tue"),
    Jadwal("19:30", "21:00", "Tue"),
    
    Jadwal("07:30", "09:15", "Wed"), Jadwal("09:30", "11:15", "Wed"),
    Jadwal("11:30", "13:15", "Wed"), Jadwal("13:30", "15:15", "Wed"),
    Jadwal("15:30", "17:15", "Wed"), Jadwal("17:30", "19:15", "Wed"),
    Jadwal("19:30", "21:00", "Wed"),
    
    Jadwal("07:30", "09:15", "Thu"), Jadwal("09:30", "11:15", "Thu"),
    Jadwal("11:30", "13:15", "Thu"), Jadwal("13:30", "15:15", "Thu"),
    Jadwal("15:30", "17:15", "Thu"), Jadwal("17:30", "19:15", "Thu"),
    Jadwal("19:30", "21:00", "Thu"),
    
    Jadwal("07:30", "09:15", "Fri"), Jadwal("09:30", "11:15", "Fri"),
    Jadwal("11:30", "13:15", "Fri"), Jadwal("13:30", "15:15", "Fri"),
    Jadwal("15:30", "17:15", "Fri"), Jadwal("17:30", "19:15", "Fri"),
    Jadwal("19:30", "21:00", "Fri")
]

ketersediaan_dosen = {
    "Septian Cahyadi S.Kom., M.Kom.": [("Mon", "07:30", "15:00")],
    "Damatraseta ST., M.Kom.": [("Fri", "10:00", "18:00")],
    "Edi Nurachmad S.Kom., M.Kom.": [("Tue", "07:30", "19:15")],
    "Jemy Arieswanto S.Kom., M.Kom.": [("Wed", "07:30", "19:15")]
}


max_score = None

penugasan_mengajar = []
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


def join_penugasan_mengajar_pair(_penugasan_mengajar):
    res = []
    for i in range(0, len(_penugasan_mengajar), 3):
        res.append(_penugasan_mengajar[i] + _penugasan_mengajar[i + 1] + _penugasan_mengajar[i + 2])
    return res

def find_kelas(nama_kelas):
    for i, kelas in enumerate(Kelas.kelas):
        if kelas.nama_kelas == nama_kelas:
            return i
    return -1
# Fungsi untuk mencari indeks dari kelas dengan nama yang diberikan dalam daftar kelas.

def find_dosen(inisial):
    for i, dosen in enumerate(Dosen.dosen):
        if dosen.inisial == inisial:
            return i
    return -1  # Return -1 jika dosen tidak ditemukan


def convert_input_to_bin():
    global penugasan_mengajar, lts, slots, max_score

    penugasan_mengajar = [
        MataKuliah.find("TIS10001"), Dosen.find("Septian Cahyadi S.Kom., M.Kom."), Kelas.find("TI-20-PA"),
        MataKuliah.find("TIS10006"), Dosen.find("Damatraseta ST., M.Kom."), Kelas.find("TI-20-PA1"),
        MataKuliah.find("TIS10003"), Dosen.find("Edi Nurachmad S.Kom., M.Kom."), Kelas.find("TI-20-PA2"),
        MataKuliah.find("TIS10004"), Dosen.find("Jemy Arieswanto S.Kom., M.Kom."), Kelas.find("TI-21-PA"),
        MataKuliah.find("TIS10005"), Dosen.find("Isnan Mulia S.Komp., M.Kom."), Kelas.find("TI-21-KA"),
        MataKuliah.find("TIS10002"), Dosen.find("Anton Sukamto S.Kom., M.T.I."), Kelas.find("TI-20-KA"),
        MataKuliah.find("TIS10084"), Dosen.find("Septian Cahyadi S.Kom., M.Kom."), Kelas.find("TI-20-PA"),
        MataKuliah.find("TIS10086"), Dosen.find("Jemy Arieswanto S.Kom., M.Kom."), Kelas.find("TI-20-PA"),
            ]

    for _c in range(len(penugasan_mengajar)):
        if _c % 3:  # MataKuliah
            penugasan_mengajar[_c] = (bin(penugasan_mengajar[_c])[2:]).rjust(bits_needed(MataKuliah.mata_kuliah), '0')
        elif _c % 3 == 1:  # Dosen
            penugasan_mengajar[_c] = (bin(penugasan_mengajar[_c])[2:]).rjust(bits_needed(Dosen.dosen), '0')
        else:  # Kelas
            penugasan_mengajar[_c] = (bin(penugasan_mengajar[_c])[2:]).rjust(bits_needed(Kelas.kelas), '0')

    penugasan_mengajar = join_penugasan_mengajar_pair(penugasan_mengajar)
    for r in range(len(Ruangan.ruangan)):
        lts.append((bin(r)[2:]).rjust(bits_needed(Ruangan.ruangan), '0'))

    for t in range(len(Jadwal.jadwal)):
        slots.append((bin(t)[2:]).rjust(bits_needed(Jadwal.jadwal), '0'))

    # print(penugasan_mengajar)
    max_score = (len(penugasan_mengajar) - 1) * 3 + len(penugasan_mengajar) * 3


def course_bits(chromosome):
    i = 0
    return chromosome[i:i + bits_needed(MataKuliah.mata_kuliah)]


def dosen_bits(chromosome):
    i = bits_needed(MataKuliah.mata_kuliah)

    return chromosome[i: i + bits_needed(Dosen.dosen)]


def kelas_bits(chromosome):
    i = bits_needed(MataKuliah.mata_kuliah) + bits_needed(Dosen.dosen)

    return chromosome[i:i + bits_needed(Kelas.kelas)]


def slot_bits(chromosome):
    i = bits_needed(MataKuliah.mata_kuliah) + bits_needed(Dosen.dosen) + \
        bits_needed(Kelas.kelas)

    return chromosome[i:i + bits_needed(Jadwal.jadwal)]


def lt_bits(chromosome):
    i = bits_needed(MataKuliah.mata_kuliah) + bits_needed(Dosen.dosen) + \
        bits_needed(Kelas.kelas) + bits_needed(Jadwal.jadwal)

    return chromosome[i: i + bits_needed(Ruangan.ruangan)]


def slot_clash(a, b):
    if slot_bits(a) == slot_bits(b):
        return 1
    return 0


 # Fungsi untuk memeriksa bahwa setiap dosen mengajar hanya satu kelas pada satu waktu.
def faculty_member_one_class(chromosome):
    scores = 0
    for i in range(len(chromosome) - 1): 
        clash = False
        for j in range(i + 1, len(chromosome)): 
            if slot_clash(chromosome[i], chromosome[j])\
                    and dosen_bits(chromosome[i]) == dosen_bits(chromosome[j]):
                clash = True
        if not clash:
            scores = scores + 1
    return scores

# Fungsi untuk memeriksa bahwa setiap kelas hanya memiliki satu kelas pada satu waktu.
def kelas_member_one_class(chromosomes):
    scores = 0

    for i in range(len(chromosomes) - 1):
        clash = False
        for j in range(i + 1, len(chromosomes)):
            if slot_clash(chromosomes[i], chromosomes[j]) and\
                    kelas_bits(chromosomes[i]) == kelas_bits(chromosomes[j]):
                clash = True
                break
        if not clash:
            scores = scores + 1
    return scores


 # Fungsi untuk memeriksa bahwa setiap mata kuliah dialokasikan ke ruangan yang tersedia. 
def use_spare_classroom(chromosome):
    scores = 0
    for i in range(len(chromosome) - 1):  # select one penugasan_mengajar pair
        clash = False
        for j in range(i + 1, len(chromosome)):  # check it with all other penugasan_mengajar pairs
            if slot_clash(chromosome[i], chromosome[j]) and lt_bits(chromosome[i]) == lt_bits(chromosome[j]):
                clash = True
        if not clash:
            scores = scores + 1
    return scores

  # Fungsi untuk memeriksa kapasitas kelas cukup untuk jumlah mahasiswa.
def classroom_size(chromosomes):
    scores = 0
    for _c in chromosomes:
        if Kelas.kelas[int(kelas_bits(_c), 2)].kuota <= Ruangan.ruangan[int(lt_bits(_c), 2)].kapasitas:
            scores = scores + 1
    return scores

 # Fungsi untuk memeriksa bahwa setiap mata kuliah ditempatkan di ruangan yang sesuai.
def appropriate_Ruangan(chromosomes):
    scores = 0
    for _c in chromosomes:
        if MataKuliah.mata_kuliah[int(course_bits(_c), 2)].is_lab == Ruangan.ruangan[int(lt_bits(_c), 2)].is_lab:
            scores = scores + 1
    return scores

# Fungsi untuk memeriksa bahwa waktu slot sesuai dengan jenis mata kuliah.
def appropriate_timeslot(chromosomes):
    scores = 0
    for _c in chromosomes:
        if MataKuliah.mata_kuliah[int(course_bits(_c), 2)].is_lab == Jadwal.jadwal[int(slot_bits(_c), 2)].is_lab_slot:
            scores = scores + 1
    return scores

# Fungsi untuk memeriksa apakah waktu mengajar dosen tersedia.
def validate_dosen_time(chromosome):
    score = 0
    dosen_bits_info = dosen_bits(chromosome)
    if dosen_bits_info:  
        dosen_index = int(dosen_bits_info, 2)
        dosen = Dosen.dosen[dosen_index]
        slot_index = int(slot_bits(chromosome), 2)
        time_slot = Jadwal.jadwal[slot_index].hari + "_" + Jadwal.jadwal[slot_index].jam_mulai
        
        # Memeriksa ketersediaan dosen
        for availability in ketersediaan_dosen.get(dosen.inisial, []):
            day, start_time, end_time = availability
            if time_slot.startswith(day) and start_time <= time_slot.split("_")[1] <= end_time:
                score += 1
                break  # Keluar dari loop setelah menemukan ketersediaan yang cocok
        else:
            score -= 1  # Penalti jika preferensi waktu tidak dipenuhi

    else:
        score -= 1  # Penalti jika tidak ada informasi dosen dalam kromosom
    return score


def evaluate(chromosomes):
    global max_score
    score = 0
    score = score + use_spare_classroom(chromosomes)
    score = score + faculty_member_one_class(chromosomes)
    score = score + classroom_size(chromosomes)
    score = score + kelas_member_one_class(chromosomes)
    score = score + appropriate_Ruangan(chromosomes)
    score = score + appropriate_timeslot(chromosomes)
    score += validate_dosen_time(chromosomes)  
    
    for chromosome in chromosomes:
        if validate_dosen_time(chromosome) < 0:
            score -= 1  # Penalti jika preferensi waktu tidak dipenuhi

    return score / max_score

def cost(solution):
    return 1 / float(evaluate(solution))

def init_population(n):
    global penugasan_mengajar, lts, slots
    chromosomes = []
    for _n in range(n):
        chromosome = []
        for _c in penugasan_mengajar:
            chromosome.append(_c + random.choice(slots) + random.choice(lts))
        chromosomes.append(chromosome)
    return chromosomes


# Modified Combination of Row_reselect, Column_reselect
def mutate(chromosome):
    # print("Before mutation: ", end="")
    # printChromosome(chromosome)

    rand_slot = random.choice(slots)
    rand_lt = random.choice(lts)

    a = random.randint(0, len(chromosome) - 1)
    
    chromosome[a] = course_bits(chromosome[a]) + dosen_bits(chromosome[a]) +\
        kelas_bits(chromosome[a]) + rand_slot + rand_lt

    # print("After mutation: ", end="")
    # printChromosome(chromosome)


def crossover(population):
    a = random.randint(0, len(population) - 1)
    b = random.randint(0, len(population) - 1)
    cut = random.randint(0, len(population[0]))  # assume all chromosome are of same len
    population.append(population[a][:cut] + population[b][cut:])
    

def selection(population, n):
    population.sort(key=evaluate, reverse=True)
    while len(population) > n:
        population.pop()


def print_chromosome(chromosome):
    print(
          Jadwal.jadwal[int(slot_bits(chromosome), 2)],"|",
          Ruangan.ruangan[int(lt_bits(chromosome), 2)],'|',
          Kelas.kelas[int(kelas_bits(chromosome), 2)], " | ",
          MataKuliah.mata_kuliah[int(course_bits(chromosome), 2)], " | ",
          Dosen.dosen[int(dosen_bits(chromosome), 2)]
          )

def chromosome_to_dict(chromosome):
    return {
        "timeslot": Jadwal.jadwal[int(slot_bits(chromosome), 2)].__dict__,
        "room": Ruangan.ruangan[int(lt_bits(chromosome), 2)].__dict__,
        "class": Kelas.kelas[int(kelas_bits(chromosome), 2)].__dict__,
        "course": MataKuliah.mata_kuliah[int(course_bits(chromosome), 2)].__dict__,
        "lecturer": Dosen.dosen[int(dosen_bits(chromosome), 2)].__dict__
    }
    
    if best_chromosome:
        best_chromosome_json = {
        "fitness_value": evaluate(best_solution),
        "chromosomes": [chromosome_to_dict(lec) for lec in best_solution]
    }
    with open("best_chromosome.json", "w") as f:
        json.dump(best_chromosome_json, f, indent=4)
    print("Best Chromosome saved to 'best_chromosome.json'")
    
# Simple Searching Neighborhood
# It randomly changes timeslot of a class/lab
def ssn(solution):
    rand_slot = random.choice(slots)
    rand_lt = random.choice(lts)
    
    a = random.randint(0, len(solution) - 1)
    
    new_solution = copy.deepcopy(solution)
    new_solution[a] = course_bits(solution[a]) + dosen_bits(solution[a]) +\
        kelas_bits(solution[a]) + rand_slot + lt_bits(solution[a])
    return [new_solution]


# It randomy selects two mata_kuliah 
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
    alpha = 0.9
    T = 1.0
    T_min = 0.00001
    
    convert_input_to_bin()
    population = init_population(1) # as simulated annealing is a single-state method
    old_cost = cost(population[0])
    # print("Cost of original random solution: ", old_cost)
    # print("Original population:")
    # print(population)

    for __n in range(500):
        new_solution = swn(population[0])
        new_solution = ssn(population[0])
        new_cost = cost(new_solution[0])
        ap = acceptance_probability(old_cost, new_cost, T)
        if ap > random.random():
            population = new_solution
            old_cost = new_cost
        T = T * alpha
    print("\n----------------------- Jadwal -----------------------\n")
    for lec in population[0]:
        print_chromosome(lec)
    print("Score: ", evaluate(population[0]))

def plot_fitness(generations, fitness_scores):
    plt.plot(generations, fitness_scores)
    plt.xlabel('Generation')
    plt.ylabel('Fitness Score')
    plt.title('Hybrid System')
    plt.show()

def plot_sa_fitness(iterations, fitness_scores):
    plt.plot(iterations, fitness_scores)
    plt.xlabel('Iteration')
    plt.ylabel('Fitness Score')
    plt.title('Simulated Annealing: Fitness Score vs Iteration')
    plt.show()

def genetic_algorithm():
    start_time = time.time()
    generations = []
    fitness_scores = []
    generation = 0
    
    convert_input_to_bin()
    population = init_population(3)

    print("\n------------- Hybrid Genetic Algorithm --------------\n")
    while True:
        max_fitness = max(evaluate(chromosome) for chromosome in population)
        best_chromosome = [chromosome for chromosome in population if evaluate(chromosome) == max_fitness][0]
        
        if max_fitness == 1 or generation == 500:
            print("Generations:", generation)
            print("Best Chromosome fitness value", max_fitness)
            print("Best Chromosome: ", best_chromosome)
            for lec in best_chromosome:
                print_chromosome(lec)
            break
        else:
            for _c in range(len(population)):
                crossover(population)
                selection(population, 5)
                mutate(population[_c])
            generations.append(generation)
            fitness_scores.append(max_fitness)
        generation += 1
    
    plot_fitness(generations, fitness_scores)
    end_time = time.time()
    execution_time = end_time - start_time
    print("Genetic Algorithm Execution Time:", execution_time, "seconds")


def simulated_annealing_algorithm():
    start_time = time.time()
    alpha = 0.9
    T = 1.0
    T_min = 0.00001
    iterations = []
    fitness_scores = []
    
    convert_input_to_bin()
    population = init_population(1)

    print("\n---------------- Genetic Algorithm ----------------\n")
    old_solution = population[0]
    old_score = evaluate(old_solution)
    print("\n initial Solution:")
    for lec in old_solution:
        print_chromosome(lec)
    print("initial Score:", old_score)

    for __n in range(500):
        new_solution = swn(old_solution)
        new_solution = ssn(old_solution)
        new_score = evaluate(new_solution[0])

        ap = acceptance_probability(old_score, new_score, T)
        if ap > random.random():
            old_solution = new_solution[0]
            old_score = new_score
        T = T * alpha
        iterations.append(__n)
        fitness_scores.append(old_score)

    print("\n----------------------- Simmulated Annealing -----------------------\n")
    for lec in old_solution:
        print_chromosome(lec)
    print("Simulated Annealing: ", old_score)

    plot_sa_fitness(iterations, fitness_scores)
    end_time = time.time()
    execution_time = end_time - start_time
    print("Simulated Annealing Execution Time:", execution_time, "seconds")
    

def main():
    start_time = time.time()
    random.seed()
    genetic_algorithm()
    simulated_annealing_algorithm()
    end_time = time.time()
    execution_time = end_time - start_time
    print("Hybrid System Execution Time:", execution_time, "seconds")
    
    

main()
