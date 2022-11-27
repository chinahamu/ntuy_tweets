import snscrape.modules.twitter as sntwitter
import pandas as pd
import sys

args = sys.argv

# Created a list to append all tweet attributes(data)
attributes_container = []

# Using TwitterSearchScraper to scrape data and append tweets to list
for i,tweet in enumerate(sntwitter.TwitterSearchScraper(f'心身二元論 since:2022-10-01').get_items()):
    attributes_container.append([tweet.url,tweet.date,tweet.rawContent,tweet.id,tweet.user,tweet.replyCount,tweet.retweetCount,tweet.likeCount,tweet.quoteCount,tweet.conversationId,tweet.lang,tweet.source,tweet.sourceUrl,tweet.sourceLabel,tweet.links,tweet.media,tweet.retweetedTweet,tweet.quotedTweet,tweet.inReplyToTweetId,tweet.inReplyToUser,tweet.mentionedUsers,tweet.coordinates,tweet.place,tweet.hashtags,tweet.cashtags,tweet.card])
    
# Creating a dataframe from the tweets list above 
tweets_df = pd.DataFrame(attributes_container, columns=["url","date","rawContent","id","user","replyCount","retweetCount","likeCount","quoteCount","conversationId","lang","source","sourceUrl","sourceLabel","links","media","retweetedTweet","quotedTweet","inReplyToTweetId","inReplyToUser","mentionedUsers","coordinates","place","hashtags","cashtags","card"])

tweets_df.to_csv(f'deka.csv',encoding="utf-8",index = False)