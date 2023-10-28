from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.data_validation import DataValidation
from textSummarizer.logging import logger


STAGE_NAME = "Data Validation stage"


class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(data_validation_config)
        data_validation.validate_all_files_exist()


try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataValidationTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e
