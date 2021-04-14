# Reddit Data Science Posts

![](http://ipic.su/img/img7/fs/reddit_cover_1616656218.png)

## [Dataset on Kaggle](https://www.kaggle.com/maksymshkliarevskyi/reddit-data-science-posts)

Data Science Community on Reddit is growing every year. Today, the network is a platform for many professionals and enthusiasts who share valuable materials and experiences. Quite an interesting task is the analysis of posts dedicated to Data Science: 
- **finding interesting topics**, 
- **studying changes in trends over time**, 
- **predicting the potential popularity of posts on Reddit by its title and text**, etc.

Over time, I will increase the size of this dataset by adding posts from other subreddits, so that the quality of the analysis and modeling will improve.

Feel free to leave your comments on this dataset and [starter notebook](https://www.kaggle.com/maksymshkliarevskyi/how-is-data-science-on-reddit). I will try to make the dataset better and much larger. The current goal is 750k + posts (spoiler: after that, there will be a million!)

### **This dataset includes over 500,000 posts from 19 Date Science subreddits:**
[r/analytics](https://www.reddit.com/r/analytics/), [r/deeplearning](https://www.reddit.com/r/deeplearning/), [r/datascience](https://www.reddit.com/r/datascience/), [r/datasets](https://www.reddit.com/r/datasets/), [r/kaggle](https://www.reddit.com/r/kaggle/), [r/learnmachinelearning](https://www.reddit.com/r/learnmachinelearning/), [r/MachineLearning](https://www.reddit.com/r/MachineLearning/), [r/statistics](https://www.reddit.com/r/statistics/), [r/artificial](https://www.reddit.com/r/artificial/), [r/AskStatistics](https://www.reddit.com/r/AskStatistics/), [r/computerscience](https://www.reddit.com/r/computerscience/), [r/computervision](https://www.reddit.com/r/computervision/), [r/dataanalysis](https://www.reddit.com/r/dataanalysis/), [r/dataengineering](https://www.reddit.com/r/dataengineering/), [r/DataScienceJobs](https://www.reddit.com/r/DataScienceJobs/), [r/datascienceproject](https://www.reddit.com/r/datascienceproject/), [r/data](https://www.reddit.com/r/data/), [r/MLQuestions](https://www.reddit.com/r/MLQuestions/), [r/rstats](https://www.reddit.com/r/rstats/)

Data were collected from [pushshift.io API](https://pushshift.io) (maintained by Jason Baumgartner).

If you know of any interesting Data Science subreddits, please, let me know in discussions.

### **You can find the code for parsing subreddits in the `Reddit_parser.py` script.**

## **19 datasets (one per one subreddit) include the following data:**

| column | description |
| --- | --- |
| `#` | row index |
| `created_date` | post publication date |
| `created_timestamp` | post publication timestamp |
| `subreddit` | subreddit name |
| `title` | post title |
| `id` | unique operation id |
| `author` | post author |
| `author_created_utc` | author registration date |
| `full_link` | hyperlink to post |
| `score` | ratio of likes and dislikes |
| `num_comments` | the number of comments |
| `num_crossposts` | the number of crossposts |
| `subreddit_subscribers` | the number of subreddit subscribers at the time the post was published |
| `post` | post text |
