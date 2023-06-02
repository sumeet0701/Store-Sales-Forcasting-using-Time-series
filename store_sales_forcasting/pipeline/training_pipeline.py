from store_sales_forcasting.config.configuration import Configuration
from store_sales_forcasting.logger import logging
from store_sales_forcasting.exception import SalesException
from store_sales_forcasting.utils.utils import read_yaml_file
from store_sales_forcasting.entity.artifact_entity import DataIngestionArtifact
#from store_sales_forcasting.entity.artifact_entity import DataValidationArtifact
#from store_sales_forcasting.entity.artifact_entity import DataTransformationArtifact
#from store_sales_forcasting.entity.artifact_entity import ModelTrainerArtifact
from store_sales_forcasting.components.data_ingestion import DataIngestion
#from store_sales_forcasting.components.data_validation import DataValidation
#from store_sales_forcasting.components.data_transformation import DataTransformation
#from store_sales_forcasting.components.model_trainer import ModelTrainer

from multiprocessing import Process
from threading import Thread
from typing import List
from collections import namedtuple
from datetime import datetime

import uuid
import os, sys
import pandas as pd



class Pipeline():

    def __init__(self, config: Configuration = Configuration()) -> None:
        try:
            self.config = config
        except Exception as e:
            raise SalesException(e, sys) from e

    def start_data_ingestion(self) -> DataIngestionArtifact:
        try:
            data_ingestion = DataIngestion(data_ingestion_config=self.config.get_data_ingestion_config())
            return data_ingestion.initiate_data_ingestion()
        except Exception as e:
            raise SalesException(e, sys) from e
        
    def run_pipeline(self):
        try:
             #data ingestion

            data_ingestion_artifact = self.start_data_ingestion()
           # data_validation_artifact = self.start_data_validation(data_ingestion_artifact=data_ingestion_artifact)
            #data_transformation_artifact = self.start_data_transformation(data_ingestion_artifact=data_ingestion_artifact,
            #                                                 data_validation_artifact=data_validation_artifact)
            #model_trainer_artifact = self.start_model_training(data_transformation_artifact=data_transformation_artifact)  

         
        except Exception as e:
            raise SalesException(e, sys) from e