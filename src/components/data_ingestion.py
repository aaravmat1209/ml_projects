import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.components.data_transformation import DataTransformation, DataTransformationConfig

from src.components.model_trainer import ModelTrainerConfig
from src.components.model_trainer import ModelTrainer

#Read the dataset from a specific data source   

@dataclass
#inputs for the data ingestion class
class DataIngestionConfig:
  train_data_path: str=os.path.join('artifacts', "train.csv")
  test_data_path: str=os.path.join('artifacts', "test.csv")
  raw_data_path: str=os.path.join('artifacts', "data.csv") 
  
class DataIngestion:
  def __init__(self):
    #saving all three paths in the ingestion config PATH variable
    self.ingestion_config = DataIngestionConfig()
  
  def initiate_data_ingestion(self):
    logging.info("Entered the data ingestion method or component")
    try:
      #reading the dataset from the data source
      df = pd.read_csv('notebook\data\stud.csv')
      logging.info("Read the dataset as dataframe")

      #saving the dataset to the raw data path
      os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
      
      #converting the dataset to a csv file
      df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

      logging.info("Train test split initiated")
      train, test = train_test_split(df, test_size=0.2, random_state=42)

      #saving train and test data to the respective paths 
      train.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
      test.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

      logging.info("Ingestion of data is completed")

      return (
        self.ingestion_config.train_data_path,
        self.ingestion_config.test_data_path,
        
      )

    except Exception as e:
      raise CustomException(e, sys)
    
if __name__ == "__main__":
  data_ingestion = DataIngestion()
  train_data, test_data = data_ingestion.initiate_data_ingestion()

  data_transformation = DataTransformation()
  train_arr, test_arr, _ = data_transformation.initiate_data_transformation(train_data,test_data)

  model_trainer = ModelTrainer()
  print(model_trainer.initiate_model_trainer(train_arr, test_arr))

