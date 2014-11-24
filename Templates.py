#templates
from string import Template

#are single quoted strings more suitable
#then triple quoted ones?
WHITE_SPACE=' '
PY_SPACE=4*WHITE_SPACE
CLASS_TEMPLATE = 'class $class_name ($parent_classes):\n'+PY_SPACE
DEF_TEMPLATE ='def $def_name ($def_args):\n'+PY_SPACE
RETURN='return'
PASS='pass'


def parents_or_args(arglist):
	#returns string from list of args
	#so that () will be later filled with
	return ", ".join(arglist)

def create_class(class_name="SomeClass", parent_classes='object'):
	pass

def create_def(def_name="some_function" , def_args = ''):
	pass


class Creator(object):

	def __init__(self):
		#stack of parents and childrens
		self.stack = []

	def add_to(self, code_object):
		#adds to the code object at the top of the stack
		#aka to the current parent
		pass

	def close_obj(self, withh=PASS):
		#closes aka removes code object from the top of the stack
		#it should close it with some other code object
		#default is python pass statement
		pass

	@staticmethod
	def write_code(path, file_name):
		#write code object to file with name = file_name
		#create new file, write, save to location = path
		pass

	@staticmethod
	def check_syntax(py_file):
		#checks if sytax is correct
		pass

print parents_or_args(['object','str'])

s = Template(CLASS_TEMPLATE)
d = Template(DEF_TEMPLATE).substitute(def_name="ime", def_args=parents_or_args(["somearg1","somearg2"]))
print s.substitute(class_name="some_class" , parent_classes=parents_or_args(['object','str']))+d


