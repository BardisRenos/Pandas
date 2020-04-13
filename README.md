# Pandas

<p align="center"> 
<img src="https://github.com/BardisRenos/Pandas/blob/master/pandas.png" width="350" height="200" style=centerme>
</p>

In computer programming, [pandas](https://en.wikipedia.org/wiki/Pandas_(software)) is a software library written for the Python programming language for data manipulation and analysis. In particular, it offers data structures and operations for manipulating numerical tables and time series.

Pandas is mainly used for machine learning in form of dataframes. Pandas allow importing data of various file formats such as csv, excel etc. Pandas allows various data manipulation operations such as groupby, join, merge, melt, concatenation as well as data cleaning features such as filling, replacing or imputing null values.


### 1.0 Import the json file
As a first step is to load the json file from. Pandas library has a build in method that retrieve json files.

```python
  import pandas as pd

  df = pd.read_json('path/to/file/name.json', lines=True)
```

The below commands shows the names of the columns as a list. Also, the second command the total length of the dataframe attributes.

```python
  print(df.columns.to_list())
  
  print(len(df.columns.to_list()))
```

After execution, the column names and also the total number.
``
['_id', 'amazon_product_url', 'author', 'bestsellers_date', 'description', 'price', 'published_date', 'publisher', 'rank', 'rank_last_week', 'title', 'weeks_on_list']

The total length:  12

``

### 1.1 Print the shape of the pandas dataframe (number of rows and columns)

```python
  print(df.shape)
```

That tuple means the first number is the number of rows and the second is the numnber of columns
  
``
  (10195, 12)
``

### 1.2 How to print the overall size structure of the data off each column.

It is possible to show the number of non-null/NaN values. using the ***.count()*** command.

```python
  print(df.count())
```

``
| column name | size |
|-------------|------|
|_id|             10195|
|amazon_product_url|    10195|
|author|                10195|
|bestsellers_date|      10195|
|description|           10195|
|price|                 10195|
|published_date|        10195|
|publisher|             10195|
|rank|                  10195|
|rank_last_week|        10195|
|title|                 10195|
|weeks_on_list|         10195|

``
Also it is possible to use the column name.

```python
  print(df['title'].count())
```
Prints just the number of the column size.
``
10195
``

### 1.3 Print single column, multiple columns or all pandas dataframe.

```python
# All dataframe is printed 
  print(df)

# Print only one column and the first 5 rows
  print(df['author'].head(5))
  
# Prnit 2 columns and the first 5 rows
  print(df[['author', 'title']].head(5))
#   
```

### 1.4 Print the last rows of the pandas dataframe.

In order to print only the last part of the dataframe. Can use the command tail(n), where the ***n*** is the number of rows.

```python
# Prints the column author and the last 5 rows
  print(df['author'].tail(5))

# Prints the columns author and title of the last 5 rows
  print(df[['author', 'title']].tail(5))

```
### 1.5 ***Select*** statement

If you want to show all columns and rows
  
  ```python
    print(df)
  ```
  This pandas command can be represented in sql command.
  
  ```sql
  select * from database.table
  ```

### 1.6 ***Where*** statement

The where statements in pandas.

```python
  # This command 
  print(df[df.author == 'Debbie Macomber'].title)
```
It can be represents in sql statement.

```sql
  select title from database.table where author = 'Debbie Macomber'
```

### 1.7 ***Distinct*** 
The distinct statement in pandas is adding the unique() command.

```python
  print(df[df.author == 'Debbie Macomber'].title.unique())
```
In a sql statement.

```sql
  select distinct title from database.table where author = 'Debbie Macomber'
```

### 1.8 ***Select*** with multiple conditions

If is need to apply multiple conditions, can be apply by adding ***&***.

```python
  print(df[(df.author == 'Debbie Macomber') & (df.title == 'A CEDAR COVE CHRISTMAS')])
```

```python 
  print(df[(df.author == 'Debbie Macomber') & (df.title == 'A CEDAR COVE CHRISTMAS')][['title', 'author', 'publisher']])
```

```python
  print(len(df[(df.author == 'Debbie Macomber') & (df.title == 'A CEDAR COVE CHRISTMAS')][['title', 'author', 'publisher']]))
```

The translation into sql statement.

```sql
  
  select * from database.table where author = 'Debbie Macomber' and title = 'A CEDAR COVE CHRISTMAS'
  
  select title, author, publisher from database.table where author = 'Debbie Macomber' and title = 'A CEDAR COVE CHRISTMAS'
  
  select count(*) from database.table where author = 'Debbie Macomber' and title = 'A CEDAR COVE CHRISTMAS'

```

### 1.9 Group by

To group the dataframe by column name. 

```python
  print(df.groupby(['author']).size())
  
```

| author | size |
|--------|------|
|AJ Finn        |                               23
|AN Roquelaure  |                                1
|Aaron Allston  |                               10
|Abraham Verghese|                               1
|Ace Atkins |                                   13
|Adam Johnson |                                  2
|Adriana Trigiani |                             24







