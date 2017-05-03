#!/usr/bin/env python

import sys

def Person(object):
	def __init___(self, name, strength, dex, stl, per, hp, chp):
		self.Name = name
		self.Strength = strength
		self.Dexterity = dex
		self.Stealth = stl
		self.Perception = per
		self.Health = hp
		self.Current_HP = chp
	
	def takeDmg(self, dmg):
		self.Current_HP -= dmg

	def heal(self, hp):
		self.Current_HP += hp
	
def Enemy(object):
	def __init__(self, name):
		self.Name = name

def main():
	while 1:
		x = raw_input(">>> ")
		if x == 'q':
			print("Correct")
			sys.exit()
		
main()
