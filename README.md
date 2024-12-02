# delete-tweets
This script delete tweets from X since a year determined by the user.

Be sure to install Tweepy if you don't have it. In the terminal, run: 
´pip install tweepy´ 

Date filter:

I added a deadline (DELETE_BEFORE_DATE) with the value datetime(2019, 1, 1).
The creation date of each tweet (tweet.created_at) is compared with this cut-off date.
Only tweets created before this date are deleted.

Clear console messages:

The script prints whether a tweet is deleted or kept, with its ID and date.

Important notes:

- API limits: If you have many tweets, the process may be delayed due to API limits (maximum 3200 tweets accessible).
- Date validation: The API returns tweet dates in UTC, so you don't need to convert them.
- Archived tweets: If you have older tweets that do not appear in the API, you will need to upload a data file exported from Twitter.
