height = float(input('กรุณาใส่ส่วนสูงของคุณ(เซนติเมตร): '))
height = height/100
weight = int(input('กรุณาใส่ส่วนน้ำหนักของคุณ(กิโลกรัม): '))
bmi = weight/(height*height)

if bmi <= 18.5:
    print('ค่าBMIของคุณคือ', bmi, 'หมายความว่าคุณน้ำหนักน้อยเกินไป')

elif bmi > 18.5 and bmi < 25:
    print('ค่าBMIของคุณคือ', bmi, 'หมายความว่าคุณน้ำหนักอยู่ในเกณฑ์ปกติ')

elif bmi > 25 and bmi < 30:
    print('ค่าBMIของคุณคือ', bmi, 'หมายความว่าคุณน้ำหนักเกินเกณฑ์.')

elif bmi > 30:
    print('ค่าBMIของคุณคือ', bmi, 'หมายความว่าคุณอ้วน')

else:
    print('ข้อมูลผิดพลาดกรุณาลองใหม่อีกครั้ง')

input('\n\nกด enter เพื่อออก.')
