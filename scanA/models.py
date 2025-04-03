from django.db import models

class Mahasiswa(models.Model):
    nama = models.CharField(max_length=100)
    nim = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)
    tanggal_lahir = models.DateField()

    def __str__(self):
        return self.nama

class Akun(models.Model):
    mahasiswa = models.OneToOneField(Mahasiswa, on_delete=models.CASCADE)  # Hubungkan ke Mahasiswa
    password = models.CharField(max_length=500)
    nama_pengguna = models.CharField(max_length=500, unique=True)  # Nama pengguna unik
    palm_kiri = models.CharField(max_length=500, blank=True, null=True)  # Bisa kosong jika belum ada
    palm_kanan = models.CharField(max_length=500, blank=True, null=True)
    wajah = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.nama_pengguna

class Kelas(models.Model):
    nama_kelas = models.CharField(max_length=100, unique=True)  # Nama kelas lebih singkat

    def __str__(self):
        return self.nama_kelas

class Admin(models.Model):
    nama = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=500)

    def __str__(self):
        return self.nama

class MataKuliah(models.Model):
    kode_mk = models.CharField(max_length=10, unique=True)
    nama_mk = models.CharField(max_length=200)
    jumlah_pertemuan = models.IntegerField(default=16)  # 16 per semester

    def __str__(self):
        return f"{self.kode_mk} - {self.nama_mk}"

class JadwalPresensi(models.Model):
    mata_kuliah = models.ForeignKey(MataKuliah, on_delete=models.CASCADE)
    kelas = models.ForeignKey(Kelas, on_delete=models.CASCADE)
    tanggal = models.DateField()

    def __str__(self):
        return f"{self.mata_kuliah.nama_mk} - {self.kelas.nama_kelas} - {self.tanggal}"

class Presensi(models.Model):
    mahasiswa = models.ForeignKey(Mahasiswa, on_delete=models.CASCADE)
    jadwal_presensi = models.ForeignKey(JadwalPresensi, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=10,
        choices=[('Hadir', 'Hadir'), ('Alpha', 'Alpha'), ('Izin', 'Izin'), ('Sakit', 'Sakit')],
        default='Alpha'
    )
    waktu_presensi = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.mahasiswa.nama} - {self.jadwal_absensi.tanggal} - {self.status}"
