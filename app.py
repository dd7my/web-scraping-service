import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

from scrapers.static_scraper import scrape_data

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Configure CORS more securely based on environment
allowed_origin = os.environ.get("ALLOWED_ORIGIN", "*") 
CORS(app, resources={r"/api/*": {"origins": allowed_origin}})

@app.route('/', methods=['GET'])
def health():
    return jsonify({
        "service": "Web Scraping Service",
        "status": "ok",
        "endpoints": {
            "POST /api/scrape": "Scrape a URL with a CSS selector"
        }
    })

# @app.route('/api/scrape', methods=['POST'])
# def scrape():
#     body = request.get_json()
#     url = body.get('url')
#     selector = body.get('selector', 'h1')
#     if not url:
#         return jsonify({"error": "url is required"}), 400
#     result = scrape_data(url, selector)
#     return jsonify(result)

@app.route('/api/scrape', methods=['POST'])
def scrape():
    body = request.get_json()

    url = body.get('url')
    selectors = body.get('selectors')

    if not url:
        return jsonify({"error": "url is required"}), 400

    if not selectors:
        selectors = {
            "titles": {"selector": "h1", "attr": "text"}
        }

    result = scrape_data(url, selectors)

    return jsonify(result)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    flask_env = os.environ.get("FLASK_ENV", "development")
    
    if flask_env == "development":
        app.run(debug=True, port=port)
    else:
        from waitress import serve
        print(f"Starting production server on port {port}...")
        serve(app, host="0.0.0.0", port=port)
