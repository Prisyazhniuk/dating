from surprise import Dataset, Reader
from surprise import SVD
from surprise.model_selection import train_test_split
from surprise import accuracy

def train_collaborative_filtering(ratings_data):
    reader = Reader(rating_scale=(1, 5))
    data = Dataset.load_from_df(ratings_data[['user', 'item', 'rating']], reader)

    trainset, testset = train_test_split(data, test_size=0.25)

    algo = SVD()
    algo.fit(trainset)

    predictions = algo.test(testset)
    accuracy.rmse(predictions)
    
    return algo
