from data_load import load
from preparation import pre_processing
# import function_pp
#import numpy as np
#import seaborn as sns
#import matplotlib.pyplot as plt
#from function_pp import pre_processing

#load_trans = data_load.load(True, False)
#print(load_trans)


x = load(True, True, join_df = 'inner')
print(x.info())


