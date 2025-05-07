# Image Analysis API

This is a RESTful API for managing users, images, and predictions in an image analysis system.

## Features

- User management (CRUD operations)
- Image management (CRUD operations)
- Prediction management (CRUD operations)
- OpenAPI/Swagger documentation
- CORS support
- Input validation
- Error handling
- CI/CD pipeline with GitHub Actions

## Getting Started

### Prerequisites

- Python 3.8+
- pip (Python package manager)

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd <repository-directory>
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running the Application

Start the FastAPI server:
```bash
uvicorn src.main:app --reload
```

The API will be available at `http://localhost:8000`

### Running Tests

Run the test suite locally:
```bash
# Install test dependencies
pip install pytest pytest-cov

# Run tests with coverage
pytest src/tests/ --cov=src
```

### API Documentation

Once the server is running, you can access:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## CI/CD Pipeline

This project uses GitHub Actions for continuous integration and deployment.

### Workflow

1. **Continuous Integration**
   - Runs on every push and pull request
   - Tests against Python 3.8, 3.9, and 3.10
   - Runs unit and integration tests
   - Generates code coverage reports

2. **Continuous Deployment**
   - Triggers on merge to main branch
   - Builds Python package
   - Uploads artifacts for release

### Branch Protection

The main branch is protected with the following rules:
- Requires pull request reviews
- Requires status checks to pass
- No direct pushes allowed

See [PROTECTION.md](PROTECTION.md) for detailed information.

## API Endpoints

### Users

- `POST /api/users` - Create a new user
- `GET /api/users` - Get all users
- `GET /api/users/{user_id}` - Get a specific user
- `PUT /api/users/{user_id}` - Update a user
- `DELETE /api/users/{user_id}` - Delete a user

### Images

- `POST /api/images` - Create a new image
- `GET /api/images` - Get all images
- `GET /api/images/{image_id}` - Get a specific image
- `PUT /api/images/{image_id}` - Update an image
- `DELETE /api/images/{image_id}` - Delete an image

### Predictions

- `POST /api/predictions` - Create a new prediction
- `GET /api/predictions` - Get all predictions
- `GET /api/predictions/{prediction_id}` - Get a specific prediction
- `PUT /api/predictions/{prediction_id}` - Update a prediction
- `DELETE /api/predictions/{prediction_id}` - Delete a prediction

## Project Structure

```
src/
├── main.py              # FastAPI application
├── models/             # Domain models
├── services/           # Business logic
│   ├── base_service.py
│   ├── user_service.py
│   ├── image_service.py
│   └── prediction_service.py
└── tests/              # Test files
    └── test_api.py
.github/
└── workflows/          # GitHub Actions workflows
    └── ci.yml
```

## Error Handling

The API uses standard HTTP status codes:
- 200: Success
- 400: Bad Request
- 404: Not Found
- 500: Internal Server Error

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request
6. Wait for CI checks and reviews
7. Merge after approval 