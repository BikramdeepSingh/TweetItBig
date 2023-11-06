## Appendix

Is there any way to forecast the use of tweets for any good? People take part in conversations with similar interests. But do they feel benefited by that? Can any good be done with these tweets? Should there be any use case proposed using twitter handle? Having bulk of data across the internet is of no use if that cannot be converted into information. Forming informational content from flowing pipelines of data and marking the point of interest for each user is what can excite a **_‘Tweeter.’_**

# TweetItBig

**TweetitBig** is a dashboard application working as a website to serve the user by providing statistical interpretations of Twitter data based on certain search keywords.
The keywords which are most likely to be chosen by 9 out of 10 people are related to apple.
This website revolves around this selection and goes beyond textual analysis to form a website of its own.

## Authors

- [@Bikramdeep-Singh](https://github.com/BikramdeepSingh)
- [@Surya-Bansal](https://github.com/Surya-Bansal)
- [@Mobassiralam-Shaikh](https://github.com/mobassir20)
- [@Jagvinder-Singh](https://github.com/jagvindersingh)
- [@Raj-Jethva](https://github.com/JethvaRaj)
- [@Parth-Mavani](https://github.com/parth-mavani)
- [@Vikas](https://github.com/vicky5060)
- [@Krishna-Patel](https://github.com/Krisnaa15)
- [@Tanishq-Taneja](https://github.com/TanishqTaneja)


## Website Snapshots

- Home page
The initial point of engagement for individuals seeking information or access to TweetitBig.

![App Screenshot](https://github.com/BikramdeepSingh/TweetItBig/blob/main/media/main_page.png?raw=true)

![App Screenshot](https://github.com/BikramdeepSingh/TweetItBig/blob/main/media/main_page_2.png?raw=true)

- Apple Analysis
This webpage provides a comprehensive overview of sentiment analysis conducted on keywords related to Apple searches.

![App Screenshot](https://github.com/BikramdeepSingh/TweetItBig/blob/main/media/sen_vs_key.png?raw=true)

- Keyword Search
Upon entering a search keyword in the designated search box, this webpage generates and displays results pertaining to subjectivity scores (ranging from 0 to 1, indicating personal opinions and judgments) and polarity scores (ranging from -1 to 1, where -1 denotes negative sentiment and +1 denotes positive sentiment). These scores are accompanied by corresponding rows of analyzed tweets for comprehensive evaluation and examination.

![App Screenshot](https://github.com/BikramdeepSingh/TweetItBig/blob/main/media/sub_&_pol.png?raw=true)

![App Screenshot](https://github.com/BikramdeepSingh/TweetItBig/blob/main/media/analyzed_tweets.png?raw=true)
## Tech Stack

- [Python](https://www.python.org/) 
- [Taskade](https://www.taskade.com/spaces/U1y6MQruSmAsYwM7) (Team Management Tool)
- [Tableau](https://www.tableau.com/) (Environment)
- [Microsoft Power BI](https://powerbi.microsoft.com/en-ca/) (Environment)
- [Jupyter Notebook](https://jupyter.org/) (Environment)
- [VS Code](https://code.visualstudio.com/) (Environment)
## Insights

- The project began with obtaining the necessary code to initiate web scraping and data retrieval from Twitter, utilizing valid Twitter API keys and access tokens.
- Twitter's rich metadata was leveraged, offering diverse applications given sufficient time and motivation, enabling the development of essential skills for the project.
- Measures were taken to clean the scraped data and extract relevant content for the purpose of creating graphs.
- Tools such as Tableau, Microsoft Power BI, and Jupyter Notebook were employed to generate graphs for data analysis, requiring meticulous exploration of combinations to achieve desired output from the end user's perspective.
- __NLTK Vader__ proved to be a useful modeling strategy compared to TexBlob, as it enabled targeted identification of slang words commonly used on platforms like Twitter.
- The development of a dashboard using _Dash with Plotly_ and associated libraries (e.g., Dash, Plotly Express, Plotly objects) showed promise initially but encountered challenges in determining the correct column combinations for the final graph intended for the user.
- Deploying the project on _PythonAnywhere_ allowed for its execution and provided an online dashboard accessible through a shared link, eliminating the need for a local server.
