# data_initializer.py

import random
from Classes import *

def initialize_classes():
    Kelas.kelas = [Kelas("TI-20-PA", 20, shift="pagi"), Kelas("TI-21-PA", 20, shift="pagi"), Kelas("TI-22-PA", 20, shift="pagi"), 
               Kelas("TI-23-PA", 20, shift="pagi"), Kelas("TI-20-KA", 20, shift="malam"), Kelas('TI-24-PA', 20, shift="pagi"), Kelas('TI-21-KA', 25, shift="malam")]

def initialize_dosen():
    Dosen.dosen = [
        Dosen("Septian Cahyadi", preferred_time_slots=[Schedule("13:15", "15:00", "thu"), Schedule("20:15", "22:00", "wed")]), 
        Dosen("Edi Nurachmad", preferred_time_slots=[Schedule("13:15", "15:00", "Mon"), Schedule("15:15", "17:00", "Mon")]),  
        Dosen("Anton Sukamto", preferred_time_slots=[Schedule("20:15", "22:00", "Tue"), Schedule("15:15", "17:00", "Tue")]),
        Dosen("Febri Damatraseta", preferred_time_slots=[Schedule("13:15", "15:00", "Wed"), Schedule("15:15", "17:00", "Wed")]), 
        Dosen("Suci Sutjipto", preferred_time_slots=[Schedule("13:15", "15:00", "Fri"), Schedule("15:15", "17:00", "Fri")]), 
        Dosen("Isnan Mulia", preferred_time_slots=[Schedule("13:15", "15:00", "Mon"), Schedule("20:15", "22:00", "Mon")])
    ]

def initialize_course_classes():
    CourseClass.classes = [CourseClass("Basis Data"),CourseClass("Tata Kelola TI"),CourseClass("Pengantar Teknologi Informasi"),CourseClass("Matematika Diskrit"),
                   CourseClass("Lab Pemrograman Web", is_lab=True),CourseClass("Kecerdasan Buatan"),CourseClass("Manajemen Projek"),
                    CourseClass("Matematika Dasar")]

def initialize_rooms():
    Room.rooms = [Room("415", 40), Room("409", 40), Room("408", 40),
          Room("215", 20, is_lab=True),Room("210", 20, is_lab=True)]

def initialize_schedules():
    Schedule.schedules = [Schedule("08:15", "10:00", "Mon"), Schedule("10:15", "12:00", "Mon"),
                  Schedule("13:15", "15:00", "Mon"), Schedule("15:15", "17:00", "Mon"), 
                  Schedule("08:15", "10:00", "tue"), Schedule("10:15", "12:00", "tue"),
                  Schedule("13:15", "15:00", "tue"), Schedule("15:15", "17:00", "tue"),
                  Schedule("08:15", "10:00", "wed"), Schedule("10:15", "12:00", "wed"),
                  Schedule("13:15", "15:00", "wed"), Schedule("15:15", "17:00", "wed"),
                  Schedule("08:15", "10:00", "thu"), Schedule("10:15", "12:00", "thu"),
                  Schedule("13:15", "15:00", "thu"), Schedule("15:15", "17:00", "thu"),
                  Schedule("18:00", "20:00", "mon"), Schedule("20:15", "22:00", "mon"),
                  Schedule("18:00", "20:00", "tue"), Schedule("20:15", "22:00", "tue"),
                  Schedule("18:00", "20:00", "wed"), Schedule("20:15", "22:00", "wed"),
                  Schedule("18:00", "20:00", "thu"), Schedule("20:15", "22:00", "thu"),]
