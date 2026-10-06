# TDD and BDD Final Project

## Product Catalogue Microservice

This project implements a RESTful product catalogue backend for an e-commerce application using Test Driven Development (TDD) and Behaviour Driven Development (BDD) practices.

### Features
- Create, Read, Update, Delete products
- List all products
- Search by name, category, and availability
- BDD scenarios using Behave and Selenium

### Tech Stack
- Python, Flask, SQLAlchemy
- factory_boy for test data
- Behave + Selenium for BDD

### Project Structure
```
├── service/
│   ├── __init__.py
│   ├── models.py       # Product model
│   ├── routes.py       # REST API endpoints
│   └── status.py       # HTTP status codes
├── tests/
│   ├── factories.py    # ProductFactory
│   ├── test_models.py  # Model unit tests
│   └── test_routes.py  # Route unit tests
├── features/
│   ├── products.feature        # BDD scenarios
│   ├── environment.py          # Behave environment
│   └── steps/
│       ├── load_steps.py       # Background data loading
│       └── web_steps.py        # Selenium step definitions
└── requirements.txt
```

### Running Tests
```bash
python -m pytest tests/
behave features/
```
