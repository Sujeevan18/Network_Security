from datetime import datetime
import os
from networksecurity.constants.training_pipeline import _init_

print(_init_.PIPELINE_NAME)
print(_init_.ARTIFACT_DIR)

class TrainingPipelineConfig:
    def __init__(self, timestamp: datetime):
        timestamp = timestamp.strftime("%Y-%m-%d-%H-%M-%S")
        self.pipeline_name = _init_.PIPELINE_NAME
        self.artifact_name = _init_.ARTIFACT_DIR
        self.artifact_dir = os.path.join(self.artifact_name, timestamp)
        self.timestamp = timestamp

class DataIngestionConfig:
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        self.data_ingestion_dir:str=os.path.join(
            training_pipeline_config.artifact_dir,_init_.DATA_INGESTION_DIR_NAME
        )
        self.feature_store_file_path: str = os.path.join(
                self.data_ingestion_dir, _init_.DATA_INGESTION_FEATURE_STORE_DIR, _init_.FILE_NAME
            )
        self.training_file_path: str = os.path.join(
                self.data_ingestion_dir, _init_.DATA_INGESTION_INGESTED_DIR, _init_.TRAIN_FILE_NAME
            )
        self.testing_file_path: str = os.path.join(
                self.data_ingestion_dir, _init_.DATA_INGESTION_INGESTED_DIR, _init_.TEST_FILE_NAME
            )
        self.train_test_split_ratio: float = _init_.DATA_INGESTION_TRAIN_TEST_SPLIT_RATION
        self.collection_name: str = _init_.DATA_INGESTION_COLLECTION_NAME
        self.database_name: str = _init_.DATA_INGESTION_DATABASE_NAME

class DataValidationConfig:
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        self.data_validation_dir: str = os.path.join( training_pipeline_config.artifact_dir, _init_.DATA_VALIDATION_DIR_NAME)
        self.valid_data_dir: str = os.path.join(self.data_validation_dir, _init_.DATA_VALIDATION_VALID_DIR)
        self.invalid_data_dir: str = os.path.join(self.data_validation_dir, _init_.DATA_VALIDATION_INVALID_DIR)
        self.valid_train_file_path: str = os.path.join(self.valid_data_dir, _init_.TRAIN_FILE_NAME)
        self.valid_test_file_path: str = os.path.join(self.valid_data_dir, _init_.TEST_FILE_NAME)
        self.invalid_train_file_path: str = os.path.join(self.invalid_data_dir, _init_.TRAIN_FILE_NAME)
        self.invalid_test_file_path: str = os.path.join(self.invalid_data_dir, _init_.TEST_FILE_NAME)
        self.drift_report_file_path: str = os.path.join(
            self.data_validation_dir,
            _init_.DATA_VALIDATION_DRIFT_REPORT_DIR,
            _init_.DATA_VALIDATION_DRIFT_REPORT_FILE_NAME,
        )

class DataTransformationConfig:
     def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        self.data_transformation_dir: str = os.path.join( training_pipeline_config.artifact_dir, _init_.DATA_TRANSFORMATION_DIR_NAME )
        self.transformed_train_file_path: str = os.path.join( self.data_transformation_dir, _init_.DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR,
            _init_.TRAIN_FILE_NAME.replace("csv", "npy"),)
        self.transformed_test_file_path: str = os.path.join(self.data_transformation_dir,  _init_.DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR,
            _init_.TEST_FILE_NAME.replace("csv", "npy"), )
        self.transformed_object_file_path: str = os.path.join( self.data_transformation_dir, _init_.DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR,
            _init_.PREPROCESSING_OBJECT_FILE_NAME,)
        
class ModelTrainerConfig:
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        self.model_trainer_dir: str = os.path.join(
            training_pipeline_config.artifact_dir, _init_.MODEL_TRAINER_DIR_NAME
        )
        self.trained_model_file_path: str = os.path.join(
            self.model_trainer_dir, _init_.MODEL_TRAINER_TRAINED_MODEL_DIR, 
            _init_.MODEL_FILE_NAME
        )
        self.expected_accuracy: float = _init_.MODEL_TRAINER_EXPECTED_SCORE
        self.overfitting_underfitting_threshold = _init_.MODEL_TRAINER_OVER_FIITING_UNDER_FITTING_THRESHOLD