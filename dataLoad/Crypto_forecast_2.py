import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM, Dropout
import requests

# Number of days to look back for training
days_to_look_back = 45
# Number of days to predict
days_to_predict = 3

def fetch_data(coin_id, days):
    # API request to get historical data
    url = f'https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart?vs_currency=usd&days={days}'
    response = requests.get(url)
    data = response.json()
    prices = data['prices']
    
    # Convert the data to a pandas DataFrame
    df = pd.DataFrame(prices, columns=['timestamp', 'price'])
    df['date'] = pd.to_datetime(df['timestamp'], unit='ms')
    df = df.set_index('date')
    df = df.drop(columns=['timestamp'])
    
    # Check if the data has the required number of days
    if len(df) < days:
        print(f"Warning: Only {len(df)} days of data are available for {coin_id}.")
    return df

# Prepare the data for LSTM model training
def prepare_data(df, days_to_look_back):
    # Scale the data to values between 0 and 1
    sc = MinMaxScaler(feature_range=(0, 1))
    training_set_scaled = sc.fit_transform(df)
    
    # Split the data into input and output sequences for training
    X_train = []
    y_train = []
    for i in range(days_to_look_back, len(training_set_scaled)):
        X_train.append(training_set_scaled[i-days_to_look_back:i, 0])
        y_train.append(training_set_scaled[i, 0])
    X_train, y_train = np.array(X_train), np.array(y_train)
    
    # Reshape the input data to 3D for LSTM model
    X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1], 1))
    return X_train, y_train, sc

# Create and compile the LSTM model
def create_lstm_model(input_shape):
    model = Sequential()
    model.add(LSTM(units=50, return_sequences=True, input_shape=input_shape))
    model.add(Dropout(0.2))
    model.add(LSTM(units=50, return_sequences=True))
    model.add(Dropout(0.2))
    model.add(LSTM(units=50, return_sequences=True))
    model.add(Dropout(0.2))
    model.add(LSTM(units=50))
    model.add(Dropout(0.2))
    model.add(Dense(units=1))
    model.compile(optimizer='adam', loss='mean_squared_error')
    return model

# Predict prices for the next days_to_predict days
def predict_prices(df, model, sc, days_to_look_back, days_to_predict):
    predicted_prices = []
    for _ in range(days_to_predict):
        # Get the last days_to_look_back days of data and scale it
        last_n_days = df[-days_to_look_back:].values
        last_n_days_scaled = sc.transform(last_n_days)
        
        # Prepare the input data and predict the price
        X_test = np.reshape(last_n_days_scaled, (1, days_to_look_back, 1))
        predicted_price = model.predict(X_test)
        predicted_price = sc.inverse_transform(predicted_price)
        
        # Append the predicted price to the list and DataFrame
        predicted_prices.append(predicted_price[0][0])
        df = df.append(pd.DataFrame({'price': predicted_price[0]}, index=[pd.Timestamp.now()]), ignore_index=False)
    return predicted_prices

# Define the coins to analyze
coins = {
    #'BTC': 'bitcoin',
    #'ETH': 'ethereum',
    #'DOT': 'polkadot',
    'CWEB': 'coinweb'  # Replace with the correct coin ID if needed
}

# Loop through the coins and process each one
for symbol, coin_id in coins.items():
    print(f'Processing {symbol}...')
    
    # Fetch historical price data
    df = fetch_data(coin_id, days_to_look_back)
    
    # Prepare the data for LSTM model training
    X_train, y_train, sc = prepare_data(df, days_to_look_back)
    
    # Create and compile the LSTM model
    model = create_lstm_model((days_to_look_back, 1))
    
    # Train the LSTM model
    model.fit(X_train, y_train, epochs=100, batch_size=32)
    
    # Predict prices for the next days_to_predict days
    predicted_prices = predict_prices(df, model, sc, days_to_look_back, days_to_predict)

    # Print the predicted prices
    print(f"Predicted {symbol} prices for the next week:")
    for i, price in enumerate(predicted_prices):
        print(f"Day {i+1}: {price}")

    # Plot the historical and predicted prices
    plt.figure(figsize=(10, 5))
    plt.plot(df.index[:-days_to_predict], df['price'][:-days_to_predict], label=f'{symbol} Historical Price Data')
    plt.plot(df.index[-days_to_predict:], predicted_prices, label=f'{symbol} Predicted Price Data', linestyle='--')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title(f'{symbol} Price Prediction Using LSTM')
    plt.legend()
    plt.show()

