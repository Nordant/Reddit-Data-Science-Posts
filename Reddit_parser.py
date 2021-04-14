"""
Code for parsing posts from reddit
"""
import numpy as np
import pandas as pd
from datetime import datetime
import requests


def df_from_response(res):
    '''
    Function for converting responses to dataframe.
    Args:
        res - response.
    '''
    df = pd.DataFrame()

    # loop through each post pulled from res and append to df
    for post in res.json()['data']:
        df = df.append({
            'author': post['author'],
            'author_created_utc': post['author_created_utc'] if 'author_created_utc' in post else np.nan,
            'subreddit': post['subreddit'],
            'full_link': post['full_link'],
            'num_comments': post['num_comments'],
            'num_crossposts': post['num_crossposts'] if 'num_crossposts' in post else np.nan,
            'subreddit_subscribers': post['subreddit_subscribers'] if 'subreddit_subscribers' in post else np.nan,
            'title': post['title'],
            'selftext': post['selftext'] if 'selftext' in post else '',
            'score': post['score'],
            'created_utc': post['created_utc'],
            'id': post['id'] 
        }, ignore_index = True)
    return df


def d_cleaner(data):
    '''
    Function for data cleaning.
    Args:
        a data frame with df_from_response data structure.
    '''
    data['selftext'] = data['selftext'].replace('[removed]', '')
    data['selftext'] = data['selftext'].replace('[deleted]', '')
    data['created_date'] = data['created_utc'].apply(lambda x: datetime.fromtimestamp(x).strftime('%Y-%m-%d %H:%M:%S'))
    data['created_timestamp'] = data['created_utc']
    data = data.drop('created_utc', axis = 1)
    columns = ['created_date', 'created_timestamp', 'subreddit', 'title', 
               'id', 'author', 'author_created_utc', 'full_link', 'selftext', 'score', 'num_comments', 
               'num_crossposts', 'subreddit_subscribers']
    data = data[columns]
    data = data.sort_values('created_date', ascending = True).reset_index(drop = True)
    data['post'] = data['selftext']
    data = data.drop('selftext', axis = 1)
    data = data.drop_duplicates(subset = ['created_date']).reset_index(drop = True)

    return data


def d_parser(subredits_list):
    '''
    The main function for parsing the data from specified subreddits.
    To prevent data loss after any errors 
    (for example, as a result of an unstable Internet), 
    the function online overwrites data in two global data frames - 
    with all data and with subreddit, which is processed for the moment.
    
    Args:
        list of subredits.
        'data' and 'all_data' global data frames (empty) must be created!!!
        Also, this function uses two another custom functions:
            - df_from_response
            - d_cleaner
    '''
    import time
    global all_data
    global data
    
    start = time.time()
    for idx, subr in enumerate(subredits_list):
        point = time.time()
        print('[{}/{}; {} min] Parsing of "{}" ...'.format(idx+1, len(subredits_list), round((point - start)/60, 1), subr))
        data = pd.DataFrame()
        time_start = 0 # Starting time for parsing
        try:
            for i in range(50000):
                res = requests.get('https://api.pushshift.io/reddit/search/submission?subreddit={}&after={}&size=100&sort_type=created_utc&sort=asc'.format(subr, time_start))

                new_df = df_from_response(res) # get dataframe from response
                row = new_df.iloc[len(new_df)-1] # take the final row (oldest entry)
                new_time = row['created_utc'] # create fullname
                time_start = int(new_time) # add/update fullname in params
                data = data.append(new_df, ignore_index = True) # append new_df to data
        except IndexError:
            pass
        data = d_cleaner(data)
        all_data = all_data.append(data, ignore_index = True)
    point = time.time()
    print('Parsing finished! (Runtime: {} min)'.format(round((point - start)/60, 1)))


# List with subreddits
subreddit = ['analytics', 'deeplearning', 'datascience', 'datasets', 'kaggle', 
             'learnmachinelearning', 'MachineLearning', 'statistics', 
             'artificial', 'AskStatistics', 'computerscience',
             'computervision', 'dataanalysis', 'dataengineering', 
             'DataScienceJobs', 'datascienceproject', 'data', 'MLQuestions', 
             'rstats']

# Parse all the data
all_data = pd.DataFrame()
data = pd.DataFrame()

d_parser(subreddit)

# Check the results
all_data
