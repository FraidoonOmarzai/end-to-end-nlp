from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.model_training import ModelTraining
from textSummarizer.logging import logger


STAGE_NAME = "ModelTraning stage"


class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_training_config = config.get_model_tranining_config()
        model = ModelTraining(model_training_config)
        model.train()


try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = ModelTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e
