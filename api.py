import requests
import json


class KEYS:
	URL = 'https://worldtimeapi.org/api'
	TIMEZONE_KEY = 'timezone'
	IP_KEY = 'ip'


class MESSAGES:
	OPTION_GETTER = "Choose one of the above options: "
	AREA_GETTER = "Enter your area(Africa, America, Asia, Australia, Europe): "
	CITY_GETTER = "Enter the timezone city: "
	INVALID_OPTION = "ERROR: Please enter a valid option!"
	INVALID_TIMEZONE = "ERROR: Please enter a valid timezone!"


class OPTIONS:
	USR_LOCATION = "1) Your Location"
	OTHER_TZ = "2) Another Timezone"


def print_response(msg: dict):
	print("############################################################")
	for key, value in msg.items():
		print(": ".join([str(key), str(value)]))
	print("############################################################")

def main():

	while(True):
		print(OPTIONS.USR_LOCATION)
		print(OPTIONS.OTHER_TZ)
		option = int(input(MESSAGES.OPTION_GETTER))
		final_url = ''

		if option == 1:
			url_list = [KEYS.URL, KEYS.IP_KEY]
			final_url = '/'.join(url_list)

		elif option == 2:

			area = input(MESSAGES.AREA_GETTER)
			city = input(MESSAGES.CITY_GETTER)
			url_list = [KEYS.URL, KEYS.TIMEZONE_KEY, area, city]
			final_url = '/'.join(url_list)

		else:

			print("############################################################")
			print(MESSAGES.INVALID_OPTION)
			print("############################################################")
			continue
		
		res = requests.get(final_url)
		
		if res.status_code == 404:
			print("############################################################")
			print(MESSAGES.INVALID_TIMEZONE)
			print("############################################################")
			continue

		true_res = json.loads(res.text)
		# print(msg)
		print_response(true_res)


if __name__ == '__main__':
	main()
