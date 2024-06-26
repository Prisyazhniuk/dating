import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Пример данных о пользователях
data = {
    'user_id': [1, 2, 3, 4, 5],
    'interest_1': [5, 3, 1, 4, 2],
    'interest_2': [3, 2, 5, 1, 4],
    'interest_3': [1, 4, 2, 3, 5],
}

df = pd.DataFrame(data)

# Стандартизация данных
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df.drop('user_id', axis=1))

# Кластеризация с помощью k-means
kmeans = KMeans(n_clusters=3, random_state=42)
df['cluster'] = kmeans.fit_predict(X_scaled)

print(df)
