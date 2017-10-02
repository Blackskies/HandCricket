import random

def main():
	number_list = [0,1,2,4,6]
	total_score = 0
	total_balls = 0
	user_input = None
	while True:
		try:
			user_input = int(input("Type a number b/w (0,1,2,4,6):\t"))
		except:
			print("Choose number in [0,1,2,4,6]")
			continue
		if user_input <= 6 and user_input >= 0 and user_input != 3 and\
			 user_input != 5:
			gen_num = random.choice(number_list)
			# gen_num = random.randint(0,6)
			print("computer generated :"+str(gen_num))
			print("\n")
			if user_input == gen_num :
				print("Empire says 'OUT' ")
				# print("Your total score is :\t"+str(total_score))
				break
			else :
				if user_input == 6 or user_input == 4 :
					print("Empire says great work 'Its a "+str(user_input))
				total_score = total_score + user_input
			total_balls = total_balls + 1

		else:
			print("Choose number in [0,1,2,4,6]")
			continue
	return total_balls,total_score

def display_score(total_balls,total_score):
	print("\n*********************************************")
	print("Your total score is :\t"+str(total_score))
	print("You Played "+ str(int(total_balls/6)) + " (Overs) and " \
		+ str(int(total_balls%6)) + " (Balls)")
	print("\n*********************************************")
	
if __name__ == '__main__':
	total_balls,total_score = main()
	display_score(total_balls,total_score)
	print("\n Thank you for playing  'Hand Cricket' ")
# print(user_input, gen_num)