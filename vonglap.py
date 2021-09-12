# Vẽ hình cây thông noel với số tầng bất kỳ
n = int(input('Nhập số nguyên bất kỳ: '))
for i in range(1,n+1):
    print(' '*(n-i),' 1'*i)