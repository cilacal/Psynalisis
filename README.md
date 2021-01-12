# Psynalisis - psychedelic data science
This project is going to have three parts (later of course in different repositories):

1. Analysis of drug experiences downloaded from [erowid.org](https://erowid.org) (with the help of the script of [basnijholt](https://github.com/basnijholt/psychedelic-data-science)).

   The following analyses is planned: 

   - Data exploration, visualization: 

     - Data preparation [x]
     - Word clouds based on [TF-IDF](http://www.tfidf.com/) separately for word classes (similar to [this](https://www.rehabs.com/explore/drug-experiences/))[X]
     - Visualization on drug symbols [X]
     - Vocabulary complexity comparison [ ]

   - Classification:

     - Grouping drug experiences based on the most frequent words in them, a.k.a. [topic modelling](https://en.wikipedia.org/wiki/Topic_model) [ ]
     - ...based on their sentiments [ ]
     - ...most significant emotions [ ]

   - Sentiment analysis:

     - Categorizing experiences into *positive, negative and neutral* groups [ ]
     - Finding the most significant emotions of the experiences [ ]

     

2. Creating a web application to find keywords based on TF-IDF. 

   - Creating a website where users can upload several documents in order to create a vocabulary. This vocabulary will be the basis to find keywords in further uploaded documents. [ ]

   - API will be provided to enable these functionalities without the use of the GUI. [ ]

     

3. Future plan: Analyzing National Survey on Drug Use and Health, 2012 [dataset](https://www.icpsr.umich.edu/web/ICPSR/studies/34933#).

   The following analyses is planned:

   - Data exploration, visualization. [ ]
   - Advance analysis of the data using statistical methods. [ ]
   - Evaluating the risk to be drug consumer for each drug by giving manually input data. [ ]

   Creation of a website with the following functionalities is planned:

   - Users can fill the input parameters similar to the [above dataset](https://github.com/deepak525/Drug-Consumption) manually and they receive the risk to be drug consumer for each drug (in the seven category). [ ]
- Adding sites to show the results of the above described (_1)_) sentiment analysis and classification problems. [ ]

