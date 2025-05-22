# Capstone Backend

A FastAPI-based backend service that provides secure password validation using Private Set Intersection (PSI) technology with OpenMined PSI library.

## Prerequisites

Before setting up this project, make sure you have **Python** installed on your system.

- **Python 3.8 or higher** is required
- You can download Python from [python.org](https://www.python.org/downloads/)
- **Bazel** build tool is required for building the PSI library

## Project Setup

### 1. Clone the Repository

```bash
git clone https://github.com/hf-cure/capstone.git
cd capstone
```

### 2. PSI OpenMined Library Installation

Follow these steps carefully to install and configure the PSI OpenMined library:

#### Step 1: Navigate to PSI Directory
```bash
cd private_set_intersection
```

#### Step 2: Move to Python Directory
```bash
cd python
```

#### Step 3: Install OpenMined PSI
```bash
pip install openmined-psi
```

#### Step 4: Run Tests
Replace `3_8` with your Python version (e.g., `3_9`, `3_10`, etc.)
```bash
bazel test --test_output=all //private_set_intersection/python:test_3_8
```

#### Step 5: Run Benchmark
Replace `3_8` with your Python version
```bash
bazel run -c opt --test_output=all //private_set_intersection/python:benchmark_3_8
```

#### Step 6: Add Dependencies
Add any dependencies to `requirements.in` and then run:
```bash
bazel run //private_set_intersection/python/requirements:requirements_3_8.update
```
Replace `3_8` with your Python version.

#### Step 7: Build the Wheel
```bash
bazel build -c opt //private_set_intersection/python:wheel
```

#### Step 8: Build and Publish (Optional)
To build and publish in one go to test PyPi:
```bash
bazel build -c opt //private_set_intersection/python:wheel
```

### 3. Run the FastAPI Project

After completing the PSI library setup (steps 1-8), navigate back to the main directory:

```bash
cd ../../  # Go back to main project directory
```

Verify that `main.py` is in the current folder:
```bash
ls main.py
```

Run the FastAPI development server:
```bash
fastapi dev main.py
```

## Application Details

- **Port**: The backend service runs on port `8000`
- **API Base URL**: http://127.0.0.1:8000/
- **Framework**: FastAPI
- **Security**: Uses Private Set Intersection (PSI) for secure password validation

## How It Works

1. The backend receives password validation requests from the frontend
2. Uses PSI (Private Set Intersection) technology with OpenMined library
3. Securely checks if the submitted password exists in the database
4. Returns validation results without exposing the actual database contents
5. Maintains user privacy through cryptographic protocols

## API Integration

This backend service is designed to work with the frontend application running on port 5000. The typical flow is:

1. Frontend sends password validation request
2. Backend processes the request using PSI
3. Password is checked against rockyou.txt database
4. Results are returned to frontend for display

## Important Notes

- The first 8 steps are crucial for building the PSI library correctly
- Make sure to replace `3_8` with your actual Python version in all commands
- Bazel build tool is required for the PSI library compilation
- The rockyou.txt database is used for password validation

## Troubleshooting

- Ensure Python is properly installed and accessible
- Verify Bazel is installed for building the PSI library
- Check that you're using the correct Python version in commands
- Make sure `main.py` is in the root directory before running FastAPI
- Ensure no other application is using port 8000

## Repository

Backend Repository: https://github.com/hf-cure/capstone
Frontend Repository: https://github.com/hf-cure/capstone-frontend
