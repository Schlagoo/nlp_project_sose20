

# Natural Language Processing

Overview of topics, which should be covered in this project. Submission should include Jupyter Notebook with Requirements file for Dependencies or Virtual Machine.

### Data Mining

Write *Webcrawler* to automatically retrieve textual data from websites. Should be able to analyze syntax and retrieve (filter, map, reduce) important information. Identify and ignore references in *robots.txt*. Identify problems and optimize runtime of crawling algorithm. Data should preferably be in *german*.

* [ ] Large text based dataset (e.g. [Grimm tales](https://www.grimmsmaerchen.net/grimmmaerchen.html) or [The Lord Of The Rings](http://ae-lib.org.ua/texts-c/tolkien__the_lord_of_the_rings_1__en.htm))
* [ ] "Search engine" (notice robots.txt, maybe use sitemap.xml)
* [ ] HTML parser
* [ ] Save data to SQL database

### Preprocessing

Text transformation or preparing. Preprocess mined and saved data. Tokenize raw textual data. Identify and fix grammar based errors. Create basic forms of words. Identify composita and proper names. Use *Spacy* as NLP preprocessing library.

* [ ] Tokenization
* [ ] Error detection
* [ ] Composites
* [ ] Basic forms
* [ ] Proper names
* [ ] (Trie) &rightarrow; Could be visualizing method
* [ ] (Phonetic) &rightarrow; Only if using STT or TTS

### Structuring

Identification of textual elements (word types, homonyms, homophones, homographs, synonyms, composites, abbreviations, proper names, inflections). Integrate part of speech tagging of previous tokenized data. Use *Spacy* as NLP preprocessing library.

* [ ] Split text in or add tokens to words, word types, sentences (POS tagging - STTS)
* [ ] Add punctuation if missing
* [ ] (n-grams) &rightarrow; Not relevant in my opinion 

### Analysis

Extraction of features from structured data. Group word groups (stemming, lemmatization). Create Hamming distance to identify errors (udr in preprocessing or structuring). Apply Successor variety. Rank words by importance. Create bag-of-words. Could use *Sklearn* (see lecture). 

* [ ] Analyse word frequency (Zipf und Luhn) &rightarrow; Could be shown in UI
* [ ] Analysis of similarity (Hemming, Levenstein) used for error detection
* [ ] Stemming (see tiger corpus CONLL09)
* [ ] Lemmatization 
* [ ] Ranking
* [ ] Successor variety
* [ ] Bag-of-words
* [ ] (Venn diagram) &rightarrow; Only if makes sense

### Transformation

Decisions based on analysis of text. Identify added value of data. Use retrieved information to solve project idea. Use ML to generate solution (algorithm depending on idea/solution). Improve and show performance of algorithm. Visualize solution and added value of analysis with web framework (django, flask etc. for python backend functionality, frontend framework of choice).

* [ ] Machine Learning Algorithm
  * k-Means (unsupervised clustering algorithm for data with low variance mostly used in image processing)
  * Nearest centroid (supervised classification algorithm, which assigns classes based on mean centroid)
  * k-Nearest-Neighbor (un- and supervised classification algorithm based on k nearest neighbors)
  * [Text generation with RNN](https://www.tensorflow.org/tutorials/text/text_generation)

* [ ] Confusion matrix (probability matrix)
* [ ] User Interface for information visualization



