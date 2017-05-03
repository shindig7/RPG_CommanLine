import os
import re
import csv

def Person(object):
	def __init___(self, name, strength, dex, stl, per, hp, chp)
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

	
