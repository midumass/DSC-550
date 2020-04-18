import matplotlib as plt
import numpy as np
import pandas as pd

df = pd.read_csv('sample.csv')

rows = 10
cols = 5 ** rows

rand = np.random.randint(low = 1, high = 500, size = size)