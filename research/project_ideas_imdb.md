# NLP project ideas IMDb data

### Data

Example reviews see [here](https://www.imdb.com/title/tt0113277/reviews?ref_=tt_urv).

```json
{
    "<movie_name>" : [
        {
            "rating": int,
            "title": string,
            "user_name": string,
            "user_url": link,
            "creation_date": timestamp,
            "description": string,
            "helpfulness": ratio
        }    
	]
}
```

### Crawler + Preprocessing

Identify movie pages and find review section. Fetch all reviews with above information. Preprocess data mit spaCy. Tokenize title and description? Hold data in pandas dataframe. Save data in JSON files (one file per movie?) or NoSQL database running in docker container. 

### Structuring + Analysis

Fetch data from data source. Structure text by splitting sentences into words and run POS tagging.

1. Detect and fix errors like missing punctuation or spelling mistakes (hemming, levensteins).
2. Try to identify characters by proper names.
3. Analyze word frequency to identify plot relevant words (zipf & luhn). Build basic form of relevant words (stemming).

### Transformation

Vectorize words in text.

1. **Build movie character descriptions based on review description analysis. Need to identify movie characters (maybe actors?) and analyze their personality.**
2. **Build relations of movie characters. Need to identify characters and their relations by finding sentences where multiple characters are described by an relation.**
3. **Identify different locations (cities, ...) in movie**
4. **Find similar movies**
5. **Generate new plots based on review descriptions as training data with RNN/LSTM**

Visualize results in UI.

