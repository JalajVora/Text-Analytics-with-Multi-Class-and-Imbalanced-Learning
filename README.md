
# Text-Analytics-with-Multi-Class-and-Imbalanced-Learning
Text Analytics with Multi-Class and Imbalanced Learning

This project is part of [Advanced Topics in Machine Learning](http://www.dke.ovgu.de/findke/en/Studies/Courses/Summer+Term+2020/Advanced+Topics+in+Machine+Learning-p-1228.html) subject. Further detailed description of the project can be known in the [documentation of the Project.](https://github.com/JalajVora/Text-Analytics-with-Multi-Class-and-Imbalanced-Learning/blob/master/docs/ATiML_Project_Paper.pdf)

## Problem: Genre Identification on (a sub-set of) Gutenberg Corpus
Consider this set of books belonging to the 19<sup>th</sup> Century English Fiction [<sup>1</sup>](http://dke.ovgu.de/findke/en/Research/Data+Sets-p-1140.html).

The data set is created from Project Gutenberg[<sup>2</sup>](https://www.gutenberg.org). The data set consists of about 1000 books and roughly 10 genres. The task here consists of detection (i.e. multi-class classification) of genre[<sup>3</sup>](https://en.wikipedia.org/wiki/Genre) of a book. Each data-point in this classification task is a fiction book with a label (genre). Please note the following three main challenges tackled:

1. Extract features that are relevant to fiction books, which may include ideas like sentiment, setting[<sup>4</sup>](https://web.csulb.edu/~yamadaty/EleFic.html) and so on, using appropriate libraries. 
2. Outline of all the models used and why and how model selection was performed.
3. Explaination of how the evaluation of the model is being done and how the data set is to be partitioned while taking into account potential challenges like class imbalances and similar.


We have one task as a nice-to-have feature (optional): Can we estimate the bias and variance of at least one of our models and also visualize it?
