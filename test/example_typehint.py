from typing import List
from typing import Tuple, Set
from typing import Dict
from typing import Optional

def get_full_name(first_name: str, last_name: str):
	full_name = first_name.title() + " " + last_name.title()
	return full_name


def get_name_with_age(name: str, age: int):
	name_with_age = name.title() + " is this old: " + str(age)
	return name_with_age


def process_items(items: List[str]):
	'''
	#use for each element
	for item in items:
		print(item, sep=" ")
	'''
	print(*items)


def process_tupset(items_t: Tuple[int, int, str], items_s: Set[bytes]):
	print(*items_t, *items_s)
	

def process_dict(items_d: Dict[str, int]):
	for name, price in items_d.items():
		print(name)
		print(price)

def say_hi(name: Optional[str] = None):
	if name is not None:
		print(f"Hey {name}!")
	else:
		print("Hello world")


print(get_full_name("john", "doe"))

print(get_name_with_age("john", 40))

process_items(["j", "o", "n"])

process_tupset((1, 2, "doe"), {255, 10, 255})

process_dict({"cloth": 200, "jeans": 500})

say_hi()
say_hi("indy")

##with class
class Person:

	def __init__(self, name: str):
		self.name = name

	def get_name(self):
		return self.name

def get_person_name(one_person: Person):
	return one_person.name.title()


person: Person = Person("chris")
print(get_person_name(person))

print(person.get_name())

#no need define type, just create from class
another_person = Person("bratt")
print(another_person.name.title())