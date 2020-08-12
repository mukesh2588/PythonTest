# load libraries
from matplotlib import pyplot
from pandas import read_csv
# Load dataset
from pandas.plotting._matplotlib import scatter_matrix
url = "C:\\Users\\hp\\Downloads\\Python\\iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = read_csv(url, names=names)
# shape
print(dataset.shape)
# head
print(dataset.head(20))
# descriptions
print(dataset.describe())
# class distribution
print(dataset.groupby('class').size())
# Data visualisation
# box and whisker plots
dataset.plot(kind='box', subplots=True, layout=(2, 2), sharex=False, sharey=False)
pyplot.show()
# box and whisker plots
dataset.plot(kind='box', subplots=True, layout=(2, 2), sharex=False, sharey=False)
pyplot.show()
# histograms
dataset.hist()
pyplot.show()

# scatter plot matrix
scatter_matrix(dataset)
pyplot.show()
# scatter plot matrix
scatter_matrix(dataset)
pyplot.show()