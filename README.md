# Clinical Trial Matching

## Overview
The Clinical Trial Matching project aims to bridge the gap between patients and relevant clinical trials by utilizing large language models (LLMs) to analyze electronic health records (EHRs) and clinical trial databases. This application will automate the extraction and standardization of trial eligibility criteria from various sources, enabling real-time matching of patients to suitable trials.

## Features
- Real-time matching of patients to clinical trials based on eligibility criteria.
- Automated extraction and standardization of trial criteria from PDFs and unstructured text.
- Interactive AI chatbots to guide patients in finding suitable trials.

## Project Structure
```
clinical-trial-matching
├── src
│   ├── app.py                # Main entry point of the application
│   ├── models
│   │   └── __init__.py       # Data models for patients and trials
│   ├── services
│   │   └── matching_service.py # Service for matching patients to trials
│   ├── utils
│   │   └── data_extraction.py  # Utility functions for data extraction
│   └── types
│       └── __init__.py       # Custom types and interfaces
├── requirements.txt          # Project dependencies
├── README.md                 # Project documentation
└── .gitignore                # Files to ignore in version control
```

## Setup Instructions
1. Clone the repository:
   ```
   git clone https://github.com/yourusername/clinical-trial-matching.git
   cd clinical-trial-matching
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   python src/app.py
   ```

## Usage Examples
- To match a patient to a trial, send a request to the appropriate endpoint with the patient's EHR data.
- Use the AI chatbot interface to interactively find suitable trials based on patient information.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License
This project is licensed under the MIT License - see the LICENSE file for details.