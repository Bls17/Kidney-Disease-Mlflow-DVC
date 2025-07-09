from src.cnnClassifier.pipeline.stage_01_data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.cnnClassifier.pipeline.stage_02_prepare_base_model_pipeline import PrepareBaseModelTraningPipeline
from src.cnnClassifier import logger

STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.initiate_data_ingestion()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
     

STAGE_NAME = "Prepare base model"
try:
      logger.info(f"*******************")
      logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
      obj = PrepareBaseModelTraningPipeline()
      obj.initiate_prepare_base_model()
      logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
      logger.exception(e)
      raise e