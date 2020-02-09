global too, p1c, p2c, p1, p2
global w
w=0
too = ["O", "X"]
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    TGREEN =  '\033[32m'
    TWHITE = '\033[37m'
def play():
	p1 = input("Player 1 please enter your name:")
	p2 = input("Player 2 please enter your name:")
	print("Get ready for playing the"+bcolors.BOLD+" legendrious",bcolors.ENDC+"game"+'\033[1;92m',"TicTacToe"+bcolors.ENDC)
	a = ["", "", ""]
	b = ["", "", ""]
	c = ["", "", ""]
	f = (a, b, c)
	w=0
	ind = 1
	while(True):
		print(p1,"please select",bcolors.BOLD+"O"+bcolors.ENDC,"or"+bcolors.BOLD,"X"+bcolors.ENDC)
		p1c = input()
		if(p1c in too):
			i = too.index(p1c)
			if(i == 0):
				p2c = too[1]
			else:
				p2c = too[0]
			break
		else:
			print("Please enter the above given symbols only:")
	while(ind <= 9):
		if(ind >= 9):
			print("No one won the game....")
			break
		while(True):
			print(p1,"enter your loction to place your",bcolors.BOLD,p1c,bcolors.ENDC,)
			t = int(input())
			if(t == 1 or t==2 or t==3):
				if(a[t-1]==""):
					a[t-1] = p1c
					ind = ind+1
					break
				else:
					print(p1,"the location is already taken")
					continue
			if(t == 4 or t==5 or t==6):
				if(b[t-4]==""):
					b[t-4] = p1c
					ind = ind+1
					break
				else:
					print(p1,"the location is already taken")
					continue
			if(t == 7 or t==8 or t==9):
				if(c[t-7]==""):
					c[t-7] = p1c
					ind = ind+1
					break
				else:
					print(p1,"the location is already taken")
					continue
		print(a[0],"|",a[1],"|",a[2])
		print("__ __ __")
		print(b[0],"|",b[1],"|",b[2])
		print("__ __ __")
		print(c[0],"|",c[1],"|",c[2])
		try:
			#if(((a[0] == b[0]== c[0]) and a[0] == pc1) or ((a[0] == b[1]== c[2]) and a[0] == pc1) or ((a[0] == b[0]== c[0]) and a[0] == pc1)):
				#print()
#Checking diagonals
			#print("Entered into try....")
			for i in range(0,1):
				#print("Entered into first diagonal")
				print(a[i] == b[i+1] == c[i+2])
				if((a[i] == b[i+1] == c[i+2]) and a[i] == p1c):
					print(p1,"you won the game")
					w = 1
				if((a[i] == b[i+1] == c[i+2]) and a[i] == p2c):
					print(p2,"you won the game")
					w = 1
			if(w == 1):
				#print("In diagonal w")
				break
			for i in range(-1,-2,-1):
				#print("Entered into 2nd diagonal")
				if((a[i] == b[i-1] == c[i-2]) and a[i] == p1c):
					print(p1,"you won the game")
					w = 1
				if((a[i] == b[i-1] == c[i-2]) and a[i] == p2c):
					print(p2,"you won the game")
					w = 1
			if(w == 1):
				break
#Checking columns
			for i in range(0,3):
				#print("Entered into columns")
				if((a[i] == b[i]== c[i]) and a[i] == p1c):
					print(p1,"You won the game")
					w=1
					break
				if((a[i] == b[i]== c[i]) and a[i] == p2c):
					print(p2,"You won the game")
					w=1
					break
			if(w == 1):
				break
#Checking Rows
			for i in range(0,1):
				#print("Entered into rows")
				print(a[i] == b[0] == c[0])
				if((a[i] == a[i+1]== a[i+2]) and a[i] == p1c):
					print(p1,"You won the game")
					w = 1
					break
				if((a[i] == a[i+1]== a[i+2]) and a[i] == p2c):
					w=1
					print(p2,"You won the game")
					break
				if((b[i] == b[i+1]== b[i+2]) and b[i] == p1c):
					print(p1,"You won the game")
					w = 1
					break
				if((b[i] == b[i+1]== b[i+2]) and b[i] == p2c):
					w=1
					print(p2,"You won the game")
					break
				if((c[i] == c[i+1]== c[i+2]) and c[i] == p1c):
					print(p1,"You won the game")
					w = 1
					break
				if((c[i] == c[i+1]== c[i+2]) and c[i] == p2c):
					w=1
					print(p2,"You won the game")
					break
			if(w==1):
				break
		except:
			#print("In catch 1")
			pass
		while(True):
			print(p2,"enter your loction to place your",bcolors.BOLD,p2c,bcolors.ENDC,)
			t = int(input())
			if(t == 1 or t==2 or t==3):
				if(a[t-1]==""):
					a[t-1] = p2c
					ind = ind+1
					break
				else:
					print(p1,"the location is already taken")
					continue
			if(t == 4 or t==5 or t==6):
				if(b[t-4]==""):
					b[t-4] = p2c
					ind = ind+1
					break
				else:
					print(p1,"the location is already taken")
					continue
			if(t == 7 or t==8 or t==9):
				if(c[t-7]==""):
					c[t-7] = p2c
					ind = ind+1
					break
				else:
					print(p1,"the location is already taken")
					continue
		print(a[0],"|",a[1],"|",a[2])
		print("__ __ __")
		print(b[0],"|",b[1],"|",b[2])
		print("__ __ __")
		print(c[0],"|",c[1],"|",c[2])
		try:
			#if(((a[0] == b[0]== c[0]) and a[0] == pc1) or ((a[0] == b[1]== c[2]) and a[0] == pc1) or ((a[0] == b[0]== c[0]) and a[0] == pc1)):
				#print()
#Checking diagonals
			#print("Entered into try....")
			for i in range(0,1):
				#print("Entered into first diagonal")
				print(a[0] == p1c)
				print(a[0] == p2c)
				if((a[i] == b[i+1] == c[i+2])):
					if(a[i] == p1c):
						print(p1,"you won the game")
						w = 1
				if((a[i] == b[i+1] == c[i+2])):
					if(a[i] == p2c):
						print(p2,"you won the game")
						w = 1
			if(w == 1):
				break
			for i in range(-1,-2,-1):
				#print("Entered into 2nd diagonal")
				if((a[i] == b[i-1] == c[i-2]) and a[i] == p1c):
					print(p1,"you won the game")
					w = 1
				if((a[i] == b[i-1] == c[i-2]) and a[i] == p2c):
					print(p2,"you won the game")
					w = 1
			if(w == 1):
				break
#Checking columns
			for i in range(0,3):
				#print("Entered into columns")
				if((a[i] == b[i]== c[i]) and a[i] == p1c):
					print(p1,"You won the game")
					w=1
					break
				if((a[i] == b[i]== c[i]) and a[i] == p2c):
					print(p2,"You won the game")
					w=1
					break
			if(w == 1):
				break
#Checking Rows
			for i in range(0,1):
				#print("Entered into rows")
				if((a[i] == a[i+1]== a[i+2]) and a[i] == p1c):
					print(p1,"You won the game")
					w = 1
					break
				if((a[i] == a[i+1]== a[i+2]) and a[i] == p2c):
					w=1
					print(p2,"You won the game")
					break
				if((b[i] == b[i+1]== b[i+2]) and b[i] == p1c):
					print(p1,"You won the game")
					w = 1
					break
				if((b[i] == b[i+1]== b[i+2]) and b[i] == p2c):
					w=1
					print(p2,"You won the game")
					break
				if((c[i] == c[i+1]== c[i+2]) and c[i] == p1c):
					print(p1,"You won the game")
					w = 1
					break
				if((c[i] == c[i+1]== c[i+2]) and c[i] == p2c):
					w=1
					print(p2,"You won the game")
					break
			if(w==1):
				break
		except:
			#print("In catch 2")
			pass
		#print("Hey",ind)
play()
