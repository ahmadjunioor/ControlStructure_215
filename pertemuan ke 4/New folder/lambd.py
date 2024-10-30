import math
lingkaran_area = lambda r: 3.14 * r ** 2

radius = float(input("Masukkan jari-jari lingkaran: "))
area = lingkaran_area(radius)

# Tampilkan hasil
print(f"Luas lingkaran dengan jari-jari {radius} adalah {area}")