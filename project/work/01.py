'''
###多元统计分析第四章119页数据代码调试
####10折交叉验证
import numpy as np
import pandas as pd
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.metrics import confusion_matrix
def Fold(y,X,Z,seed=8888):
    id0=np.arange(len(y))
    part=[]
    for i in np.unique(y):
        part.append(id0[y==i]) #part is index of y=i
    Zid=[];Xn=[];yn=[]
    np.random.seed(seed)
    for k in part:
        np.random.shuffle(k)#for each y=i shuffle index
        yn.extend(y[k])
        Xn.extend(X[k])
        Zid.extend((list(range(Z))*int(len(k)/Z+1))[:len(k)])
    return Zid, yn, Xn
v= pd.read_csv('F:\\pendigits.csv',index_col=False)
X=np.array(v[v.columns[:16]])#自变量
y=np.array(v[v.columns[16]])#因变量
Zid, yn, Xn=Fold(y=y,X=X,Z=10,seed=1010)
yn=np.array(yn)
Xn=np.array(Xn)
def CCV(clf,Zid, Xn, yn):
    y_pred=[];yN=[]
    for j in np.unique(Zid): #j has Z kinds of values
        clf.fit(Xn[Zid!=j],yn[Zid!=j])
        yN.extend(yn[Zid==j])
        y_pred.extend(clf.predict(Xn[Zid==j]))
    y_pred=np.array(y_pred)
    yN=np.array(yN)
    error=np.sum(yN!=y_pred)/len(y)
    cmatrix=confusion_matrix(yN,y_pred)
    return(error,cmatrix)
lda=LinearDiscriminantAnalysis()
lda.fit(X,y)
y_pred=lda.predict(X)
y_score=lda.score(X,y)
print (confusion_matrix(y,y_pred))
print ('Misclassification rate=', 1-y_score)
lda=LinearDiscriminantAnalysis()
er,cm=CCV(lda,Zid, Xn, yn)
print("Error rate=",er)
print(cm)
####二次判别不做交叉验证
qda=QuadraticDiscriminantAnalysis()
qda.fit(X,y)
y_pred2=qda.predict(X)
y_score2=qda.score(X,y)
print( confusion_matrix(y,y_pred2))
print( 'Misclassification rate=', 1-y_score2)

####二次判别做交叉验证
qda=QuadraticDiscriminantAnalysis()
er,cm=CCV(qda,Zid, Xn, yn)
print("Error rate=",er)
print (cm)

####对数字笔迹识别数据做5个机器学习分类的交叉验证
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import scipy.stats as stats
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_moons, make_circles, make_classification
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
names = ["Nearest Neighbors", "Linear SVM", "Decision Tree",\
       "Random Forest", "Naive Bayes"]
classifiers = [
    KNeighborsClassifier(3),
    SVC(kernel="linear", C=0.025),
    DecisionTreeClassifier(max_depth=5),
    RandomForestClassifier(n_estimators=500),
    GaussianNB()]
####计算
A=list()
for clf in classifiers:
    np.random.seed(1010)
    er,cm=CCV(clf,Zid, Xn, yn)
    A.append(er)
print(A)
####打印5个误判率条形图
plt.bar(range(len(A)),A,)
plt.ylabel('Error rate')
plt.title('Error rate')
plt.xticks(np.arange(len(names)),names,rotation=90)
plt.show()
'''




#####********************************************************
##Logistic回归对献血数据的拟合

import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import roc_curve, auc, confusion_matrix
w = pd.read_csv('F:\\Trans.csv')
w['intercept'] = 1.0 #加上截距
X_cols=w.columns[[4,0,1,2]];y_col=w.columns[3]
X=w[X_cols];y=w[y_col]
X=np.array(X);y=np.array(y)
Zid=np.ones(len(y));Zid[:int(len(y)*0.20)]=0
X_train=X[Zid==1,:];y_train=y[Zid==1]
X_test=X[Zid==0,:];y_test=y[Zid==0]
'''####做logistic回归
result = sm.Logit(y_train, X_train).fit()
print(result.summary())

####对献血数据进行logistic回归的ROC曲线拟合
y_pred= result.predict(X_test)
fpr, tpr, thresholds =roc_curve(y_test, y_pred)
roc_auc = auc(fpr, tpr)
print("Area under the ROC curve: %f" % roc_auc)

#最优的阈值
thresholds[np.argmin(np.abs(tpr-(1-fpr)))]
print(confusion_matrix(y_test, 1*(y_pred>0.3421)))
print(np.sum(y_test!=1*(y_pred>0.3421))/len(y_test))

#####绘制图像进行可视化
i = np.arange(len(tpr)) # index for df
roc = pd.DataFrame({'fpr' : pd.Series(fpr, index=i),
                    'tpr' : pd.Series(tpr, index = i),
                    '1-fpr' : pd.Series(1-fpr, index = i),
                    'tf' : pd.Series(tpr - (1-fpr), index = i),
                    'thresholds' : pd.Series(thresholds, index = i)})
roc.index[(roc.tf-0).abs().argsort()[:1]]
fig, ax = plt.subplots(figsize=(10,4.4))
plt.plot(roc['fpr'],roc['tpr'])
plt.plot(roc['1-fpr'],roc['tpr'])
plt.xlabel('FPR or 1-FPR')
plt.ylabel('TPR')
plt.title('Receiver operating characteristic')
ax.set_xticklabels([])
#plt.show()'''


######对献血数据进行10折交叉验证
import pandas as pd
import numpy as np
from sklearn.metrics import roc_curve, auc, confusion_matrix
def Fold(y,X,Z,seed=8888):
    id0=np.arange(len(y))
    part=[]
    for i in np.unique(y):
        part.append(id0[y==i]) #part is index of y=i
    Zid=[];Xn=[];yn=[]
    np.random.seed(seed)
    for k in part:
        np.random.shuffle(k)#for each y=i shuffle index
        yn.extend(y[k])
        Xn.extend(X[k])
        Zid.extend((list(range(Z))*int(len(k)/Z+1))[:len(k)])
    return Zid, yn, Xn

def CCV(clf,Zid, Xn, yn):
    y_pred=[];yN=[]
    for j in np.unique(Zid): #j has Z kinds of values
        clf.fit(Xn[Zid!=j],yn[Zid!=j])
        yN.extend(yn[Zid==j])
        y_pred.extend(clf.predict(Xn[Zid==j]))
    y_pred=np.array(y_pred)
    yN=np.array(yN)
    error=np.sum(yN!=y_pred)/len(y)
    cmatrix=confusion_matrix(yN,y_pred)
    return(error,cmatrix)
Zid, yn,Xn=Fold(y=y,X=X,Z=10,seed=1010)
yn=np.array(yn)
Xn=np.array(Xn)
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.linear_model import LogisticRegression
names = ["Linear Discriminant Analysis","Quadratic Discriminant Analysis","Logistic Regression"]
classifiers = [LinearDiscriminantAnalysis(),QuadraticDiscriminantAnalysis(),LogisticRegression()]
A=list()
###########忽略警告
import warnings
warnings.filterwarnings("ignore")
###下面混淆矩阵出现严重的相关性
for clf in classifiers:
    np.random.seed(1010)
    er,cm=CCV(clf,Zid, Xn, yn)
    A.append(er)
print(A)
from sklearn.ensemble import RandomForestClassifier
RF=RandomForestClassifier(n_estimators=500)
np.random.seed(1010)
er,cm=CCV(RF,Zid, Xn, yn)
print("Error rate=",er)
print(cm)



