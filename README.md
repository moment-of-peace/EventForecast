<div>
<img src="https://github.com/moment-of-peace/EventForecast/blob/master/data/event-forecast-art_0.JPG"></img>
</div>

-----------------------
# EventForecast
A group data mining project using deep learning (LSTM) aiming at predicting the probability of occurence of particular events and the popularity of events.
****************************************************************************
### dataset
Source data: https://www.gdeltproject.org/data.html

Crawled news data on google drive: https://drive.google.com/file/d/0B--MjMVnQr09SmJ2VGh5VkstR2c/view?usp=sharing

Processed data: https://drive.google.com/open?id=0B_YAORWAkCjrMHJFN25MY2tJQ00
*****************************************************************************
### Occurrence Prediction 
Environment: numpy, scipy, tensorflow, keras, h5py

python3 rnn_model.py [option parameter]

-p: the path of precessed events records for a certain country (any "attr-country" folder in the processed data link)

-s: step size, how long history to consider

-a: how many days look ahead (which day in the future to predict)

-e: training epochs

### Popularity (hot events) Prediction 
Environment: numpy, scipy, tensorflow, keras, nltk, h5py, gensim. 

python3 rnn_text.py [option parameter]

-f: word2vec model file

-d: processed news data (the "news-64" folder in the processed data link)

-b: batch

-l: cutting length, i.e. how many words in the news to consider

-e: training epochs
*****************************************************************************
### Cluster 
Environment: R language:

1.copy the exact data in test.xlsx (X to AP)

2.z=read.table("clipboard",header=T)//import data in to z

3.km <- kmeans(z[,1:20], 3)//use build-in Kmeans function

4.km//print km results

