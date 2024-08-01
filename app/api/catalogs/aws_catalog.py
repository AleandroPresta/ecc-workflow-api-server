aws_catalog = {
    "catalog": {
        "services" : [
            {
                "name": "Lambda Function",
                "id": 0,
                "type": "Computation",
                "parameters": {
                    "Execution Time": 5, # Execution time in ms
                },
                "description": """An AWS Lambda function is a small, single-purpose piece of code 
                that you can execute without provisioning or managing servers."""
            },
            {
               "name": "Lambda Function",
                "id": 1,
                "type": "Computation",
                "parameters": {
                    "Execution Time": 15, # Execution time in ms
                },
                "description": """An AWS Lambda function is a small, single-purpose piece of code 
                that you can execute without provisioning or managing servers.""" 
            },
            {
                "name": "S3 Bucket",
                "id": 2,
                "type": "Storage",
                "parameters": {
                    "Type of Database": "SQL",
                    "Available Memory": 1280, # Memory size in MB
                },
                "description": """A storage container used to store objects like files and data. 
                It offers scalable, durable, and secure storage, with features such as 
                access control, encryption, lifecycle management, versioning, and event notifications"""
            },
            {
                "name": "S3 Bucket",
                "id": 3,
                "type": "Storage",
                "parameters": {
                    "Type of Database": "SQL",
                    "Available Memory": 800, # Memory size in MB
                },
                "description": """A storage container used to store objects like files and data. 
                It offers scalable, durable, and secure storage, with features such as 
                access control, encryption, lifecycle management, versioning, and event notifications"""
            },
            {
                "name": "Amazon TimeStream",
                "id": 4,
                "type": "Storage",
                "parameters": {
                    "Type": "Time Series",
                    "Available Memory": 1100, # Memory size in MB
                },
                "description": """Amazon Timestream offers fully managed, purpose-built 
                time-series database engines for workloads from low-latency queries 
                to large-scale data ingestion."""
            },
            {
                "name": "DocumentDB",
                "id": 5,
                "type": "Storage",
                "parameters": {
                    "Type": "JSON",
                    "Available Memory": 1200, # Memory size in MB
                },
            },
            {
                "name" : "Cloud Component",
                "id": 6,
                "type": "Computation",
                "parameters": {
                    "Execution Time": 100, # Execution time in ms
                },    
            },
            {
                "name" : "ML Component",
                "id": 7,
                "type": "Computation",
                "parameters": {
                    "Execution Time": 100, # Execution time in ms
                    "ML": "Yes",
                },    
            },
            {
                "name": "Amazon SageMaker",
                "id": 8,
                "type": "Computation",
                "parameters": {
                    "ML": "Yes",
                },
                "description": """Amazon SageMaker is a fully managed service that brings 
                together a broad set of tools to enable high-performance, 
                low-cost machine learning (ML) for any use case."""
            },
            {
                "name": "AWS IoT Greengrass",
                "id": 8,
                "type": "Computation",
            },
            {
                "name": "AWS Glue",
                "id": 9,
                "type": "Computation",
            },
        ]
    }
}