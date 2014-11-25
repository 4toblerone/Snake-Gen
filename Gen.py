#templates
from string import Template

#are single quoted strings more suitable
#then triple quoted ones?
WHITE_SPACE=' '
PASS='pass'
PY_SPACE=4*WHITE_SPACE
CLASS_TEMPLATE = 'class $class_name ($parent_classes):\n'#+PY_SPACE
DEF_TEMPLATE ='def $def_name ($def_args):\n'#+PY_SPACE+PASS
RETURN='return'



def parents_or_args(arglist):
	#returns string from list of args
	#so that () will be later filled with
	return ", ".join(arglist)

def create_class(class_name="SomeClass", parent_classes='object'):

	return Template(CLASS_TEMPLATE).substitute(class_name="NekaKlasa", parent_classes="object")
	

def create_def(def_name="some_function" , def_args = ''):
	#pass
	return Template(DEF_TEMPLATE).substitute(def_name="nekafun", def_args="args")

class Creator(object):

	def __init__(self):
		#stack of parents and childrens
		self.stack = []
		self.code=''
		#num of tabs/4spaces
		self.indentation = 0


	def add_to(self, code_object):
		#i should just append code_object to current
		#code_object
		#self.stack.append(code_object)
		self.code+=self.indentation*PY_SPACE+code_object
		self.indentation+=1
		return self

	def and_close(self, withh=None):
		#indentation can not be less then 0
		#make indentation a property?
		if withh is not None:
			self.add_to(withh+"\n")
		self.indentation-=2
		return self

	@staticmethod
	def write_code(path, file_name,code):
		#write code object to file with name = file_name
		#create new file, write, save to location = path
		pass

	@staticmethod
	def check_syntax(py_file):
		#checks if sytax is correct
		pass

class CodeObject(object):
	pass

c = Creator()
c.add_to(create_class())
print c.code
c.add_to(create_def()).and_close(withh=PASS)
print c.code
c.add_to(create_def()).and_close(withh="return").and_close()
print c.code
#print parents_or_args(['object','str'])

#s = Template(CLASS_TEMPLATE)
#d = Template(DEF_TEMPLATE).substitute(def_name="ime", def_args=parents_or_args(["somearg1","somearg2"]))
#print s.substitute(class_name="some_class" , parent_classes=parents_or_args(['object','str']))+d


