from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
from keras.utils import to_categorical
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load the Iris dataset
data = load_iris()
X = data.data
y = data.target

# Preprocess the data
scaler = StandardScaler()
X = scaler.fit_transform(X)
y = to_categorical(y)  # Convert labels to one-hot encoded vectors

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build the neural network model
model = Sequential()
model.add(Dense(10, input_shape=(X.shape[1],), activation='relu'))  # Input layer with 10 neurons and ReLU activation
model.add(Dense(8, activation='relu'))  # Hidden layer with 8 neurons and ReLU activation
model.add(Dense(3, activation='softmax'))  # Output layer with 3 neurons for classification

# Compile the model
model.compile(optimizer=Adam(lr=0.001), loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=50, batch_size=4, validation_data=(X_test, y_test))

# Evaluate the model
loss, accuracy = model.evaluate(X_test, y_test)
print(f"Test accuracy: {accuracy:.4f}")
