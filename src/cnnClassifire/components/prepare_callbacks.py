# create component


import os
import urllib.request as request
from zipfile import ZipFile
import tensorflow as tf
import time
from cnnClassifire.entity.config_entity import PrepareCallbacksConfig
from cnnClassifire.config.configuration import ConfigurationManager

class PrepareCallback:
    def __init__(self, config: PrepareCallbacksConfig):
        self.config = config

    @property
    def _create_tb_callbacks(self):
        timestamp = time.strftime("%Y-%m-%d-%H-%M-%S")
        print(
            f"config.tensorboard_root_log_dir:{self.config.tensorboard_root_log_dir}, {type(self.config.tensorboard_root_log_dir)}")

        tb_running_log_dir = os.path.join(
            self.config.tensorboard_root_log_dir,
            f"tb_logs_at_{timestamp}",
        )
        return tf.keras.callbacks.TensorBoard(log_dir=tb_running_log_dir)

    @property
    def _create_ckpt_callbacks(self):
        print(
            f"config.checkpoint_model_filepath:{self.config.checkpoint_model_filepath}, {type(self.config.checkpoint_model_filepath)}")
        return tf.keras.callbacks.ModelCheckpoint(
            filepath=str(self.config.checkpoint_model_filepath),
            monitor='val_loss',
            save_best_only=True,
            save_weights_only=False,
            mode='min',
            verbose=1
        )

    def get_tb_ckpt_callbacks(self):
        return [
            self._create_tb_callbacks,
            self._create_ckpt_callbacks
        ]


if '__main__' == __name__:
    try:
        config = ConfigurationManager()
        prepare_callbacks_config = config.get_prepare_callback_config()
        prepare_callbacks = PrepareCallback(config=prepare_callbacks_config)
        callback_list = prepare_callbacks.get_tb_ckpt_callbacks()
    except Exception as e:
        raise e