#Talking Data Starter Code

#Part 2 Setting up the program
import pandas as pd
import matplotlib.pyplot as plt

#-------for color----------
# colorama_demo.py
from colorama import init, Fore, Back, Style
# Initializes Colorama
init(autoreset=True)

pd.set_option('display.max_columns', None)
pd.set_option('max_colwidth', None)

movieData = pd.read_csv('./rotten_tomatoes_movies.csv')
favMovie = "Deadpool"

print("My favorite movie is " + favMovie + "! \n")

#deadpool ascii art
print(Fore.RED + "        ooooooo | ooooooo      ")
print(Fore.RED + "       oooooooo | oooooooo     ")
print(Fore.RED + "      ooooooooo | ooooooooo    ")
print(Fore.RED + "      ooo " + Fore.WHITE + ":::.  " + Fore.RED + "|" +  Fore.WHITE + "  .:::" + Fore.RED + " ooo   ")
print(Fore.RED + "      ooo " + Fore.WHITE + ":::   " + Fore.RED + "|" + Fore.WHITE + "   :::" + Fore.RED + " ooo   ")
print(Fore.RED + "      oooooooo  |  oooooooo   ")
print(Fore.RED + "       ooooooo  |  ooooooo    ")
print(Fore.RED + "        oooooo  |  oooooo     \n")

#Part 3 Investigate the data
#print(movieData.head())
#print("\n" + movieData["movie_title"])

#Part 4 Filter data
print("\nThe data for my favorite movie is:\n")
#Create a new variable to store your favorite movie information

favMovieBooleanList = movieData["movie_title"] == favMovie

favMovieData = movieData.loc[favMovieBooleanList]
print(favMovieData)

print("\n\n")

#Create a new variable to store a new data set with a certain genre

actionMovieBooleanList = movieData["genres"].str.contains("Action")

actionMovieData = movieData.loc[actionMovieBooleanList]


numOfMovies = actionMovieData.shape[0]

print("We will be comparing " + favMovie +
      " to other movies under the genre Action in the data set.\n")
print("There are " + str(numOfMovies) + " movies under the category Action.")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
input("Press enter to see more information about how " + favMovie +
      " compares to other movies in this genre.\n")

#Part 5 Describe data
#min
min = actionMovieData["audience_rating"].min()
print("The min audience rating of the data set is: " + str(min))
print(favMovie + " is rated 90 points higher than the lowest rated movie.")
print()

#find max
max = actionMovieData["audience_rating"].max()
print("The max audience rating of the data set is: " + str(max))
print(favMovie + " is rated 8 points lower than the highest rated movie.")
print()

#find mean
mean = actionMovieData["audience_rating"].mean()
print("The mean audience rating of the data set is: " + str(mean))
print(favMovie + " is higher than the mean movie rating.")
print()

#find median
median = actionMovieData["audience_rating"].median()
print("The median audience rating of the data set is: " + str(median))
print(favMovie + " is higher than the median movie rating.")
print()

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
input("Press enter to see data visualizations.\n")

#Part 6 Create graphs
#Create histogram

plt.hist(actionMovieData["audience_rating"], range = (0,100), bins = 20)

#Adds labels and adjusts histogram
plt.grid(True)
plt.title("Audience Ratings of Action Movies")
plt.xlabel("Audience Ratings")
plt.ylabel("Number of Action Movies")

#Prints interpretation of histogram
print(
  "According to the histogram, most action movies fall under audience ratings between 60 and 65%. The model is nearly normal with a unimodal and symmetric distribution. As a result, the mean is an accurate measure of center to study the data. The histogram surprised me as I believed that because action movies are so popular that viewers would rate them higher on average. However, the model shows us that since before October 2020, audience ratings tend to fall between 60 and 65% on the lower spectrum of the movie rating system. \n"
)
print("Close the graph by pressing the 'X' in the top right corner.")
print()

#Show histogram
plt.show()

#Create scatterplot
plt.scatter(data = actionMovieData, x = "audience_rating", y = "critic_rating")

#Adds labels and adjusts scatterplot
plt.grid(True)
plt.title("Action Movie Audience Rating vs. Action Movie Critic Rating")
plt.xlabel("Audience Rating")
plt.ylabel("Critic Rating")
plt.xlim(0, 100)
plt.ylim(0, 100)

#Prints interpretation of scatterplot
print(
  "According to the scatter plot, its strength is moderate, linear in form, and positive in direction. There exists a moderate correlation between critic and audience rating in reference to action movies. Outliers do stray away from the linear trend, but they lack leverage and influence that would otherwise significantly influence the trends the scatter plot currently displays."
)
print()

print("Close the graph by pressing the 'X' in the top right corner.")

#Show scatterplot
plt.show()

print("\nThank you for reading through my data analysis!")
