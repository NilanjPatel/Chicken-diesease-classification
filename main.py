from cnnClassifire import logger
from cnnClassifire.pipline.stage_01_data_ingestion import DataIngestionTrainingPipeling

STAGE_NAME = "Data Ingestion stage"


try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<")
    stage_1_obj = DataIngestionTrainingPipeling()
    stage_1_obj.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx====================x")
except Exception as e:
    logger.exception(e)
    raise e
