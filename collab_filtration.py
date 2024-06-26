from surprise import Dataset, Reader
from surprise import SVD
from surprise.model_selection import train_test_split
from surprise import accuracy

# Пример данных о рейтингах
ratings_dict = {
    "item": [1, 1, 1, 2, 2],
    "user": [9, 32, 2, 45, 27],
    "rating": [3, 2, 4, 3, 5],
}

df = pd.DataFrame(ratings_dict)

reader = Reader(rating_scale=(1, 5))
data = Dataset.load_from_df(df[['user', 'item', 'rating']], reader)

# Разделение данных на обучающую и тестовую выборки
trainset, testset = train_test_split(data, test_size=0.25)

# Обучение модели SVD
algo = SVD()
algo.fit(trainset)

# Предсказание и оценка точности
predictions = algo.test(testset)
accuracy.rmse(predictions)
