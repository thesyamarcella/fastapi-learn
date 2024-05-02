class Kelas:
    kelas = None

    def __init__(self, nama_kelas, kuota):
        self.nama_kelas = nama_kelas
        self.kuota = kuota

    @staticmethod
    def find(nama_kelas):
        for i in range(len(Kelas.kelas)):
            if Kelas.kelas[i].nama_kelas == nama_kelas:
                return i
        return -1

    def __repr__(self):
        return "Kelas: " + self.nama_kelas


class Dosen:
    dosen = None

    def __init__(self, inisial):
        self.inisial = inisial

    @staticmethod
    def find(inisial):
        for i in range(len(Dosen.dosen)):
            if Dosen.dosen[i].inisial == inisial:
                return i
        return -1

    def __repr__(self):
        return "Dosen Pengampu: " + self.inisial


class MataKuliah:
    mata_kuliah = None

    def __init__(self, kd_mata_kuliah, is_lab=False):
        self.kd_mata_kuliah = kd_mata_kuliah
        self.is_lab = is_lab

    @staticmethod
    def find(kd_mata_kuliah):
        for i in range(len(MataKuliah.mata_kuliah)):
            if MataKuliah.mata_kuliah[i].kd_mata_kuliah == kd_mata_kuliah:
                return i
        return -1

    def __repr__(self):
        return "Mata Kuliah: " + self.kd_mata_kuliah 

class Ruangan:
    ruangan = None

    def __init__(self, nama_ruangan, kapasitas, is_lab=False):
        self.nama_ruangan = nama_ruangan
        self.kapasitas = kapasitas
        self.is_lab = is_lab

    @staticmethod
    def find(nama_ruangan):
        for i in range(len(Ruangan.ruangan)):
            if Ruangan.ruangan[i].nama_ruangan == nama_ruangan:
                return i
        return -1

    def __repr__(self):
        return "Ruangan: " + self.nama_ruangan


class Jadwal:
    jadwal = None

    def __init__(self, jam_mulai, jam_selesai, hari, is_lab_slot=False):
        self.jam_mulai = jam_mulai
        self.jam_selesai = jam_selesai
        self.hari = hari
        self.is_lab_slot = is_lab_slot

    def __repr__(self):
        return "Jadwal: " + self.jam_mulai + "-" + self.jam_selesai + " Hari: " + self.hari
