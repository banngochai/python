
def mainlab3():
	print("chọn câu : ")
	print("câu 1  ")
	print("câu 2  ")
	print("câu 3  ")
	print("câu 4  ")
	print("câu 5  ")
	print("câu 6  ")
	print("câu 7  ")
	print("câu 8  ")
	print("câu 9  ")
	
	print("chọn 0 để kết thúc ")
	n1 = int(input("nhập câu muốn chọn : "))

	if n1 ==1:
		dungnumber()
		mainlab3()
	elif n1==2:
		dungbool()
		mainlab3()
	elif n1==3:
		dungchuoi()
		mainlab3()
	elif n1==4:
		dungLists()
		mainlab3()
	elif  n1 ==5:
		dungDictionaries()
		mainlab3()
	elif n1==6:
		dungSets()
		mainlab3()
	elif n1==7:
		dungTuples()
		mainlab3()
	elif n1==8:
		Ham()
		mainlab3()
	elif n1==9:
		dungClasses()
		mainlab3()
	
	elif n1==0:
		print("tạm biệt")
	else:
		print("chọn không hợp lệ mời bạn chọn lại")
		mainlab3()

def sign(x):
	if x>0 :
		return 'pos'
	elif x < 0:
		return 'neg'
	else :
		return 'aeneneem'
class Greeter(object):
	
	def __init__(self, name):
		
		self.name = name
	def greet(self,loud=False):
		if loud :
			print("hello, %s! " % self.name.upper())
		else:
			print('hello %s' % self.name)


def dungnumber():
	x = 3
	print (type(x))
	print (x)
	print (x + 1)
	print (x - 1)
	print (x * 1)
	print (x ** 2)
	x += 1
	print (x)
	x *= 2
	print (x)
	y = 2.5
	print (type(y))
	print (y, y + 1, y * 2, y ** 2)

def dungbool():
	t = True 
	f = False
	print (type(t))
	print (t and f)
	print (t or f)
	print (not t)
	print (t != f)

def dungchuoi():
	hello = 'hello'
	world = "world"
	print(hello)
	print(len(hello))
	hw = hello + ' ' + world
	print(hw)
	hw12 = '%s %s %d' % (hello, world, 12)
	print(hw12)

	s = "hello"
	
	print(s.capitalize())
	print(s.upper())
	print(s.rjust(7))
	print(s.center(7))
	print(s.replace('1', '(ell)'))
	print(' world'.strip())

def dungLists():
	nums = list (range(5))
	print(nums)
	print(nums [2:4])
	print(nums [2:])
	print(nums [:2])
	print(nums [:])
	print(nums [:-1])
	nums[2:4]=[8,9]
	print(nums)

	animals = ['cat','dog','monkey']
	for animal in animals: print(animal)

	animals = ['cat','dog','monkey']
	for idx, animal in  enumerate(animals):
	    print('#%d:%s'%(idx+1,animal))

	nums= [0, 1, 2, 3, 4]
	squares=[]
	for x in nums:
	    squares.append(x ** 2)
	print(squares)

def dungDictionaries():
	d = {'cat': 'cute', 'dog': 'furry'}
	print(d['cat'])
	print('cat' in d)
	d['fish'] = 'wet'
	print(d.get('monkey', 'N/A'))
	print(d.get('fish', 'N/A'))
	del d['fish']
	print(d.get('fish', 'N/A'))
def dungSets():
	animals = {'cat', 'dog'}
	print('cat' in animals)
	print('fish' in animals)
	animals.add('fish')
	print('fish' in animals)
	print(len(animals))
	animals.add('cat')
	print(len(animals))
	animals.remove('cat')
	print(len(animals))

def dungTuples():
	d = {(x, x + 1): x for x in range(10)}
	t = (5, 6)
	print(type(t))
	print(d[t])
	print(d[1, 2])

def Ham():

	for x in [-1,0,1]:
		print(sign(x))
def dungClasses():
	g = Greeter('Fred')
	g.greet()
	g.greet(loud=True)


