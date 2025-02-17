model_config: dict = {
    # Takes the model choice from the command line argument
    "SELECTED_MODEL": 3,
    "MODEL_CHOICES" : {
        '1': "gpt-3.5-turbo", # Default model
        '2': "gpt-4o",
        '3': "o1-mini"
    },
    # Number of services to be generated for each abstract service (default: 5)
    "N_OF_SERVICES": 5,
    "TEMPERATURE": 0.0,
    "DEVELOPER_TEXT": "I want you to be my AWS Architecture expert. I have a workflow that I want to deploy on AWS.",
    "PERFORMANCE_PATH": './data/performance.json',
    "USE_TAGS": True # If True, the tags of the abstract service will be used to find the best concrete service from the catalog
}