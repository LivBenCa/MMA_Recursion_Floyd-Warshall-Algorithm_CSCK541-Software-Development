"""
Simple demo of non-keyword arguments
"""

def print_out_simple_arguments(*args):
  """
  Print out the contents of *args
  """
  for arg in args:
    print (arg)

def print_out_keyword_arguments(**kwargs):
  """
  Print out contents of **kwargs
  """
  for arg, value in kwargs.items():
    print (f"Parameter {arg} \t Argument {value}")

print_out_simple_arguments('This', 'is', 'a', 'test')

print_out_keyword_arguments(determiner = 'This', \
                            stopword = 'is', article ='a', noun = 'test')