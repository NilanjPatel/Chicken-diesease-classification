
from cnnClassifire.entity.config_entity import TrainingConfig
from cnnClassifire.config.configuration import ConfigurationManager
from cnnClassifire.components.prepare_callbacks import PrepareCallback
from cnnClassifire.components.training import Training
from cnnClassifire import logger
STAGE_NAME = "Training"


class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        prepare_callbacks_config = config.get_prepare_callback_config()
        prepare_callbacks = PrepareCallback(config=prepare_callbacks_config)
        callback_list = prepare_callbacks.get_tb_ckpt_callbacks()

        training_config = config.get_training_config()
        training = Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train(
            callback_list=callback_list
        )


STAGE_NAME = "Training Model"
if '__main__' == __name__:
    try:
        logger.info(f"****************************")
        logger.info(f">>>>>>>>>>>>>STAGE {STAGE_NAME} Started <<<<<<<<<<<<<<<<")
        model_trainer = ModelTrainingPipeline()
        model_trainer.main()
        logger.info(">>>>>>>>>> model training complete <<<<<<<<<<<<<<<<<<")
    except Exception as e:
        logger.error(e)
        raise e