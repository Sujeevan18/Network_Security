from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig, DataValidationConfig, TrainingPipelineConfig
import sys
from datetime import datetime

if __name__ == "__main__":
    try:
        # Create training pipeline config
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
        # Pass the ARTIFACT, not the CONFIG
        data_validation = DataValidation(data_ingestion_artifact, data_validation_config)

        logging.info("Initiating data validation...")
        data_validation_artifact = data_validation.initiate_data_validation()
        logging.info("Data validation completed successfully.")
        print(data_validation_artifact)

    except Exception as e:
        raise NetworkSecurityException(e, sys)
