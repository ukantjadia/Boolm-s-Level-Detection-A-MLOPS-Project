from blooms.config.configuration import ConfigurationManager
from blooms.components.model_evaluation import ModelEvaluation
from blooms import logger

STAGE_NAME = "Model Evaluation Stage"

class ModelEvaluationPipeline:
    def __init__(self) -> None:
        pass
    
    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(config=model_evaluation_config)
        model_evaluation.log_into_mlflow()
        
        
if __name__ == "__main__":
    try:
        logger.info(f">>>> stage {STAGE_NAME} started <<<<<")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f">>>> stage {STAGE_NAME} completed <<<<< \n\n x=======x")
    except Exception as e:
        logger.exception(e)
        raise e