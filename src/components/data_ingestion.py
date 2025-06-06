import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
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
    obj.initiate_data_ingestion()
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