import pandas as pd

df = pd.read_json('nyt2.json', lines=True)



# print(df.groupby(['author']).size())
# print(df[(df.author == 'Debbie Macomber') & (df.title == 'A CEDAR COVE CHRISTMAS')])
# print(len(df[(df.author == 'Debbie Macomber') & (df.title == 'A CEDAR COVE CHRISTMAS')][['title', 'author', 'publisher']]))
# print(df[(df.author == 'Debbie Macomber') & (df.title == 'A CEDAR COVE CHRISTMAS')][['title', 'author', 'publisher']])
# print(df['title'].count())
# print(df.count())
# print(df[df.author == 'Debbie Macomber'].title.unique())
# print(df['author'].tail(5))
# print(df[['author', 'title']].tail(5))
# print(df['author'].head(5))
# print(df[['author', 'title']].head(5))
# print(df)
# print(df.shape)
# print(df.columns.to_list())
# print("The total length: ",len(df.columns.to_list()))

