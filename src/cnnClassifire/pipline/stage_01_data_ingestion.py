from cnnClassifire.components.data_ingestion import DataIngestion
from cnnClassifire.config.configuration import ConfigurationManager
from cnnClassifire import logger

# try:
#     config = ConfigurationManager()
#     data_ingestion_config = config.get_data_ingestion_config()
#     data_ingestion = DataIngestion(config=data_ingestion_config)
#     data_ingestion.download_file()
#     data_ingestion.extract_zip_file()
# except Exception as e:
#     raise e

STAGE_NAME = "Data Ingestion stage"

class DataIngestionTrainingPipeling:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()


if __name__ == '__main__':
    try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<")
        stage_1_obj = DataIngestionTrainingPipeling()
        stage_1_obj.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx====================x")
    except Exception as e:
        logger.exception(e)
        raise e

