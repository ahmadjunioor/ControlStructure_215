def ubah_temperature(nilai, unit):
    if unit == 'C':
        hasil = (nilai * 9/5) + 32
        print(f"{nilai}°C = {hasil}°F")
    elif unit == 'F':
        hasil = (nilai - 32) * 5/9
        print(f"{nilai}°F = {hasil}°C")
    else:
        print("suhunya tidak valid. Gunakan 'C' untuk Celsius atau 'F' untuk Fahrenheit.")

# Contoh penggunaan
nilai = float(input("Masukkan nilai suhu: "))  # Input nilai suhu
unit = input("Masukkan ssuhunya ('C' untuk Celsius, 'F' untuk Fahrenheit): ")  # Input suhu

# Panggil fungsi untuk mengonversi suhu
ubah_temperature(nilai, unit)