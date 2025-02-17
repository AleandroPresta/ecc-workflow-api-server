#!/bin/bash

# Test the home endpoint
echo "Testing home endpoint..."
curl -X GET http://localhost:8000/api/v1/

# Test the LLM solver endpoint with trailing slash
echo -e "\n\nTesting LLM solver endpoint..."
curl -X POST http://localhost:8000/api/v1/solve/llm/ \
  -H "Content-Type: application/json" \
  -d '[
    {
      "name": "Sample Workflow",
      "tasks": [
        {
          "id": "task1",
          "requirements": {"cpu": 2, "memory": 4}
        }
      ]
    },
    {
      "services": [
        {
          "id": "service1",
          "capabilities": {"cpu": 4, "memory": 8}
        }
      ]
    }
  ]'