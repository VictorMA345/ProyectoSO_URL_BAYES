import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB 
import inspect

#dataset from kaggle  
recommendation_dataset = pd.read_csv('dmoz.csv')
recommendation_dataset = recommendation_dataset[recommendation_dataset['desc'].notna()]#remove nan rows from the dataset 

#importing multinominal naive bayes 

#splitting train and test data
X_train, X_test, y_train, y_test = train_test_split(recommendation_dataset['desc'], recommendation_dataset['category'], random_state = 5)

count_vect = CountVectorizer()

X_train_counts = count_vect.fit_transform(X_train)

tfidf_transformer = TfidfTransformer()

X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)

datos = [['Nirvana - Smells Like Teen Spirit (Official Music Video) - YouTube'], [""]]

classifier = MultinomialNB().fit(X_train_tfidf, y_train)#train the train data with MultinomialNB model

result = classifier.predict(count_vect.transform([str(datos[1][0])]))

print(inspect.getsource( tfidf_transformer.fit_transform))
