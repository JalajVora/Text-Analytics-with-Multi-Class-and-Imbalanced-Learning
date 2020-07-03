
# Text-Analytics-with-Multi-Class-and-Imbalanced-Learning
Text Analytics with Multi-Class and Imbalanced Learning

- [Advanced Topics in Machine Learning](https://elearning.ovgu.de/course/view.php?id=7443)
- [project plan on overleaf](https://www.overleaf.com/2797467682nwppqscnczbh)

## Genre Identification on (a sub-set of) Gutenberg Corpus
Consider this set of books belonging to the 19th Century English Fiction1. 
The data set is created from Project Gutenberg 2. The data set consists of about 1000 books and roughly
10 genres. The task here consists of detection (i.e. classification) of genre3 of a book. Each
data-point in this classification task is a fiction book with a label (genre). Please note the
following three main challenges, that you have to consider for your work:
1. Extract features that are relevant to fiction books, which may include ideas like sentiment, setting4 and so on, using appropriate libraries if possible. You cannot hand-in a solution with bag-of-words or simple term incidences, as your feature representation.
1. Outline which models you intend on using and why and how model selection was performed.
1. Explain how the evaluation of the model is being done and how the data set is to be
partitioned while taking into account potential challenges like class imbalances and
similar.

We have one task as a nice-to-have feature (optional): Do you think you can estimate the
bias and variance5 of at least one of your models and also visualize it?

Please **document every** step that has been made in order to solve the challenges. If
you use any libraries in your programming, reference where you have got them and which
version your program uses. At best include the libraries in your contribution if possible
(please do not exceed a certain size in your submission). It is not enough to just use
existing algorithms. **We expect you to extract at least a few features that may
be relevant to fiction books. You are free to make simplified assumptions to
arrive at the features. But mention those assumptions clearly!** You need to
have an understanding, what exactly happens to the data. Therefore you should be able
to explain (and also document!), why certain methods could or could not be used for your
problem. We do not expect perfect results, but the challenges have to be addressed and
we must have the feeling in the end, that you tried to solve them sensibly.