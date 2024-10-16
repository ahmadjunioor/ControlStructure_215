def evaluasi_performance(persentase):
    if persentase >= 90:
        return "Luar Biasa"
    elif persentase >= 80:
        return "Sangat Baik"
    elif persentase >= 70:
        return "Baik"
    elif persentase >= 60:
        return "Rata-rata"
    else:
        return "Perlu Ditingkatkan"

persentase = float(input("Masukkan persentase siswa: "))
print(evaluasi_performance(persentase))

def largest_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

a = float(input("Masukkan angka pertama: "))
b = float(input("Masukkan angka kedua: "))
c = float(input("Masukkan angka ketiga: "))
print(f"Angka terbesar adalah: {largest_of_three(a, b, c)}")

def fibonacci(n):
    fib_series = [0, 1]
    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series[:n]

n = int(input("Masukkan nilai n: untuk deret Fibonacci: "))
print(f"Deret Fibonacci hingga {n} adalah: {fibonacci(n)}")

def print_odd_numbers(n):
    odd_numbers = [i for i in range(1, n+1) if i % 2 != 0]
    return odd_numbers

n = int(input("Enter the value of n: "))
print(f"Odd numbers up to {n}: {print_odd_numbers(n)}")

def cetak_segitiga_siku(n):
    for i in range(1, n+1):
        print((str(i) + " ") * i)

n = int(input("Masukkan nilai n: "))
cetak_segitiga_siku(n)