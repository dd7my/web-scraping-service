# Web Scraping Service

A lightweight, Docker-ready Python microservice that exposes a REST API for extracting content from web pages using CSS selectors. Built with Flask, Requests, and Scrapling.

## Features

- **RESTful API**: Simple POST endpoint to schedule and execute scraping tasks.
- **Dynamic Selection**: Customize exactly what elements to scrape on a page using CSS selectors.
- **Production-Ready**: Configured with `waitress` as a production WSGI server.
- **Dockerized**: Easy to build, deploy, and scale via Docker.
- **CORS Support**: Configurable Cross-Origin Resource Sharing.

## Requirements

- Python 3.11+
- [Docker](https://docs.docker.com/get-docker/) (optional, for containerized deployment)

## Installation (Local)

1. **Clone the repository** (if applicable) and navigate to the project directory:
   ```bash
   cd web-scraping-service
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables**:
   Copy the example environment file and configure it:
   ```bash
   cp .env.example .env
   ```
   *Available variables:*
   - `PORT`: Define the port for the application (default: 5000).
   - `FLASK_ENV`: Set to `development` for local dev or `production` for prod deployment.
   - `ALLOWED_ORIGIN`: Configure CORS origins (e.g., `http://localhost:3000` or `*`).

## Usage

### Running Locally

To run the application in development mode:
```bash
# Ensure FLASK_ENV=development is set in your .env
python app.py
```

To run the application in production mode, Waitress will automatically be used if `FLASK_ENV!=development`:
```bash
python app.py
```

### Running with Docker

1. **Build the image**:
   ```bash
   docker build -t web-scraping-service .
   ```

2. **Run the container**:
   ```bash
   docker run -p 5000:5000 --env-file .env web-scraping-service
   ```

## API Reference

### `POST /api/scrape`

Extracts data from a given URL based on a CSS selector.

**Request Body:**

```json
{
  "url": "https://example.com",
  "selector": "h1" 
}
```
- `url` (string, required): The target webpage to scrape.
- `selector` (string, optional): The CSS selector of elements to extract. Defaults to `"h1"`.

**Success Response:**

```json
{
  "success": true,
  "data": [
    "Example Domain"
  ],
  "count": 1
}
```

**Error Response:**

```json
{
  "success": false,
  "error": "Error message details here"
}
```
*or*
```json
{
  "error": "url is required"
}
```

## Testing

The project includes unit tests using `pytest`. To run them:

```bash
pytest
```
