from sklearn import datasets
boston = datasets.load_boston()
X, y = shuffle_data(boston.data, boston.target, seed=13)
X = X.astype(np.float32)
offset = int(X.shape[0] * 0.9)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
print(X_train.shape, y_train.shape, X_test.shape, y_test.shape)

model = GBDTRegressor()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
# Color map
cmap = plt.get_cmap('viridis')
mse = mean_squared_error(y_test, y_pred)
print ("Mean Squared Error:", mse)

# Plot the results
m1 = plt.scatter(range(X_test.shape[0]), y_test, color=cmap(0.5), s=10)
m2 = plt.scatter(range(X_test.shape[0]), y_pred, color='black', s=10)
plt.suptitle("Regression Tree")
plt.title("MSE: %.2f" % mse, fontsize=10)
plt.xlabel('sample')
plt.ylabel('house price')
plt.legend((m1, m2), ("Test data", "Prediction"), loc='lower right')
plt.show();