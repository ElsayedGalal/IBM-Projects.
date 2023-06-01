#!/usr/bin/env python
# coding: utf-8

# # Extracting and Visualizing Stock Data
# 
# Description
# 
# Extracting essential data from a dataset and displaying it is a necessary part of data science; therefore individuals can make correct decisions based on the data. In this assignment, you will extract some stock data, you will then display this data in a graph.

# In[62]:


get_ipython().system('pip install yfinance')
#!pip install pandas
#!pip install requests
get_ipython().system('pip install bs4')
#!pip install plotly


# # Importing Libraries:

# In[63]:


import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from plotly.subplots import make_subplots


# # Define Graphing Function
# 

# In[64]:


def make_graph(stock_data, revenue_data, stock):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Historical Share Price", "Historical Revenue"), vertical_spacing = .3)
    fig.add_trace(go.Scatter(x=pd.to_datetime(stock_data.Date, infer_datetime_format=True), y=stock_data.Close.astype("float"), name="Share Price"), row=1, col=1)
    fig.add_trace(go.Scatter(x=pd.to_datetime(revenue_data.Date, infer_datetime_format=True), y=revenue_data.Revenue.astype("float"), name="Revenue"), row=2, col=1)
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
    fig.update_layout(showlegend=False,
    height=900,
    title=stock,
    xaxis_rangeslider_visible=True)
    fig.show()


# # Question 1: Use yfinance to Extract Stock Data
# 
# 
# 

# In[65]:


tesla = yf.Ticker('TSLA')


# In[66]:


tesla_data = tesla.history(period="max")


# In[67]:


tesla_data.reset_index(inplace=True)
tesla_data.head()


# # Question 2: Use Webscraping to Extract Tesla Revenue Data

# In[68]:


url = 'https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue'
html_data = requests.get(url).text


# In[69]:


soup = BeautifulSoup(html_data,"html5lib")


# In[87]:


tesla_revenue = tesla_revenue.rename(columns={"Tesla Quarterly Revenue(Millions of US $)":"Date","Tesla Quarterly Revenue(Millions of US $).1":"Revenue"}) #Rename df columns to 'Date' and 'Revenue'
tesla_revenue.head() 


# In[72]:


tesla_revenue


# In[73]:


tesla_revenue = tesla_revenue[tesla_revenue['Revenue'].astype(bool)]


# In[74]:


tesla_revenue.tail()


# # Question 3: Use yfinance to Extract Stock Data

# In[75]:


gme = yf.Ticker('GME')


# In[76]:


gme_data = gme.history(period='max')


# In[77]:


gme_data.reset_index(inplace=True)
gme_data.head()


# # Question 4: Use Webscraping to Extract GME Revenue Data

# In[78]:


url = 'https://www.macrotrends.net/stocks/charts/GME/gamestop/revenue'
html_data = requests.get(url).text


# In[83]:


soup = BeautifulSoup(html_data,"html5lib")
soup.find_all('title')


# In[88]:


gme_revenue = gme_revenue.rename(columns={"GameStop Quarterly Revenue(Millions of US $)":"Date","GameStop Quarterly Revenue(Millions of US $).1":"Revenue"}) 
gme_revenue.head() 


# In[89]:


gme_revenue.tail()


# # Question 5: Plot Tesla Stock Graph

# In[90]:


make_graph(tesla_data[['Date','Close']], tesla_revenue, 'Tesla')


# # Question 6: Plot GameStop Stock Graph

# In[46]:


make_graph(gme_data[['Date','Close']], gme_revenue, 'GameStop')


# In[47]:


print("Completed")


# In[ ]:




