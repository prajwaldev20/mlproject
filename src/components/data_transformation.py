import sys
import os 
from dataclasses import dataclass
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from src.exception import CustomException
from src.logger import logging

@dataclass
class DataTransformation_config:
    preprocessor_ob_file_path = os.path.join('artifact',"preprocessor.pkl")


class DataTransformation:
    def __init__(self):
        self.data_transfromation_config = DataTransformation_config()

    def get_data_transformer_object(self):
        try:
            numerical_columns = ["writing_score","reading_score"]

            categorical_columns = [
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "test_preparation_course"
            ]

            num_pipeline = Pipeline(
                steps=[("imputer", SimpleImputer(strategy="median")),
                       ("scalar", StandardScaler())]
            )

            cat_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="most_frequent")),
                    ("one_hot_encoder", OneHotEncoder()),
                    ("scaler", StandardScaler())
                ]
            )

            logging.info(f"Categorical Columns: {categorical_columns}")

            logging.info(f"Numercial Column: {numerical_columns}")

            preprocessor = ColumnTransformer(
                ("num_pipeline", num_pipeline , numerical_columns),
                ("cat_pipline", cat_pipeline, categorical_columns)
            )

            return preprocessor

        except Exception as e:
            raise CustomException(e,sys)

