aws_catalog = {
    "catalog": {
        "services" : [
            {
                "name": "Lambda Function",
                "id": 0,
                "type": "Computation",
                "parameters": {
                    "topic": "0", # 0: Local publish/subscribe, 1: AWS IoT Core MQTT 
                    "timeout": "3", # Timeout in seconds
                    "encoding_type" : "0", # 0: JSON, 1: Binary
                    "os": "0", # 0: Linux, 1: Windows
                    "architecture": "0", # 0: amd64, 1: arm, 2: aarch64, 3: x86
                    "memory_size": "128", # Memory size in MB
                },
                "description": """An AWS Lambda function is a small, single-purpose piece of code 
                that you can execute without provisioning or managing servers."""
            },
            {
                "name": "S3 Bucket",
                "id": 1,
                "type": "Storage",
                "parameters": {
                    "region": "0", # 0:
                    "storage_class": "0", # 0: Standard, 1: Intelligent-Tiering, 2: One Zone-IA, 3: Glacier
                    "encryption": "0", # 0: AES256, 1: aws:kms
                    "public_access": "0", # 0: Enabled, 1: Disabled
                },
                "description": """A storage container used to store objects like files and data. 
                It offers scalable, durable, and secure storage, with features such as 
                access control, encryption, lifecycle management, versioning, and event notifications"""
            },
            {
                "name": "Amazon TimeStream",
                "id": 2,
                "type": "Storage",
                "parameters": {
                    "region": "0", # 0:
                    "retention_period": "1", # Retention period in days
                    "memory_size": "128", # Memory size in MB
                },
                "description": """Amazon Timestream offers fully managed, purpose-built 
                time-series database engines for workloads from low-latency queries 
                to large-scale data ingestion."""
            },
            {
                "name": "Amazon SageMaker",
                "id": 3,
                "type": "Machine Learning",
                "parameters": {
                    "region": "0", # 0:
                    "instance_type": "0", # 0: ml.t2.medium, 1: ml.t2.large, 2: ml.t2.xlarge
                    "instance_count": "1", # Number of instances
                    "model": "0", # 0: Linear Regression, 1: Decision Trees, 2: Neural Networks
                },
                "description": """Amazon SageMaker is a fully managed service that brings 
                together a broad set of tools to enable high-performance, 
                low-cost machine learning (ML) for any use case."""
            }
        ]
    }
}