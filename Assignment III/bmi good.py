# Description of this Program
# Author : Theerachote Sittikorn
# Since : 2021-05-14
# Program Name :BMI Caculator
# Program Language : Python
# Program Purpose : Write a small program

height = float(input('กรุณาใส่ส่วนสูงของคุณ(เซนติเมตร): ')) #input your height for "height" to keep 
height = height/100  # Convert centimeters to meters
weight = int(input('กรุณาใส่ส่วนน้ำหนักของคุณ(กิโลกรัม): '))  # input your weight for "weight" to keep

bmi = weight/(height*height) #Caculate your BMI
 
 # comparison your BMI from standart
if bmi <= 18.5: 
    print('ค่าBMIของคุณคือ', bmi, 'หมายความว่าคุณน้ำหนักน้อยเกินไป') 

elif bmi > 18.5 and bmi < 25:
    print('ค่าBMIของคุณคือ', bmi, 'หมายความว่าคุณน้ำหนักอยู่ในเกณฑ์ปกติ')

elif bmi > 25 and bmi < 30:
    print('ค่าBMIของคุณคือ', bmi, 'หมายความว่าคุณน้ำหนักเกินเกณฑ์.')

elif bmi > 30:
    print('ค่าBMIของคุณคือ', bmi, 'หมายความว่าคุณอ้วน')

else: #if some thing bug
    print('ข้อมูลผิดพลาดกรุณาลองใหม่อีกครั้ง')

input('\n\nกด enter เพื่อออก.') #for exit program
