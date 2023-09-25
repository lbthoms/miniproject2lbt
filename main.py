# INF601 - Advanced Programming in Python
# Lisa Thoms
# Mini Project 2

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# import dataset of KPop Hits 2021
# https://www.kaggle.com/datasets/sberj127/kpop-hits-through-the-years?select=KPopHits2021.csv
# added one addition column - gender
data = pd.read_csv(filepath_or_buffer='KPopHits2021.csv', index_col='artist/s')

print(data.head())


# (10/10 points) Using matplotlib, graph this data in a way that will visually represent the data. Really try to build
# some fancy charts here as it will greatly help you in future homework assignments and in the final project.


# Start of program
try:
    # Create our charts folder
    Path("charts").mkdir()
except FileExistsError:
    pass

# Saves plot
savefile = "charts/" + ".png"
plt.savefig(savefile)

# Shows graph
plt.show()
