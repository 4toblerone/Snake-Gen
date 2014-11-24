#templates
from string import Template


WHITE_SPACE=' '
PY_SPACE=4*WHITE_SPACE
CLASS_TEMPLATE = 'class $class_name ($parent_classes):\n'+PY_SPACE
DEF_TEMPLATE ='def $def_name ($def_args):\n'+PY_SPACE

def args(arglist):
	#returns string from list of args
	#so that () will be later filled with
	pass

s = Template(CLASS_TEMPLATE)
print s.substitute(class_name="some_class" , parent_classes="object")

