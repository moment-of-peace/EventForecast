<div>
<img src="https://github.com/moment-of-peace/EventForecast/blob/master/data/award.jpeg"></img>
</div>
-----------------------

website: https://github.com/moment-of-peace/EventForecast

# EventForecast
A group data mining project using deep learning (LSTM) aiming at predicting the probability of occurence of particular events and the popularity of events.
This project is granted "The Best Data Mining Project Award" of the University of Queensland in 2017
****************************************************************************
### dataset
Source data: https://www.gdeltproject.org/data.html

Crawled news data on google drive: https://drive.google.com/file/d/0B--MjMVnQr09SmJ2VGh5VkstR2c/view?usp=sharing

Processed data: https://drive.google.com/drive/folders/0B_Qs_6HNIHS9Qk1hMzZ1c3VWOE0?usp=sharing
*****************************************************************************
### Occurrence Prediction 
Environment: numpy, scipy, tensorflow, keras, h5py, matplotlib

Require at leat one "attr-county" folder provided by processed data link above (need to unzip first)

Use following command to run (-p is compulsory, others are optional):

python3 rnn_model.py [option parameter]

-p: the path of precessed events records for a certain country (any "attr-country" folder in the processed data link)

-s: step size, how long history to consider

-a: how many days look ahead (which day in the future to predict)

-e: training epochs

### Popularity (hot events) Prediction 
Environment: numpy, scipy, tensorflow, keras, nltk, h5py, gensim. 

Require folder "news_50_num" (need to unzip first), and word embedding files "vocab_event100.pkl", "weights_event100.npy"
provided by the processed data link above

Use following command to run (all options are optional):

python3 rnn_text.py [option parameter]

-b: batch

-l: cutting length, i.e. how many words in the news to consider

-e: training epochs
*****************************************************************************
### Cluster 
Environment: R language:

1.copy the exact data in data/test.xlsx (X to AP)

2.z=read.table("clipboard",header=T)//import data in to z

3.km <- kmeans(z[,1:20], 3)//use build-in Kmeans function

4.km//print km results
*****************************************************************************
### Other files
preprocessing.py: general preprocessing, including removing useless data, extract and count events and so on.

nlp_preprocessing.py: special preprocessing for text analysis, including removing common words, stemming, and so on

hot_news_php/ : files for the webpage application about hot news recommendation

association_rule/ : codes association rules mining

cluster/ : files and results for clustering
