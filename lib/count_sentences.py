#!/usr/bin/env python3
import re

class MyString:
  def __init__(self,value=''):
    self.str = value
    pass
  
  def is_sentence(self):
    if self.str[-1] == '.':
      return True
    return False
  
  def is_question(self):
    if self.str[-1] == '?':
      return True
    return False
  
  def is_exclamation(self):
    if self.str[-1] == '!':
      return True
    return False
  
  def count_sentences(self):
    sentences = re.split(r'[.!?]+', self.str)
    return len([s for s in sentences if s.strip()])
  
  @property
  def value(self):
    return self.str
  
  @value.setter
  def value(self,value):
    if not isinstance(value,str):
      print("The value must be a string.")
    else:
      self.str = value
      
  

string = MyString()
#string.value = "This is a string! It has three sentences. Right?"
# string.value = "This is a string!"
# print(string.value)