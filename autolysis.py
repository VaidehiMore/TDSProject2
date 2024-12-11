# -*- coding: utf-8 -*-
"""Project 2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/12QnPU3rk7IRh1NwMbeuj-D6k41mGozQw

#### Please upload your datasets before running the cells

### Q1: How many books do not have an original title [books.csv] ? (N)
"""

import pandas as pd
import numpy as np
books = pd.read_csv("books.csv")
books["original_title"].isna().sum()

"""### Q2: How many unique books are present in the dataset ? Evaluate based on the 'book_id'? [books.csv] (N)"""

import pandas as pd
books = pd.read_csv("books.csv")
books["book_id"].nunique()

"""### Q3: How many unique books are present in the dataset [books.csv]? (N)"""

import pandas as pd
ratings = pd.read_csv("books.csv")
ratings["book_id"].nunique()

"""### Q4: Which book (title) has the maximum number of ratings based on (work_ratings_count) [books.csv] ? (S)"""

import pandas as pd
books = pd.read_csv("books.csv")
books.loc[books["work_ratings_count"].idxmax()]["title"]

"""### Q5: Which (tag_id) is the most frequently used ie. mapped with the highest number of books [books.csv]? (In case of more than one tag, mention the tag id with the least numerical value) (N)"""

import pandas as pd
book_tags = pd.read_csv("books.csv")
value_counts = book_tags['best_book_id'].value_counts()
max_count = value_counts.max()
value_counts[value_counts == max_count].index.min()

"""### Q6: Which book (title) has the most number of counts of tags given by the user ie. the book with maximum user records including all tags [book_tags.csv,books.csv] ? (S)"""

import pandas as pd
books = pd.read_csv("books.csv")

value_counts = book_tags.groupby("goodreads_book_id")["book_id"].sum()
books[books["goodreads_book_id"] == value_counts.idxmax()]["title"].values[0]

"""### Q7: Which book (goodreads_book_id) is marked as to-read by most users [books.csv,toread.csv] ? (N)"""

import pandas as pd
books = pd.read_csv("books.csv")

value_counts = books.groupby("book_id")["title"].nunique()
books[books["book_id"] == value_counts.idxmax()]["title"].values[0]

"""### Q8: Which is the least used tag, i.e. mapped with the lowest number of books [book_tags.csv]? (In case of more than one tag, mention the tag id with the least numerical value) (N)"""

import pandas as pd
books = pd.read_csv("books.csv")
value_counts = book_tags["book_id"].value_counts()
min_count = value_counts.min()
value_counts[value_counts == min_count].index.min()

"""### Q9: Which book (title) has the minimum (average_rating) [books.csv], if more than 1 book have same average rating, sort the books by ['title'] in alphabetical order and use the first book in the sorted list? (S)"""

import pandas as pd
books = pd.read_csv("books.csv")
min_avg_rating = books["average_rating"].min()
books[books["average_rating"] == min_avg_rating]["title"].sort_values(ascending=True).values[0]

"""### Q10: Which book (goodreads_book_id) has the least number of count of tags given by the user ie. the book with minimum user records including all tags [book_tags.csv] ? (N)"""

import pandas as pd
book_tags = pd.read_csv("books.csv")
value_counts = book_tags.groupby("goodreads_book_id")["title"].sum()
value_counts[value_counts == value_counts.min()].index[0]

"""### Q11: How many unique tags are there in the dataset [books.csv] ? (N)"""

import pandas as pd
books = pd.read_csv("books.csv")
book_tags["book_id"].nunique()

"""### Q12: What is the mean value of rating of all the books in the dataset based on (average_rating) [books.csv] ? (F)"""

import pandas as pd
books = pd.read_csv("books.csv")
f"{books['average_rating'].mean():.2f}"

"""### Q14: Predict sentiment using Textblob. How many positive titles (original_title) are there [books.csv] ? (cut-off >=0) N"""

from textblob import TextBlob
import pandas as pd
import numpy as np
books = pd.read_csv("books.csv")
books_cleaned = books.dropna(subset=["original_title"])
original_titles = books_cleaned["original_title"].values
[TextBlob(title).sentiment.polarity >= 0 for title in original_titles].count(True)

"""### Export"""

import pandas as pd
### Edit this to include your questions and answers in order
answers = {"Q4":"The Hunger Games (The Hunger Games, #1)",
           "Q12":4.05,
           "Q6":"Harry Potter and the Sorcerer's Stone (Harry Potter, #1)",
           "Q10":3334563,
           "Q8":24,
           "Q11":6084,
           "Q1":51,
           "Q7":5470,
           "Q2":1620,
           "Q14":1426}

### Download the answers.csv
pd.DataFrame.from_dict(answers,orient='index').to_csv("answers.csv", header=False, encoding='utf-8')

"""#### PS: Wrapping up this final Project! It's been great learning with everyone. Thank You!!

Let's keep in touch: [LinkedIn](https://in.linkedin.com/in/sm-arif-ali-17386821b)
"""