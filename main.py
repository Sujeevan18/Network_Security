import sys
from datetime import datetime

from networksecurity.components.model_trainer import ModelTrainer
from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.data_transformation import DataTransformation

from networksecurity.entity.config_entity import (
    DataIngestionConfig,
    DataValidationConfig,
    DataTransformationConfig,
    TrainingPipelineConfig,
    ModelTrainerConfig,
)
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

if __name__ == "__main__":
    try:
        # Pipeline config (timestamped artifact dir)
        training_pipeline_config = TrainingPipelineConfig(timestamp=datetime.now())

        # ------------------- Data Ingestion -------------------
        data_ingestion_config = DataIngestionConfig(training_pipeline_config)
        data_ingestion = DataIngestion(data_ingestion_config)

        logging.info("Initiating data ingestion...")
        data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
        logging.info("Data ingestion completed successfully.")
        print(data_ingestion_artifact)

        # ------------------- Data Validation -------------------
        data_validation_config = DataValidationConfig(training_pipeline_config)
        data_validation = DataValidation(data_ingestion_artifact, data_validation_config)

        logging.info("Initiating data validation...")
        data_validation_artifact = data_validation.initiate_data_validation()
        logging.info("Data validation completed successfully.")
        print(data_validation_artifact)

        # ------------------- Data Transformation -------------------
        data_transformation_config = DataTransformationConfig(training_pipeline_config)
        data_transformation = DataTransformation(data_validation_artifact, data_transformation_config)

        logging.info("Initiating data transformation...")
        data_transformation_artifact = data_transformation.initiate_data_transformation()
        logging.info("Data transformation completed successfully.")
        print(data_transformation_artifact)

        # ------------------- Model Training -------------------
        logging.info("Initiating model training...")
        model_trainer_config = ModelTrainerConfig(training_pipeline_config)
        model_trainer = ModelTrainer(
            model_trainer_config=model_trainer_config,
            data_transformation_artifact=data_transformation_artifact,
        )
        model_trainer_artifact = model_trainer.initiate_model_trainer()
        logging.info("Model training completed successfully.")
        print(model_trainer_artifact)

    except Exception as e:
        raise NetworkSecurityException(e, sys)
