# EventForecast
 A group data mining project using Python that aim at predicting the probability of occurence of particular events and the popularity of events.

Source data: https://www.gdeltproject.org/data.html
Crawled news data on google drive: https://drive.google.com/file/d/0B--MjMVnQr09SmJ2VGh5VkstR2c/view?usp=sharing

Processed data: https://drive.google.com/open?id=0B_YAORWAkCjrMHJFN25MY2tJQ00

Usage of occurrence predictoin model (required libraries: numpy, scipy, tensorflow, keras, h5py):

python3 rnn_model.py [option parameter]

-p: the path of precessed events records

-s: step size, how many past days to consider

-a: how many days look ahead

-e: training epochs

Usage of popularity (hot topics) prediction (required libraries: numpy, scipy, tensorflow, keras, h5py, gensim):

python3 rnn_text.py
