import random

def main():
	number_list = [0,1,2,4,6]
	total_score = 0
	while True:
		user_input = int(input("Type a number b/w (0,1,2,4,6):\t"))
		if user_input <= 6 and user_input >= 0 and user_input != 3 and user_input != 5:
			gen_num = random.choice(number_list)
			# gen_num = random.randint(0,6)
			print("computer generated :"+str(gen_num))
			print("\n")
			if user_input == gen_num :
				print("Empire says 'OUT' ")
				print("Your total score is :\t"+str(total_score))
				break
			else :
				total_score = total_score + user_input

		else:
			print("Choose number in [0,1,2,4,6]")
			continue

if __name__ == '__main__':
	main()
	print("\n Thank you for playing  'Hand Cricket' ")
# print(user_input, gen_num)