import random
import sys

def display_banner():
	print("\n*********************************************")
	print("\tLET'S PLAY HAND CRICKET")
	print("START BATTING AND TASTE THE BOWLING OF COMPUTER")
	print("\n")

def number_gen():
	a = 1
	while True:
		yield a
		a = a+1 

def main_game():
	number_list = [0,1,2,3,4,5,6]
	total_score = 0
	total_balls = 0
	user_input = None
	free_hit = 0
	serial_number = number_gen()
	while True:
		print(str(next(serial_number))+".")
		total_balls = total_balls + 1
		try:
			user_input = input("Type a number in range [0,6]:\t")
			if user_input == "exit":
				break
			user_input = int(user_input)
		except:
			print("Choose number in range [0,6]")
			continue
		if user_input <= 6 and user_input >= 0 :# and user_input != 3 and\
			# user_input != 5:
			gen_num = random.choice(number_list)
			# gen_num = random.randint(0,6)
			print("computer generated :"+str(gen_num))
			print("\n")
			if free_hit == 0 :
				if user_input == gen_num :
					print("Empire says 'OUT' ")
					# total_balls = total_balls + 1
					# print("Your total score is :\t"+str(total_score))
					break
			else :
				if user_input == 6 or user_input == 4 :
					print("Empire says great work 'Its a "+str(user_input)+"\n")

			free_hit = 0

			if gen_num != 0 :
				total_score = total_score + user_input

			else :
				print("Oops No ball\n")
				total_balls = total_balls - 1
				free_hit = 1
				print("\n You got a free hit ;)")

		else:
			print("\nChoose number in range [0,6]\n")
			continue
	return total_balls,total_score

def display_score(total_balls,total_score,player_name):
	print("\n*********************************************")
	print("Well Played "+player_name+" , Here is your score")
	print("Your total score is :\t"+str(total_score))
	print("You Played "+ str(int(total_balls/6)) + " (Overs) and " \
		+ str(int(total_balls%6)) + " (Balls)")
	print("\n*********************************************")
	
if __name__ == '__main__':
	display_banner()
	total_balls,total_score = main_game()
	player_name = input("\nEnter you name :")
	display_score(total_balls,total_score,player_name)
	print("\n Keep playing  'Hand Cricket' the only fun game")
# print(user_input, gen_num)