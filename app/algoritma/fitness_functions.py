# fitness_functions.py

from Classes import *

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
