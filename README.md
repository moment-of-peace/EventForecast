<div>
<img src="https://github.com/moment-of-peace/EventForecast/blob/master/2015-event-forecast-art_0.JPG"></img>
</div>

-----------------------
# EventForecast
 A group data mining project using Python that aim at predicting the probability of occurence of particular events and the popularity of events.
****************************************************************************
# dataset
Source data: https://www.gdeltproject.org/data.html

Crawled news data on google drive: https://drive.google.com/file/d/0B--MjMVnQr09SmJ2VGh5VkstR2c/view?usp=sharing

Processed data: https://drive.google.com/open?id=0B_YAORWAkCjrMHJFN25MY2tJQ00
*****************************************************************************
### Occurrence Predictoin Model 
Environment: numpy, scipy, tensorflow, keras, h5py
python3 rnn_model.py [option parameter]

-p: the path of precessed events records

-s: step size, how many past days to consider

-a: how many days look ahead

-e: training epochs

### Popularity (hot news) Prediction 
Environment: numpy, scipy, tensorflow, keras, h5py, gensim

python3 rnn_text.py
*****************************************************************************
### Cluster 
Environment: R language:

1.copy the exact data in test.xlsx (X to AP)

2.z=read.table("clipboard",header=T)//import data in to z

3.km <- kmeans(z[,1:20], 3)//use build-in Kmeans function

4.km//print km results

