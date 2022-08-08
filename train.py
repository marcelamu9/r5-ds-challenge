# from sklearn.linear_model import LogisticRegression
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.svm import SVC
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.naive_bayes import GaussianNB
# from sklearn import model_selection
# from sklearn.utils import class_weight
# from sklearn.metrics import classification_report
# from sklearn.metrics import confusion_matrix
# importing required libraries
from typing import Any
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from sklearn.pipeline import Pipeline as skPipeline
from imblearn.pipeline import Pipeline as imbPipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from imblearn.over_sampling import SMOTE
import pickle


def model_train(df: pd.DataFrame):

    # obtener los valores nulos para reemplzarlos luego
    df.replace({'none': np.NaN}, inplace=True)
    df['age'] = df['age'].replace({0: np.NaN})
    df[['dayofweekclaimed', 'monthclaimed']] = df[[
        'dayofweekclaimed', 'monthclaimed']].replace({'0': np.NaN})

    # cambiar tipos de variables
    df[['fraudfound_p', 'repnumber', 'yearr', 'driverrating', 'deductible']] = df[['fraudfound_p', 'repnumber',
                                                                                  'yearr', 'driverrating', 'deductible']].astype(str)

    # eliminar columnas
 #   df.drop(['policynumber', 'repnumber', 'numberofsuppliments', 'addresschange_claim', 'policereportfiled',
  #          'witnesspresent', 'agenttype'], axis=1, inplace=True)

    # separar nombres de variables en categoricos y numericos
    tipos_object = df.loc[:, df.columns].dtypes
    categorical_names = tipos_object[tipos_object == object].index
    numeric_var = tipos_object[tipos_object != object].index

    # valores categoricos en nulos se reemplazan por la moda

    # categorical_transformer = SimpleImputer(strategy='most_frequent')
    # idf = pd.DataFrame(categorical_transformer.fit_transform(df))
    # categorical_transformer.fit(df[categorical_names])
    # idf.columns = df.columns
    # idf.index = df.index

    # df = idf

    # # get dummies
    # train_data = pd.get_dummies(
    #     df, columns=categorical_names, drop_first=True)
    # # renombrando la variable de respuesta
    # train_data = train_data.rename(
    #     columns={'fraudfound_p_1': 'fraudfound_p'})

    # pipeline de procesamiento
    var_cat_model = categorical_names[categorical_names != 'fraudfound_p']

    numeric_transformer = skPipeline(steps=[
        ('transfor_vars', SimpleImputer(strategy='mean')),
        ('scaler', StandardScaler())]
    )

    categorical_transformer = skPipeline(steps=[
        ('transfor_vars', SimpleImputer(strategy='most_frequent')),
        ('scaler', OneHotEncoder())]
    )

    pre_process = ColumnTransformer(remainder='passthrough',
                                    transformers=[
                                        ('drop_columns', 'drop', ['policynumber', 'repnumber', 'numberofsuppliments',
                                                                  'addresschange_claim', 'policereportfiled', 'witnesspresent', 'agenttype']),
                                        ('num', numeric_transformer, numeric_var),
                                        ('cat', categorical_transformer, var_cat_model)
                                    ]
                                    )

    X = df.drop(['fraudfound_p'], axis=1)
    y = df['fraudfound_p'].astype(int)
    nombresX = X.columns

    # creando set de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=123)

    # metodo de desbalanceo
    oversample = SMOTE(sampling_strategy='auto', random_state=123, )
    #nombres = X.columns

    # X_res, y_res = oversample.fit_resample(X_train, y_train)
    # X_res = pd.DataFrame(X_res, columns=nombres)
    print("Tamanio del X train:", X_train.shape)
    print("Tamanio del y train:", y_train.shape)

    # modelo
    model = XGBClassifier(objective="binary:logistic",
                          eval_metric="mlogloss", use_label_encoder=False)

    model_pipe = imbPipeline(steps=[
        ('pre', pre_process),
        ('smt', oversample),
        ('model', model)
    ]
    )

    print("Training model...")
    result = model_pipe.fit(X_train, y_train)
    return result
    
def export_model_trained(model: Any, path: str = '.'):
    print("exportando modelo...")
    with open(f"{path}/model.pickle", "wb") as file:
        pickle.dump(model, file)
    print('model saved')
