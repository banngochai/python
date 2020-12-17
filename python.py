from lab1 import  mainlab1
from lab2 import  mainlab2
from lab3 import  mainlab3
from baitap1 import  mainbt1


def main():
	print("Chương trình bài tập python")
	print("1 : lab 1")
	print("2 : lab 2")
	print("3 : lab 3")
	print("4 : Bài tập 1")
	print("chọn 0 để kết thúc ")

	n = int(input("Mời bạn chọn Bài tập muốn xem : "))
	
	if n ==1:
		mainlab1()
	elif n==2:
		mainlab2()
	elif n==3:
		mainlab3()
	elif n==4:
		mainbt1()
	elif n==0:
		print("tạm biệt")
	else:
		print("chọn không hợp lệ mời bạn chọn lại")
		main()

if __name__ == '__main__':
	main()

