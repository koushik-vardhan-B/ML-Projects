import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig
from src.components.model_trainer import ModelTrainerConfig
from src.components.model_trainer import ModelTrainer
from src.utils import evaluate_models
from dataclasses import dataclass
@dataclass
class DataIngestionConfig:
    train_data_path : str = os.path.join('artifacts', 'train.csv')
    test_data_path : str = os.path.join('artifacts', 'test.csv')
    raw_data_path : str = os.path.join('artifacts', 'raw.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
        
    def initiate_data_ingestion(self):
        logging.info("Entering the Data Ingestion method or component starts")
        try:
            df = pd.read_csv('notebooks/data/stud.csv')
            logging.info('Read the dataset as a DataFrame')
            
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            logging.info('Train test split initiated')
            
            train_set,test_set = train_test_split(df, test_size=0.2, random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            logging.info('Ingestion of the data is completed')
            
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
                # self.ingestion_config.raw_data_path
            )
        except Exception as e:
            raise CustomException(e, sys) from e
        
if __name__ == "__main__":
    obj = DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()
    
    data_transformation = DataTransformation()
    train_arr, test_arr, preprocessor_path = data_transformation.initiate_data_transformation(train_data, test_data)
    
    model_trainer = ModelTrainer()
    print(model_trainer.initiate_model_trainer(
        train_array=train_arr, 
        test_array=test_arr, 
        preprocessor_path=preprocessor_path
    ))
# This code is part of a data ingestion module that reads a dataset, splits it into training and testing sets, and saves them to specified paths.
# It uses pandas for data manipulation and sklearn for splitting the dataset.
# The code also includes error handling and logging for better traceability.
# The DataIngestion class is initialized with a configuration for file paths, and the initiate_data_ingestion method performs the main functionality.
# The code is designed to be run as a script, and it will execute the data ingestion process when run directly.
# The code is structured to allow for easy integration into a larger data processing pipeline.
# The DataIngestionConfig class defines the paths for the training, testing, and raw data files.
# The code uses the dataclass decorator for cleaner and more efficient data structure definition.
# The initiate_data_ingestion method reads the dataset from a CSV file, splits it into training and testing sets, and saves them to the specified paths.
# The method also handles exceptions and logs the process for better debugging and maintenance.