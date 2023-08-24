from cnnClassifire import logger
from cnnClassifire.pipline.stage_01_data_ingestion import DataIngestionTrainingPipeling
from cnnClassifire.pipline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline

STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<")
    stage_1_obj = DataIngestionTrainingPipeling()
    stage_1_obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx====================x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Prepare base model stage"

try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<")
    stage_2_obj = PrepareBaseModelTrainingPipeline()
    stage_2_obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx====================x")
except Exception as e:
    raise e
