import os
import re
import csv

def Person(object):
	def __init___(self, name, str, dex, stl, per, hp, chp)
		self.Name = name
		self.Strength = str
		self.Dexterity = dex
		self.Stealth = stl
		self.Perception = per
		self.Health = hp
		self.Current_HP = chp
	
	# Accessors
	def getName(self):
		return self.Name
	
	def getStrength(self):
		return self.Strength
	
	def getDexterity(self):
		return self.Dexterity
	
	def getStealth(self):
		return self.Stealth
	
	def getPerception(self):
		return self.Perception
	
	def getHealth(self):
		return self.Health
	
	def getCurrentHP(self):
		return self.Current_HP
	
	#  Mutators
	def takeDamage(self, damage):
		self.Current_HP -= damage
	
	def setCurrentHP(self, hp)
		self.Current_HP = hp