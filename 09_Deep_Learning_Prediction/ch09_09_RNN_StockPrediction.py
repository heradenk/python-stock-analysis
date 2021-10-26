import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, LSTM, Dropout
import numpy as np
import matplotlib.pyplot as plt
from Investar import Analyzer

mk = Analyzer.MarketDB()
raw_df = mk.get_daily_price('삼성전자', '2019-08-06', '2021-08-06')

def MinMaxScaler(data):  # 1
    """최솟값과 최댓값을 이용하여 0 ~ 1 값으로 변환"""
    numerator = data - np.min(data, 0)
    denominator = np.max(data, 0) - np.min(data, 0)
    return numerator / (denominator + 1e-7) # 2

dfx =  raw_df[['open', 'high', 'low', 'volume', 'close']]
dfx = MinMaxScaler(dfx) # 3
dfy = dfx[['close']]

x = dfx.values.tolist()
y = dfy.values.tolist()


data_x = []
data_y = []
window_size = 10
for i in range(len(y) - window_size):
    _x = x[i: i + window_size] # 다음 날 종가(i+window_size)는 포함되지 않음
    _y = y[i + window_size]    # 다음 날 종가
    data_x.append(_x)
    data_y.append(_y)
print(_x, "->", _y)

# 훈련용 데이터셋
train_size = int(len(data_y) * 0.7)
train_x = np.array(data_x[0:train_size])
train_y = np.array(data_y[0:train_size])

# 테스트용 데이터셋
test_size = len(data_y) - train_size
test_x = np.array(data_x[train_size:len(data_x)])
test_y = np.array(data_y[train_size:len(data_y)])

model = Sequential() # 1
model.add(LSTM(units=10, activation='relu', return_sequences=True, input_shape=(window_size, 5))) # 2
model.add(Dropout(0.1)) # 3
model.add(LSTM(units=10, activation='relu'))
model.add(Dropout(0.1))
model.add(Dense(units=1)) # 4
model.summary()

model.compile(optimizer='adam', loss='mean_squared_error') # 5
model.fit(train_x, train_y, epochs=60, batch_size=30) # 6
pred_y = model.predict(test_x) # 7


plt.figure()
plt.plot(test_y, color='red', label='real SEC stock price')
plt.plot(pred_y, color='blue', label='predicted SEC stock price')
plt.title('SEC stock price prediction')
plt.xlabel('time')
plt.ylabel('stock price')
plt.legend()
plt.show()



