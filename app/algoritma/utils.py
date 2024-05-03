# utils.py
import random
from Classes import *
from math import ceil, log2

cpg = []
lts = []
slots = []
bits_needed_backup_store = {}  


def bits_needed(x):
    bits_needed_backup_store = {}
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

def is_evening_class(class_index, slot_index):
    class_shift = Kelas.kelas[class_index].shift
    schedule_day = Schedule.schedules[slot_index].day
    max_evening_schedule = MAX_EVENING_SCHEDULE.get(schedule_day)
    
    # Periksa apakah max_evening_schedule adalah None
    if max_evening_schedule is None:
        return False
    
    # Ambil waktu mulai dan waktu akhir dari jadwal kelas
    class_start_time = Schedule.schedules[slot_index].start
    class_end_time = Schedule.schedules[slot_index].end
    
    # Ambil waktu mulai dan waktu akhir dari batas waktu maksimum untuk kelas malam
    max_evening_start_time = max_evening_schedule.start
    max_evening_end_time = max_evening_schedule.end
    
    # Jika shift adalah malam dan waktu mulai kelas di bawah jam 18:00, maka kelas bukanlah kelas malam
    if class_shift == "malam" and class_start_time >= max_evening_start_time and class_end_time <= max_evening_end_time:
        return True
    
    # Jika shift adalah pagi dan waktu mulai kelas di atas jam 18:00, maka kelas bukanlah kelas malam
    if class_shift == "pagi" and class_start_time < max_evening_start_time:
        return True
    
    return False


