# training pipeline
import os
import sys
import numpy as np
import pandas as pd
import pickle
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

from src.exception import CustomException
from src.utils import save_object, evaluate_models, load_object

def training_pipeline(data, model_config, param_config, save_model_path):
    try:
        X = data.drop(columns=["target"])
        y = data["target"]

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        models = {
            "RandomForest": RandomForestRegressor(),
            "LinearRegression": LinearRegression()
        }

        report = evaluate_models(X_train, y_train, X_test, y_test, models, param_config)

        best_model_name = max(report, key=report.get)

        best_model = models[best_model_name]

        best_model.fit(X_train, y_train)

        save_object(save_model_path, best_model)

        return report

    except Exception as e:
        raise CustomException(e, sys)
      
