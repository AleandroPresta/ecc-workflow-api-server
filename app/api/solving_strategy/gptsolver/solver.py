from .config import model_config as config
import json

from .caller import GptCaller

"""
    This function is responsible for setting up the model to be used in the GPT API
"""
def setupModel():
        model: str = config["MODEL_CHOICES"][config["SELECTED_MODEL"]]
        temperature: float = config["TEMPERATURE"]
        gpt_caller: GptCaller = GptCaller(model=model, temperature=temperature)
        return gpt_caller
    

"""
    This function is responsible for setting up the files to be used inside the prompt
"""
def setupFiles(performance_path: str):        
    with open(performance_path, 'r') as file:
        performance: dict = json.load(file)
        
    return performance

def solve(workflow: dict, catalog: dict):
    gpt_caller: GptCaller = setupModel()
    
    n_of_generated_services: int = config["N_OF_SERVICES"]
    use_tags: bool = config["USE_TAGS"]
    
    performance: dict = setupFiles(config["PERFORMANCE_PATH"])
    
    return "Solved workflow using llm model"