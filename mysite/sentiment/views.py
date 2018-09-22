from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import MyForm

import nltk
import random
#from nltk.corpus import movie_reviews
from nltk.classify.scikitlearn import SklearnClassifier
import pickle
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC
from nltk.classify import ClassifierI
from statistics import mode
from nltk.tokenize import word_tokenize




short_pos = open("C:\\Users\\Inspiron\\Desktop\\positive3.txt","r").read()
short_neg = open("C:\\Users\\Inspiron\\Desktop\\negative3.txt","r").read()
all_words = []
allowed_word_types = ["J","R"]
documents = []

for p in short_pos.split('\n'):
        documents.append( (p, "This is a POSITIVE statement.") )
        words = word_tokenize(p)
        pos = nltk.pos_tag(words)
        for w in pos:
            if w[1][0] in allowed_word_types:
                all_words.append(w[0].lower())

for p in short_neg.split('\n'):
        documents.append( (p, "This is a NEGATIVE statement.") )
        words = word_tokenize(p)
        pos = nltk.pos_tag(words)
        for w in pos:
            if w[1][0] in allowed_word_types:
                all_words.append(w[0].lower())

def find_features(document):
    

    words = word_tokenize(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)

    return features
all_words = nltk.FreqDist(all_words)
word_features = list(all_words.keys())[:20000]
featuresets = [(find_features(rev), category) for (rev, category) in documents]
random.shuffle(featuresets)
training_set = featuresets[:3000]
testing_set = featuresets[3000:]



class VoteClassifier(ClassifierI):
    def __init__(self, *classifiers):
        self._classifiers = classifiers

    def classify(self, features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)
        return mode(votes)

    def confidence(self, features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)

        choice_votes = votes.count(mode(votes))
        conf = choice_votes / len(votes)
        return conf





classifier = nltk.NaiveBayesClassifier.train(training_set)
MNB_classifier = SklearnClassifier(MultinomialNB())
MNB_classifier.train(training_set)
BernoulliNB_classifier = SklearnClassifier(BernoulliNB())
BernoulliNB_classifier.train(training_set)
LogisticRegression_classifier = SklearnClassifier(LogisticRegression())
LogisticRegression_classifier.train(training_set)
LinearSVC_classifier = SklearnClassifier(LinearSVC())
LinearSVC_classifier.train(training_set)
SGDC_classifier = SklearnClassifier(SGDClassifier())
SGDC_classifier.train(training_set)
voted_classifier = VoteClassifier(
                                  classifier,
                                  LinearSVC_classifier,
                                  MNB_classifier,
                                  BernoulliNB_classifier,
                                  LogisticRegression_classifier)





def sentimentanalyser(request):
    if request.method=='POST':
        form=MyForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            text = cd.get('your_review')
            

            


            feats = find_features(text)
            ratingreview=voted_classifier.classify(feats),voted_classifier.confidence(feats)
            return render(request,'sentiment/leaffile.html',{'ratingreview':ratingreview})
            #return HttpResponseRedirect('/thanks/')
    else:
        form=MyForm()
        
    return render(request,'sentiment/rootfile.html',{'form':form})




