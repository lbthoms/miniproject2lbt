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


# graph 1
# bar graph male vs female
# are there more male or female in top hits?
#def graph1 ():

#    male = data['gender'].value_counts()['male']
#    female = data['gender'].value_counts()['female']
#    multi = data['gender'].value_counts()['multi']
#    plt.bar(x='male',  width=0.5, color="orange", height='30')
#
#    # Set the chart title and labels
#    plt.title('Male Versus Female Top Tracks')
#    plt.xlabel('Gender')
#    plt.ylabel('Number of Songs')

    # Saves plot
    # savefile = "charts/gender.png"
    # plt.savefig(savefile)

    # Shows graph
   # plt.show()
#
# graph1()


# graph 2
# tempo vs danceability
# are high tempo songs more "danceable"?
def graph2():
    # plot graph w/ x,y labels and title
    data.plot(x='tempo', y='danceability', style='o')
    plt.xlabel("Tempo")
    plt.ylabel("Danceability")
    plt.title("Top 50 K-POP Hits 2021 \n Tempo Vs. Danceability")

    # save file to charts folder
    savefile2 = "charts/tempovsdance.png"
    plt.savefig(savefile2)
    plt.show()


# graph 3
# speechiness vs. length
# is a song with more lyrics likely to be longer or shorter?

def graph3():
    # plot graph w/ x,y labels and title
    data.plot(x='speechiness', y='duration_sec', style='o')
    plt.xlabel("Speechiness")
    plt.ylabel("Duration in Seconds")
    plt.title("Top 50 K-POP Hits 2021 \n Speechiness Vs. Song Duration")

    # save file to charts folder
    savefile3 = "charts/speechvslength.png"
    plt.savefig(savefile3)
    plt.show()



# graph 4
# bar graph major vs minor
# is one more likely to be in the top 50?

#def graph4():

#graph4()





# graph 5
# valence vs loudness plot graph
# is a song with higher valence ("happier") louder?
def graph5():
    #plot graph w/ x,y labels and title
    data.plot(x='valence', y='loudness', style='o')
    plt.xlabel("Valence")
    plt.ylabel("Loudness")
    plt.title("Top 50 K-POP Hits 2021 \n Loudness vs. Valence")

    #save file to charts folder
    savefile5 = "charts/loudvsval.png"
    plt.savefig(savefile5)
    plt.show()


# Add/create folder and save graph
try:
    # Create charts folder
    Path("charts").mkdir()
except FileExistsError:
    pass

#graph1()
graph2()
graph3()
#graph4()
graph5()
