#!/usr/bin/env python3

import socket
import os
import uuid
from flask import Flask, jsonify, make_response

# os.environ['AUTHOR'] = 'dizz23'
# os.environ['UUID'] = str(uuid.uuid4())


def main():
    app = Flask(__name__)

    @app.route('/hostname', methods=['GET'])
    def hostname():
        return socket.gethostname()

    @app.route('/author', methods=['GET'])
    def author():
        return os.environ.get('AUTHOR', '')
    
    @app.route('/id', methods=['GET'])
    def id():
        return os.environ.get('UUID', '')

    @app.errorhandler(404)
    def not_found(error):
        return make_response(jsonify({'error': 'Not found'}), 404)

    app.run(host='0.0.0.0', port='8000')

if __name__ == '__main__':
    main()
