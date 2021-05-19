# Language-Detection

## Overview:-

* This is Natural language processing (NLP) project to detect language from text using machine learning. this model can detect 
**79** Languages.

## Data:-

* We got dataset from [here](https://downloads.tatoeba.org/exports/) in which their are more than 94 lakh rows but we did not needed that much so after preprocessing we 
have 6K for some languages.

## Model Training:-

* First trained pipeline of Logistic Regressor with Tf*Idf vectorizer without any hyperparameters.
* And then Tf*Idf with ngrams (1,3) means all bigram, trigrams and with analyzer as characters means model will train of characters not on words got **95%** accuracy.

## Predictions:-

<img src="https://user-images.githubusercontent.com/75840165/118815668-0e255200-b8cf-11eb-907b-da2e4a30c3d6.jpg" height=250 width=550>
<img src="https://user-images.githubusercontent.com/75840165/118815661-0bc2f800-b8cf-11eb-9aba-650a61aad6fc.jpg" height=250 width=550>
