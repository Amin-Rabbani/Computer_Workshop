import requests
import json
import os
import msvcrt
import time


class USER:
	TIMEZONE = 'America/New_York'


class CONSTS:
	DELAY_TIME_FOR_EACH_REQUEST = 0.5
	BREAK_KEY_ASCII = 27
	PRINT_SEPARATOR = "###########################################################################"


class KEYS:
	URL = 'https://worldtimeapi.org/api'
	TIMEZONE = 'timezone'
	IP = 'ip'
	DATETIME = 'datetime'


class MESSAGES:
	OPTION_GETTER = "Choose one of the above options: "
	AREA_GETTER = "Enter your area(Africa, America, Asia, Australia, Europe, Pacific, Indian): "
	CITY_GETTER = "Enter the timezone city: "
	INVALID_OPTION = "ERROR: Please enter a valid option!"
	INVALID_REQUEST = "ERROR: Please enter a valid area or city!"
	BREAK_KEY_PRESS =  "Press <Esc> key to return to main menu"


class OPTIONS:
	LIST = [
		"1) Your Location Timezone",
		"2) Your Chosen Timezone",
		"3) All World Timezones List",
		"4) All Timezones List in an Area",
		"5) Exit",
	]


def clear_console():
	os.system('cls' if os.name == 'nt' else "printf '\033c'")


def print_time_response(url: str):
	while True:
		res = requests.get(url)
		dict_res = json.loads(res.text)
		clear_console()
		print(CONSTS.PRINT_SEPARATOR)
		print(dict_res[KEYS.TIMEZONE])
		print(dict_res[KEYS.DATETIME])
		print(MESSAGES.BREAK_KEY_PRESS)
		print(CONSTS.PRINT_SEPARATOR)
		time.sleep(CONSTS.DELAY_TIME_FOR_EACH_REQUEST)
		if msvcrt.kbhit():
			if ord(msvcrt.getch()) == CONSTS.BREAK_KEY_ASCII:
				break


def print_list_response(res: list):
	clear_console()
	print(CONSTS.PRINT_SEPARATOR)
	for tz in res:
		print(tz)
	print(CONSTS.PRINT_SEPARATOR)


def main():

	while True:
		for opt in OPTIONS.LIST:
			print(opt)

		option = int(input(MESSAGES.OPTION_GETTER))
		url_list = list()

		if option == 1:
			url_list = [KEYS.URL, KEYS.IP]

		elif option == 2:
			area = input(MESSAGES.AREA_GETTER)
			city = input(MESSAGES.CITY_GETTER)
			url_list = [KEYS.URL, KEYS.TIMEZONE, area, city]

		elif option == 3:
			url_list = [KEYS.URL, KEYS.TIMEZONE]
		
		elif option == 4:
			area = input(MESSAGES.AREA_GETTER)
			url_list = [KEYS.URL, KEYS.TIMEZONE, area]

		elif option == 5:
			exit(0)

		else:
			print(MESSAGES.INVALID_OPTION)
			continue
		
		final_url = '/'.join(url_list)
		res = requests.get(final_url)

		if res.status_code == 404:
			print(MESSAGES.INVALID_REQUEST)
			continue
		
		clear_console()
		json_res = json.loads(res.text)

		if option in [1, 2]:
			print_time_response(final_url)
		elif option in [3, 4]:
			print_list_response(json_res)


if __name__ == '__main__':
	main()
