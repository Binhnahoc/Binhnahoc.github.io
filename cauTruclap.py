n=int(input('Nhap so nguyen duong thu nhat: '))
m=int(input('Nhap so nguyen duong thu hai: '))
s=0
for i in range(n,m):
    if i%3==0 or i%5==0:
        s=s+i
print('Tong cac so nguyen duong chia het cho 3 va 5 tu ', n, ' den ', m, 'la',s)
