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

print parents_or_args(['object','str'])

s = Template(CLASS_TEMPLATE)
d = Template(DEF_TEMPLATE).substitute(def_name="ime", def_args=parents_or_args(["somearg1","somearg2"]))
print s.substitute(class_name="some_class" , parent_classes=parents_or_args(['object','str']))+d


