import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plot

df= {'company_name':['HDFC','TCS','ICICI','INFOSYS','RI'],
     'stock_price':[1500,2000,1256,1534,1984],
     'total_company':[1,2,3,4,5],
     
     }

stock_maret = pd.DataFrame(df)
print(stock_maret)

total_company_name = df['company_name']
total_stocke_price =df['stock_price']
company_list = df['total_company']


print ("company name:",total_company_name)
print("stock price:",total_stocke_price)
print("list:",company_list)

sb.histplot(df['company_name'],kde=True)
plot.xlabel("company_name",color='blue')
plot.ylabel('company_name')
plot.title("stock market chart")
plot.show()