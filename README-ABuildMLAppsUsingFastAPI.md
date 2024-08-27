# Build ML Apps w FastAPI
Folder => Build-ML-App-FASTAPI

## REST API vs OpenAPI
- REST API is the actual web service that follows REST principles, 
- OpenAPI (OAS) is a standard specification used to describe, document, and define how a REST API should behave.

### How REST API Works?
- Resources (data objects, services etc.) via URI (Uniform Resources Identifier)
- HTTP Methods (GET, POST, PUT, DELETE)
- Stateless communication

// Response
- HTTP Status Code
- Headers
- Data objects (Json or XML)

### What is FastAPI
- FastAPI is a modern, fast (high-performance), web framework for building APIs with Python.
- It's designed to make it easy to create RESTful APIs with minimal code while ensuring type safety, 
  automatic documentation, and high performance.
- FastAPI has gained significant popularity in the Python web development community due to its simplicity and efficiency.

https://fastapi.tiangolo.com/features/
- High Performance
- Asynchronous Support
- Automatic Interactive API Documentation (OAS)
- Type Annotations and Validation
- Dependency Injection
- Minimal Boilerplate
- Compatibility with Other Python Web Frameworks
- Supports WebSocket
- Community and Ecosystem
- Security and Authentication https://fastapi.tiangolo.com/features/#security-and-authentication
- Middleware supports such as logging, CORS etc.
- Extensible via custom components, authentication, plugins

// Test FastAPI
pip install fastapi[all]

cd Build-ML-App-FASTAPI
uvicorn fastapi-demo:app --reload
http://127.0.0.1:8000/
  {
    Hello: "World"
  }

http://127.0.0.1:8000/docs
