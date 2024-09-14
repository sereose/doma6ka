from flask import Flask, jsonify
from urllib.parse import urlparse as url_parse

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/healthcheck')
def health_check():
    # Perform any health checks you need here (database connection, etc.)
    # For now, we'll just simulate a successful check
    return jsonify({'status': 'healthy'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0')
