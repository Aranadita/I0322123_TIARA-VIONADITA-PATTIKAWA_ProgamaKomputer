print("==================================")
x = int(input("masukkan nilai variabel anda = "))
n = int(input("masukkan nilai pangkat       = "))

y=1
i=0
while n >= 1:
    y = y*x
    n = n-1
    i = i+1
    print ("nilai pangkat ke =", i , "adalah = ", y)
print("==================================")

print("==================================")
print("Bilangan ganjil <100 dengan konsep while")
while i <= 100:
    print (i)
    i = i+1
print("==================================")
x = int(input("masukkan nilai variabel anda = "))

#proses
y=1

while x != 1 :
    y = y * x
    x = x-1
print("Nilai faktorial anda =", y)