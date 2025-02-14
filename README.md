# Stepstone Job Scraper

## Overview
This project is a web scraper built with Selenium that automates the process of searching and collecting job listings from Stepstone. It handles the complete workflow from login to saving job data in a PostgreSQL database.

## Features
- Automated job search with customizable parameters
- Handles cookie consent automatically
- User authentication
- Database storage of job listings
- Comprehensive error handling and logging
- Unit testing support
- Docker and docker-compose.yml files

## Project Structure

SeleniumUnittestExample/
├── source/
│   ├── __init__.py
│   ├── stepstone.py #main scrapper implementation
│   ├── cfg #general configuration and database configurations
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── cookie_handle.py #cookie management
│   │   └── continue_next_page.py #navigation utility
│   ├── selection_handle/
│   │   ├── __init__.py
│   │   ├── selection.py #search criteria selections
│   │   └── logging_in.py #authentication handling
│   └── fetching_job_info/
│       ├── __init__.py
│       ├── fetch_job_properties.py # job info extraction
│       └── db.py #database operations
├── tests/
│   ├── __init__.py
│   └── test_stepstone.py #unit tests
└── requirements.txt #project dependencies

├── source/
│ ├── init.py
│ ├── stepstone.py # Main scraper implementation
│ ├── config/
│ │ ├── init.py
│ │ ├── db_config.py # Database configuration
│ │ └── cfg.py # General configuration
│ ├── utils/
│ │ ├── init.py
│ │ ├── cookie_handle.py # Cookie management
│ │ └── continue_next_page.py # Navigation utilities
│ ├── selection_handle/
│ │ ├── init.py
│ │ ├── selection.py # Search criteria selection
│ │ └── logging_in.py # Authentication handling
│ └── fetching_job_info/
│ ├── init.py
│ ├── fetch_job_properties.py # Job data extraction
│ └── db.py # Database operations
├── tests/
│ ├── init.py
│ └── test_stepstone.py # Unit tests
└── requirements.txt # Project dependencies

## Prerequisites
- Python 3.8+
- PostgreSQL database
- Chrome WebDriver

## Installation
1. Clone the repository:
2. Create a virtual environment
3. Install dependencies
4. Set up and configure database


## Usage
python -m source.stepstone.py

## Tests
python -m pytest tests/test_stepstone.py
