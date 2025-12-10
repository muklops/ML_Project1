from src.MLProject.utils import logger
from src.MLProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.MLProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from src.MLProject.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline

stage_name = "Data Ingestion Stage"
try:
    logger.info(f">>>>>> stage {stage_name} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {stage_name} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

stage_name = "Data Validation Stage"
try:    
    logger.info(f">>>>>> stage {stage_name} started <<<<<<")
    obj = DataValidationTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {stage_name} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e     

stage_name = "Data Transformation Stage"
try:
    logger.info(f">>>>>> stage {stage_name} started <<<<<<")
    from src.MLProject.pipeline.stage_03_data_transformation import DataTransformationPipeline
    obj = DataTransformationPipeline()
    obj.main()
    logger.info(f">>>>>> stage {stage_name} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e   

stage_name = "Model Trainer Stage"
try:
    logger.info(f">>>>>> stage {stage_name} started <<<<<<")
    obj = ModelTrainerTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {stage_name} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e
            