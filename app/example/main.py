import random
import copy
from Classes import *
from math import ceil, log2
import math
import pandas as pd
import time
import json
from ics import Calendar, Event
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

Kelas.kelas = [Kelas("TI-20-PA", 20), Kelas("TI-21-PA", 20), Kelas("TI-22-PA", 20), 
               Kelas("TI-23-PA", 20), Kelas("TI-20-KA", 20), Kelas('TI-24-PA', 20), Kelas('TI-21-KA', 25)]

Dosen.dosen = [
    Dosen("Septian Cahyadi", preferred_time_slots=["08:15", "10:00", "13:15"]), 
    Dosen("Edi Nurachmad", preferred_time_slots=[Schedule("13:15", "15:00", "Mon"), Schedule("15:15", "17:00", "Mon")]),  
    Dosen("Anton Sukamto", preferred_time_slots=[Schedule("13:15", "15:00", "Tue"), Schedule("15:15", "17:00", "Tue")]),
    Dosen("Febri Damatraseta", preferred_time_slots=[Schedule("13:15", "15:00", "Wed"), Schedule("15:15", "17:00", "Wed")]), 
    Dosen("Suci Sutjipto", preferred_time_slots=[Schedule("13:15", "15:00", "Fri"), Schedule("15:15", "17:00", "Fri")]), 
    Dosen("Isnan Mulia", preferred_time_slots=[Schedule("13:15", "15:00", "Mon"), Schedule("15:15", "17:00", "Mon")])
]

CourseClass.classes = [CourseClass("Basis Data"),CourseClass("Tata Kelola TI"),CourseClass("Pengantar Teknologi Informasi"),CourseClass("Matematika Diskrit"),
                       CourseClass("Lab Pemrograman Web", is_lab=True),CourseClass("Kecerdasan Buatan"),CourseClass("Manajemen Projek"),
                        CourseClass("Matematika Dasar")]

Room.rooms = [Room("415", 40), Room("409", 40), Room("408", 40),
              Room("215", 20, is_lab=True),Room("210", 20, is_lab=True)]

Schedule.schedules = [Schedule("08:15", "10:00", "Mon"), Schedule("10:15", "12:00", "Mon"),
                      Schedule("13:15", "15:00", "Mon"), Schedule("15:15", "17:00", "Mon"), 
                      Schedule("08:15", "10:00", "tue"), Schedule("10:15", "12:00", "tue"),
                      Schedule("13:15", "15:00", "tue"), Schedule("15:15", "17:00", "tue"),
                      Schedule("08:15", "10:00", "wed"), Schedule("10:15", "12:00", "wed"),
                      Schedule("13:15", "15:00", "wed"), Schedule("15:15", "17:00", "wed"),
                      Schedule("08:15", "10:00", "thu"), Schedule("10:15", "12:00", "thu"),
                      Schedule("13:15", "15:00", "thu"), Schedule("15:15", "17:00", "thu"),]


max_score = None

cpg = []
lts = []
slots = []
bits_needed_backup_store = {}  # to improve performance


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

    cpg = [CourseClass.find("Basis Data"), Dosen.find("Septian Cahyadi"), Kelas.find("TI-20-KA"),
           CourseClass.find("Kecerdasan Buatan"), Dosen.find("Septian Cahyadi"), Kelas.find("TI-20-KA"),
           CourseClass.find("Lab Pemrograman Web"), Dosen.find("Febri Damatraseta"), Kelas.find("TI-20-PA"),
           CourseClass.find("Matematika Diskrit"), Dosen.find("Isnan Mulia"), Kelas.find("TI-21-KA"),
           CourseClass.find("Pengantar Teknologi Informasi"), Dosen.find("Suci Sutjipto"), Kelas.find("TI-21-KA"),
           CourseClass.find("Tata Kelola TI"), Dosen.find("Edi Nurachmad"), Kelas.find("TI-21-PA"),
           CourseClass.find("Lab Pemrograman Web"), Dosen.find("Febri Damatraseta"), Kelas.find("TI-22-PA"),
           CourseClass.find("Pengantar Teknologi Informasi"), Dosen.find("Anton Sukamto"), Kelas.find("TI-21-KA"),
           CourseClass.find("Basis Data"), Dosen.find("Septian Cahyadi"), Kelas.find("TI-21-KA"),
           CourseClass.find("Kecerdasan Buatan"), Dosen.find("Septian Cahyadi"), Kelas.find("TI-21-KA"),
           CourseClass.find("Lab Pemrograman Web"), Dosen.find("Febri Damatraseta"), Kelas.find("TI-21-PA"),
           CourseClass.find("Matematika Dasar"), Dosen.find("Isnan Mulia"), Kelas.find("TI-20-KA"),
           CourseClass.find("Pengantar Teknologi Informasi"), Dosen.find("Suci Sutjipto"), Kelas.find("TI-20-KA"),
           CourseClass.find("Tata Kelola TI"), Dosen.find("Edi Nurachmad"), Kelas.find("TI-20-PA"),
           CourseClass.find("Lab Pemrograman Web"), Dosen.find("Febri Damatraseta"), Kelas.find("TI-23-PA"),
           CourseClass.find("Manajemen Projek"), Dosen.find("Anton Sukamto"), Kelas.find("TI-21-KA")
           ]

    for _c in range(len(cpg)):
        if _c % 3:  # CourseClass
            cpg[_c] = (bin(cpg[_c])[2:]).rjust(bits_needed(CourseClass.classes), '0')
        elif _c % 3 == 1:  # Dosen
            cpg[_c] = (bin(cpg[_c])[2:]).rjust(bits_needed(Dosen.dosen), '0')
        else:  # Kelas
            cpg[_c] = (bin(cpg[_c])[2:]).rjust(bits_needed(Kelas.kelas), '0')

    cpg = join_cpg_pair(cpg)
    for r in range(len(Room.rooms)):
        lts.append((bin(r)[2:]).rjust(bits_needed(Room.rooms), '0'))

    for t in range(len(Schedule.schedules)):
        slots.append((bin(t)[2:]).rjust(bits_needed(Schedule.schedules), '0'))

    max_score = (len(cpg) - 1) * 3 + len(cpg) * 3


def course_bits(chromosome):
    i = 0

    return chromosome[i:i + bits_needed(CourseClass.classes)]


def dosen_bits(chromosome):
    i = bits_needed(CourseClass.classes)

    return chromosome[i: i + bits_needed(Dosen.dosen)]


def kelas_bits(chromosome):
    i = bits_needed(CourseClass.classes) + bits_needed(Dosen.dosen)

    return chromosome[i:i + bits_needed(Kelas.kelas)]


def slot_bits(chromosome):
    i = bits_needed(CourseClass.classes) + bits_needed(Dosen.dosen) + \
        bits_needed(Kelas.kelas)

    return chromosome[i:i + bits_needed(Schedule.schedules)]


def lt_bits(chromosome):
    i = bits_needed(CourseClass.classes) + bits_needed(Dosen.dosen) + \
        bits_needed(Kelas.kelas) + bits_needed(Schedule.schedules)

    return chromosome[i: i + bits_needed(Room.rooms)]


def slot_clash(a, b):
    if slot_bits(a) == slot_bits(b):
        return 1
    return 0

def dosen_preferred_time_slots(chromosomes):
    scores = 0
    for _c in chromosomes:
        dosen_index = int(dosen_bits(_c), 2)
        dosen = Dosen.dosen[dosen_index]
        slot_index = int(slot_bits(_c), 2)
        preferred_slots = dosen.preferred_time_slots
        if Schedule.schedules[slot_index] in preferred_slots:
            scores += 1
    return scores


# checks that a faculty member teaches only one course at a time.
def faculty_member_one_class(chromosome):
    scores = 0
    for i in range(len(chromosome) - 1):  # select one cpg pair
        clash = False
        for j in range(i + 1, len(chromosome)):  # check it with all other cpg pairs
            if slot_clash(chromosome[i], chromosome[j])\
                    and dosen_bits(chromosome[i]) == dosen_bits(chromosome[j]):
                clash = True
        if not clash:
            scores = scores + 1
    return scores


# check that a kelas member takes only one class at a time.
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


# checks that a course is assigned to an available classroom. 
def use_spare_classroom(chromosome):
    scores = 0
    for i in range(len(chromosome) - 1):  # select one cpg pair
        clash = False
        for j in range(i + 1, len(chromosome)):  # check it with all other cpg pairs
            if slot_clash(chromosome[i], chromosome[j]) and lt_bits(chromosome[i]) == lt_bits(chromosome[j]):
                clash = True
        if not clash:
            scores = scores + 1
    return scores


# checks that the classroom capacity is large enough for the classes that
def classroom_size(chromosomes):
    scores = 0
    for _c in chromosomes:
        if Kelas.kelas[int(kelas_bits(_c), 2)].size <= Room.rooms[int(lt_bits(_c), 2)].size:
            scores = scores + 1
    return scores

# check that room is appropriate for particular class/lab
def appropriate_room(chromosomes):
    scores = 0
    for _c in chromosomes:
        room_index = int(lt_bits(_c), 2)
        room = Room.rooms[room_index]
        class_index = int(course_bits(_c), 2)
        course_class = CourseClass.classes[class_index]
        if room.is_lab == course_class.is_lab:
            scores += 1
    return scores


# check that lab is allocated appropriate time slot
def appropriate_timeslot(chromosomes):
    scores = 0
    for _c in chromosomes:
        class_index = int(course_bits(_c), 2)
        course_class = CourseClass.classes[class_index]
        slot_index = int(slot_bits(_c), 2)
        if course_class.is_lab == Schedule.schedules[slot_index].is_lab_slot:
            scores += 1
    return scores

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


def print_chromosome(chromosome):
    print(
          Schedule.schedules[int(slot_bits(chromosome), 2)],"|",
          Room.rooms[int(lt_bits(chromosome), 2)],'|',
          Kelas.kelas[int(kelas_bits(chromosome), 2)], " | ",
          CourseClass.classes[int(course_bits(chromosome), 2)], " | ",
          Dosen.dosen[int(dosen_bits(chromosome), 2)]
          )

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
    
    # Plot the scores of each iteration
    plt.plot(range(len(simulated_annealing_scores)), simulated_annealing_scores)
    plt.title('Simulated Annealing: Fitness Score over Iterations')
    plt.xlabel('Iteration')
    plt.ylabel('Fitness Score')
    plt.show()

population = [] 

def genetic_algorithm():
    start_time = time.time() 
    generation = 0
    convert_input_to_bin()
    population = init_population(3)

    print("\n---------------- Genetic Algorithm ------------------\n")
    while True:
        
        # if termination criteria are satisfied, stop.
        if evaluate(max(population, key=evaluate)) == 1 or generation == 500:
            end_time = time.time()  # End time for tracking execution time
            print("Generations:", generation)
            print("Best Chromosome fitness value", evaluate(max(population, key=evaluate)))
            print("Best Chromosome: ", max(population, key=evaluate))
            for lec in max(population, key=evaluate):
                print_chromosome(lec)
            print("Time taken for Genetic Algorithm: {:.4f} seconds".format(end_time - start_time))
            break
        
        # Otherwise continue
        else:
            for _c in range(len(population)):
                crossover(population)
                selection(population, 5)
                mutate(population[_c])
        generation = generation + 1

def print_schedule_by_class(schedule, class_name):
    print("Schedule for Class", class_name)
    print("-----------------------------------------------------")
    for lec in schedule:
        if Kelas.kelas[int(kelas_bits(lec), 2)].name == class_name:
            print_chromosome(lec)
    print("-----------------------------------------------------")

def convert_schedule_to_json(schedule):
    schedule_json = []
    for chromosome in schedule:
        schedule_json.append({
            "course": CourseClass.classes[int(course_bits(chromosome), 2)].code,
            "lecturer": Dosen.dosen[int(dosen_bits(chromosome), 2)].name,
            "class": Kelas.kelas[int(kelas_bits(chromosome), 2)].name,
            "room": Room.rooms[int(lt_bits(chromosome), 2)].name,
            "schedule": {
                "start": Schedule.schedules[int(slot_bits(chromosome), 2)].start,
                "end": Schedule.schedules[int(slot_bits(chromosome), 2)].end,
                "day": Schedule.schedules[int(slot_bits(chromosome), 2)].day,
                "is_lab_slot": Schedule.schedules[int(slot_bits(chromosome), 2)].is_lab_slot
            }
        })
    return schedule_json

def convert_schedule_to_google_calendar_json(schedule):
    google_calendar_json = []
    for chromosome in schedule:
        course_class = CourseClass.classes[int(course_bits(chromosome), 2)]
        dosen = Dosen.dosen[int(dosen_bits(chromosome), 2)]
        kelas = Kelas.kelas[int(kelas_bits(chromosome), 2)]
        room = Room.rooms[int(lt_bits(chromosome), 2)]
        schedule_time = Schedule.schedules[int(slot_bits(chromosome), 2)]
        
        # Membuat nama acara dengan format "Kode_Matakuliah - Kelas"
        event_name = f"{course_class.code} - {kelas.name}"
        
        # Menyiapkan struktur JSON untuk jadwal
        schedule_json = {
            "summary": event_name,
            "location": room.name,
            "start": {
                "dateTime": schedule_time.start,
            },
            "end": {
                "dateTime": schedule_time.end,
            },
            "description": f"Dosen: {dosen.name}, Kelas: {kelas.name}",
            "recurrence": [
                f"RRULE:FREQ=WEEKLY;BYDAY={schedule_time.day[:2].upper()}"  # Menggunakan dua karakter pertama dari day
            ],
            "attendees": [
                {"email": f"{dosen.name.replace(' ', '')}@ibik.ac.id"}  # Email dosen
            ]
        }
        google_calendar_json.append(schedule_json)
    return google_calendar_json

# def convert_schedule_to_ics(schedule):
#     cal = Calendar()
#     for chromosome in schedule:
#         course_class = CourseClass.classes[int(course_bits(chromosome), 2)]
#         dosen = Dosen.dosen[int(dosen_bits(chromosome), 2)]
#         kelas = Kelas.kelas[int(kelas_bits(chromosome), 2)]
#         room = Room.rooms[int(lt_bits(chromosome), 2)]
#         schedule_time = Schedule.schedules[int(slot_bits(chromosome), 2)]
        
#         event = Event()
#         event.name = f"{course_class.code} - {kelas.name}"
#         event.location = room.name
#         event.description = f"Dosen: {dosen.name}, Kelas: {kelas.name}"
        
#         # Parse start and end times
#         start_time = datetime.strptime(schedule_time.start, "%H:%M")
#         end_time = datetime.strptime(schedule_time.end, "%H:%M")
        
#         # Calculate start and end dates (assuming Monday as the start of the week)
#         day_mapping = {"MON": 0, "TUE": 1, "WED": 2, "THU": 3, "FRI": 4, "SAT": 5, "SUN": 6}  # Ensure all days are in uppercase
#         current_day = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
#         target_day = day_mapping[schedule_time.day.upper()]  # Convert day abbreviation to uppercase
#         while current_day.weekday() != target_day:
#             current_day += timedelta(days=1)
        
#         start_date = current_day + timedelta(hours=start_time.hour, minutes=start_time.minute)
#         end_date = current_day + timedelta(hours=end_time.hour, minutes=end_time.minute)
        
#         event.begin = start_date
#         event.end = end_date
        
#         # Recur weekly
#         event.extra.append("RRULE:FREQ=WEEKLY")
        
#         cal.events.add(event)
    
#     return cal

def main():
    random.seed()
    genetic_algorithm()
    simulated_annealing()
    
    all_schedules = []

    # Convert schedule to Google Calendar JSON
    schedule = max(population, key=evaluate)
    google_calendar_json = convert_schedule_to_google_calendar_json(schedule)
    ics_schedule = convert_schedule_to_ics(schedule)

    # Save Google Calendar JSON to file
    with open("schedule_google_calendar.json", "w") as json_file:
        json.dump(google_calendar_json, json_file)

    # Print schedules for each class and save them to JSON files
    for class_obj in Kelas.kelas:
        schedule = max(population, key=evaluate)
        print_schedule_by_class(schedule, class_obj.name)

        # Convert schedule to JSON
        schedule_json = convert_schedule_to_json(schedule)
        all_schedules.extend(schedule_json)

    # Save all schedules to a single JSON file
    with open("all_schedules.json", "w") as json_file:
        json.dump(all_schedules, json_file)
        
    # Save the entire schedule to a single ICS file
    # with open("schedule.ics", "w") as ics_file:
    #     ics_file.write(ics_schedule.serialize())  

main()
