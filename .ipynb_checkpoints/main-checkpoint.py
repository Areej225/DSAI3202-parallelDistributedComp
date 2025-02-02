data = load_data()
X_train, X_test, y_train, y_test = split_data(data)
model = train_model(X_train, y_train)
report = evaluate_model(model, X_test, y_test)
print(report)
