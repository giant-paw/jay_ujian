def c_ke_f(dataC) :
    return (dataC * 9/5) + 32

def f_ke_c(dataF) :
    return (dataF -32) * 5/9

while True :
    print ("\n------------------------")
    print("\nMenu Konversi : ")
    print("1. Celcius ke Fahrenheit")
    print("2. Fahrenheit ke Celcius")
    pilihan = input("\nMasukkan pilihan (1 atau 2) : ")

    if pilihan == '1' :
        dataC = float(input("\nMasukkan suhu Celcius : "))   
        hasil_konv = c_ke_f(dataC) 
        print(f"{dataC} celcius sama dengan {hasil_konv} Fahrenheit")
        
    elif pilihan == '2' :
        dataF = float(input("Masukkan suhu Fahrenheit : "))
        hasil_konv = f_ke_c(dataF)
        print(f"{dataF} fahrenheit sama dengan {hasil_konv} Celcius")

    else :
        print("\nPilihan SALAH !!")       
        
    loop = input("\nApakah anda ingin mengulangi program lagi (y/n): ")
    if loop.lower() != 'y' :
        break