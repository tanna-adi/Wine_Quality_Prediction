import os
from Wine_Quality_Prediction import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from Wine_Quality_Prediction.entity.config_entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    ## Note: need to add diffrent data transformation techniques such as Scaler,PCA, etc.
    # need to perform EDA here before passing data to the model

    def train_test_spliting(self):
        data = pd.read_csv(self.config.data_path)

        # split the data into training and test sets. (0.75, 0.25) split.
        train, test = train_test_split(data)

        train.to_csv(os.path.join(self.config.root_dir,"train.csv"),index = False)
        test.to_csv(os.path.join(self.config.root_dir,"test.csv"),index = False)
        
        logger.info("Splited data into training and test sets")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)
        

