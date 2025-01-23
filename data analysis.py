import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
try:
    df = pd.read_csv("Iris.csv")

    print(df.head())
    print(df.columns)
    print(df.describe())
    print(df.shape)

    print(df['Species'].value_counts())


    print(df['SepalLengthCm'].mean())
    print(df['SepalWidthCm'].mean())
    print(df['PetalLengthCm'].mean())
    print(df['PetalWidthCm'].mean())

    sepalLength = df['SepalLengthCm']
    sepalWidth = df['SepalWidthCm']

    #Creating a line graph in matplotlib
    plt.plot(sepalWidth,sepalLength)
    plt.title("A line graph of Sepal Width against Sepal Length")
    plt.xlabel("Sepal Width")
    plt.ylabel("Sepal Length")
    plt.show()


    #Using seaborn to create a scatter diagram

    sns.scatterplot(data=df, x="SepalWidthCm", y="SepalLengthCm", hue="Species")
    plt.title("A scatter diagram of sepal width against sepal length")
    plt.show()



    # Creating a pair plot for the Iris dataset
    sns.pairplot(data=df, hue="Species", diag_kind="hist")
    plt.suptitle("Pair Plot of the Iris Dataset", y=1.02)
    plt.show()

    # A histogram comparing sepal lengths

    sns.histplot(data=df, x="SepalLengthCm", hue="Species", kde=True, bins=20, palette="viridis")
    plt.title("Histogram of Sepal Length by Species")
    plt.xlabel("Sepal Length (cm)")
    plt.ylabel("Frequency")
    plt.show()
except FileNotFoundError:
    print("The specified file can't be reached")



