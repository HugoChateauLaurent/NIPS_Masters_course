#python 2 - pianoroll to midi function
import sys
import pickle
sys.path
sys.path.append('./midi')

import numpy as np
from midi import utils    

def pr2midi(pianoroll, i=1):
    filename = './Test/piano_rolls/pianoroll_'+ str(i) + '.mid'
    print(pianoroll.shape)
    utils.midiwrite(filename, pianoroll.T, (32, 93), .1) # 3rd arg is the start and end notes; 4rth arg is time between sample
    i += 1      



#python2 - converts all the pianorolls to midi 
with open('Test/piano_rolls.pickle', 'rb') as file:
    pr_arr = pickle.load(file)
    print len(pr_arr)

i=0
for pr in pr_arr:
	pr2midi(pr_arr[i], i)
	i+=1
