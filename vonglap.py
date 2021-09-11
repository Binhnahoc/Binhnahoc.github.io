tiengui=int(input('nhập số tiền gửi vào ngân hàng: '))
tiennhan=int(input('nhập số tiền nhận ở ngân hàng: '))
tien=tiengui
sothang=0
while tien<tiennhan:
    tien=tien+0.0058*tiengui
    sothang=sothang+1
print('sau',sothang,'tháng,người đó sẽ nhận được',tiennhan)