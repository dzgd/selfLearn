import numpy
import pandas as pd
test = pd.read_excel('C:/Users/Administrator/Desktop/url.xlsx')
# x1=test[:5000]
# x2=test[5000:10000]
# x3=test[10000:15000]
# x4=test[15000:20000]
# x5=test[20000:25000]
# x6=test[25000:30000]
# x7=test[30000:35000]
# x8=test[35000:40000]
# x9=test[40000:45000]
# x10=test[45000:50000]
# x11=test[50000:55000]
# x12=test[55000:60000]
# x13=test[60000:]
for i in range(12):
    y = test[i*5000:(i+1)*5000]
    y.to_excel("C:/Users/Administrator/Desktop/"+str(i)+".xlsx")







