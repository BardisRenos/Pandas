# Pandas

<p align="center"> 
<img src="https://github.com/BardisRenos/Pandas/blob/master/pandas.png" width="350" height="200" style=centerme>
</p>

In computer programming, pandas is a software library written for the Python programming language for data manipulation and analysis. In particular, it offers data structures and operations for manipulating numerical tables and time series.

Pandas is mainly used for machine learning in form of dataframes. Pandas allow importing data of various file formats such as csv, excel etc. Pandas allows various data manipulation operations such as groupby, join, merge, melt, concatenation as well as data cleaning features such as filling, replacing or imputing null values.


### 1.0 
As a first step is to load the json file from. Pandas library has a build in method that retrieve json files.

```python
  import pandas as pd

  df = pd.read_json('path/to/file/name.json', lines=True)
```

The below commands shows 

```python
  print(df.columns.to_list())
  
  print(len(df.columns.to_list()))
```

``
['_id', 'amazon_product_url', 'author', 'bestsellers_date', 'description', 'price', 'published_date', 'publisher', 'rank', 'rank_last_week', 'title', 'weeks_on_list']

The total length:  12
``
