print("------------------------")
print("PROGRAM HITUNG RATA-RATA")
print("------------------------")
angka = []
sum = 0
total = 0
while True: 
        data = str(input("Masukkan bilangan : "))
        
        angka.append(data)
       
        if data == "0":
            break
            
       
for datas in angka:
        sum = sum + int(datas)
        
hasil = sum / len(angka)
print("------------------------")
print("Total data  : " +str(len(angka)))
print("Data dalam list : " +str(angka))
print("Jumlah data : " +str(sum))
print("Nilai Rata-ratanya adalah : "+ str(hasil))
print("------------------------")

