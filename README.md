# Secure Cloud Log Analyzer with MapReduce

A cloud-based log analysis platform developed using *Python, **Flask, **PostgreSQL (Neon DB), and **Railway Deployment*. The system allows authenticated administrators to upload server log files, process them using a MapReduce-inspired workflow, and generate analytical summaries such as HTTP error frequencies and peak traffic hours.

## Features

* Secure Administrator Authentication
* Log File Upload Interface
* MapReduce-Inspired Log Processing
* HTTP Error Analysis (404, 500, etc.)
* Peak Traffic Hour Detection
* PostgreSQL Cloud Database Integration
* Environment Variable Based Secrets Management
* Public Cloud Deployment via Railway
* Responsive Web Interface

## Technology Stack

### Backend

* Python
* Flask

### Database

* PostgreSQL
* Neon Database

### Frontend

* HTML
* CSS

### Cloud & DevOps

* GitHub
* Railway

## Project Workflow

1. Administrator logs into the portal.
2. A server log file is uploaded.
3. The system performs:

   * Split Phase
   * Map Phase
   * Shuffle & Sort Phase
   * Reduce Phase
4. Analytical results are generated.
5. Results are stored in PostgreSQL.
6. Results are displayed on the dashboard.

## Sample Output

The system can generate insights such as:

| Metric   | Count |
| -------- | ----- |
| HTTP_404 | 2     |
| HTTP_500 | 2     |
| HOUR_14  | 3     |
| HOUR_15  | 2     |
| HOUR_16  | 1     |

## Installation

Clone the repository:

bash
git clone <repository-url>
cd secure-cloud-log-analyzer


Install dependencies:

bash
pip install -r requirements.txt


Create a .env file:

env
DATABASE_URL=your_neon_database_url
SECRET_KEY=your_secret_key
ADMIN_USERNAME=admin
ADMIN_PASSWORD=admin123


Run the application:

bash
python app.py


Open:

text
http://127.0.0.1:5000

## Deployment

The application is deployed using Railway and connected to Neon PostgreSQL for cloud data persistence.

## Live Deployment URL:

https://secure-cloud-log-analyzer-production.up.railway.app

## Security

Sensitive credentials are not stored in source code.

The project uses:

* Environment Variables
* Secure Database Connections
* Hidden Credentials
* Cloud-Based Secrets Management
