
## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Run](#run)

## General info
Sentiment Analysis program designed to monitor public opinion based on a given trend. 
	
## Technologies
Project is created with:
* TextBlob
* Matplotlib
* Tweepy
	
## Setup
To run this project, install it as follows:

```
$ cd ../op_osint
$ sudo python3 -m pip install -r requirements.txt
$ sudo python3 -m textblob.download_corpora

```

## Run
Add Twitter API keys to secrets.py

```
$ python3 analyse.py --help
```

