import requests
while(True) :
	print("1) My Location ")
	print("2) Other")
	option = int(input("Chose one of the above options: "))
	if(option ==  1) :
		r = requests.get('http://worldtimeapi.org/api/ip')
		break;
	elif(option == 2) :
		area = input("Enter your area(Europe, Asia, America, Australia): ")
		city = input("Enter your city: ")
		r = requests.get('http://worldtimeapi.org/api/timezone/'+area+'/'+city)
		break;
	else :
		print("Please enter a valid option !")
print (r.text)

