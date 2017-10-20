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
Usage of occurrence predictoin model (required libraries: numpy, scipy, tensorflow, keras, h5py):
for example: cmd > pip install numpy 
python3 rnn_model.py [option parameter]

-p: the path of precessed events records

-s: step size, how many past days to consider

-a: how many days look ahead

-e: training epochs

# Usage of popularity (hot topics) prediction (required libraries: numpy, scipy, tensorflow, keras, h5py, gensim):

python3 rnn_text.py
*****************************************************************************
Cluster R language:

1.copy the exact data in test.xlsx (X to AP)

2.z=read.table("clipboard",header=T)//import data in to z

3.km <- kmeans(z[,1:20], 3)//use build-in Kmeans function

4.km//print km results

******************************************************************************
software:Tableau public

username: shijie.zhang@uqnnect.edu.au

password: 011010642zsj

due to the public version, we cannot import the actual graph in Tableau. hence, please login our

account and check presentation1 and presentation2.

*******************************************************************************
