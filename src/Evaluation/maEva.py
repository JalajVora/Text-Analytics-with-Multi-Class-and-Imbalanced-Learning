import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA, KernelPCA
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import KNNImputer, IterativeImputer
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split, cross_val_score, RepeatedStratifiedKFold
from sklearn.metrics import balanced_accuracy_score
from imblearn.over_sampling import RandomOverSampler

def GetTrainTestSplit(features, labels, to_be_dropped = ['Allegories', 'Christmas Stories'], use_pca = True, use_imp = True,
                     draw_plot = False, over_sample = True):

    y = labels.values
    x = features

    if use_imp:
        imp = IterativeImputer(max_iter=10, random_state=42)
        x = imp.fit_transform(x)
    
    if use_pca:
        kpca = KernelPCA(kernel="rbf", fit_inverse_transform=True, gamma=10)
        x = kpca.fit_transform(x)
        
    #drop all instances of underepresented genres
    for genre in to_be_dropped:   
        y_ind = np.where(y == genre)
        x = np.delete(x, y_ind[0], 0)#x.drop(index = y_ind[0])
        y = np.delete(y, y_ind[0], 0)
    
    X_train , X_test , y_train, y_test = train_test_split(x, y, stratify=y)
    
    if draw_plot:
        plt.figure(figsize=(24, 6))
        plt.bar(pd.value_counts(y_train).index, pd.value_counts(y_train))
        plt.bar(pd.value_counts(y_test).index, pd.value_counts(y_test))
    if over_sample:
        ros = RandomOverSampler(random_state=42)
        X_train, y_train = ros.fit_resample(X_train, y_train)
    return (X_train, y_train, X_test, y_test)


def GetTrainTestFromSplit(train_features, test_features, labels, to_be_dropped = ['Allegories', 'Christmas Stories'],
                          use_pca = True, use_imp = True, draw_plot = False, over_sample = True):
    y = labels.values
    x = pd.concat([train_features, test_features])
    
    if use_imp:
        imp = IterativeImputer(max_iter=10, random_state=42)
        x_ = imp.fit_transform(x)
    if use_pca:
        kpca = KernelPCA(kernel="rbf", fit_inverse_transform=True, gamma=10)
        x_ = kpca.fit_transform(x)
        
    x = pd.DataFrame(data=x_, index=x.index, columns=x.columns)

    x_train = x.head(len(train_features.index))
    x_test = x.tail(len(test_features.index))
    
    #drop all instances of underepresented genres
    for genre in to_be_dropped:
        y_ind_train = np.where(labels[x_train.index] == genre)
        y_ind_test = np.where(labels[x_test.index] == genre)
        x_train = x_train.drop(index = x_train.index[y_ind_train[0]])
        x_test = x_test.drop(index = x_test.index[y_ind_test[0]])
        
    if draw_plot:
        plt.figure(figsize=(24, 6))
        plt.bar(pd.value_counts(labels[x_train.index]).index, pd.value_counts(labels[x_train.index]))
        plt.bar(pd.value_counts(labels[x_test.index]).index, pd.value_counts(labels[x_test.index]))
    if over_sample:
        ros = RandomOverSampler(random_state=42)
        x_train = ros.fit_resample(x_train)
    return (x_train, x_test)


def GetAccuracy(y_test, predictions):
    #this function should actually already do the trick, already will weigh literary less since its represented by more instances
    return balanced_accuracy_score(y_test, predictions)