import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import plotly.express as px

pd.set_option("display.max_columns", 1000)

from fredapi import Fred
fred_key = "981efcd7e9faf439aa70c00d5ae16089"

fred=Fred(api_key=fred_key)


sp_search= fred.search("S&P", order_by="popularity")

sp_search2=fred.get_series("SP500")


plt.plot(sp_search2)
plt.title("S&P500")
plt.show()
#use 3.12.7