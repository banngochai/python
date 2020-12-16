

def mainlab2():
	print("chọn câu : ")
	print("câu 1  ")
	print("câu 2  ")
	print("câu 3  ")
	print("câu 4  ")
	print("câu 5  ")
	print("chọn 0 để kết thúc ")
	n1 = int(input("nhập câu muốn chọn : "))

	if n1 ==1:
		cau1()
		mainlab2()
	elif n1==2:
		cau2()
		mainlab2()
	elif n1==3:
		cau3()
		mainlab2()
	elif n1==4:
		cau4()
		mainlab2()
	elif  n1 ==5:
		cau5()
		mainlab2()
	elif n1==0:
		print("tạm biệt")
	else:
		print("chọn không hợp lệ mời bạn chọn lại")
		mainlab2()



def cau1():
	n = int(input('so phan tu: '))
	lst = []
	for i in range(n):
		lst.append(int(input()))
	min_value = lst[0]
	for i in lst:
		if i < min_value:
			min_value = i
	print(min_value)

def cau2():
	n = int(input('so phan tu: '))
	lst = []
	for i in range(n):
		lst.append(int(input()))
	answer = 0
	for v in lst:
		answer += v
	print(answer)

def cau3():
	lst = []
	n = int(input('so phan tu:' ))
	for i in range(n):
		lst.append(int(input()))
	for i in range(len(lst)):
		for j in range(i):
			if lst[i] < lst[j]:
				tmp = lst[i]
				lst[i] = lst[j]
				lst[j] = tmp
	print(lst)
def cau4():
	lst = []
	n = int(input('so phan tu: '))
	for i in range(n):
		lst.append(int(input()))
	answer = []
	for v in lst:
		if v % 2!=0:
			answer.append(v)
	print(answer)

def cau5():
	lst = []
	n = int(input('so phan tu: '))
	for i in range(n):
		lst.append(int(input()))
	answer = []
	for v in lst:
		if v % 5 == 0:
			answer.append(v)
	if len(answer) == 0:
		answer = [0]
	print(answer)
