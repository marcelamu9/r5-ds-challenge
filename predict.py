from sklearn.pipeline import Pipeline as skPipeline
from imblearn.pipeline import Pipeline as imbPipeline
import pickle


def predict_model(path_model: str, data):

    with open(f"{path_model}/model.pickle", "rb") as file:
        model = pickle.load(file)

    predict_proba = model.predict_proba(data)

    model_pipe = imbPipeline(steps=[
        ('predict_proba', predict_proba),
    ]
    )
    return model_pipe
