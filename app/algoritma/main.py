# main.py
import random
from data_initializer import initialize_classes, initialize_dosen, initialize_course_classes, initialize_rooms, initialize_schedules
from genetic_algorithm import genetic_algorithm
from simulated_annealing import simulated_annealing

def main():
    random.seed()
    initialize_classes()
    initialize_dosen()
    initialize_course_classes()
    initialize_rooms()
    initialize_schedules()
    
    simulated_annealing()
    genetic_algorithm()

if __name__ == "__main__":
    main()
