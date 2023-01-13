def string_int(txt):
	nolist=[]
	for i in range (len(txt)):
		match txt[i]:
			case "0":
				nolist.append(0)
			case "1":
				nolist.append(1)
			case "2":
				nolist.append(2)
			case "3":
				nolist.append(3)
			case "4":
				nolist.append(4)
			case "5":
				nolist.append(5)
			case "6":	
				nolist.append(6)
			case "7":
				nolist.append(7)
			case "8":
				nolist.append(8)
			case "9":
				nolist.append(9)
	no=int()
	for i in range(len(nolist)):
		no= (no*10)+nolist[i]
	return no

print(string_int("21431"))