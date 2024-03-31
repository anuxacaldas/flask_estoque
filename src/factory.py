import logging
import os
import json
import sys

from flask import Flask, render_template


def create_app(config_filename: str = 'config.dev.json') -> Flask:
    app = Flask(__name__,
                instance_relative_config=True,
                static_folder='static',
                template_folder='templates')

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.logger.setLevel(logging.DEBUG)

    app.logger.debug("Configurando a aplicação a partir do arquivo '%s'" % (config_filename))
    try:

        app.config.from_file(config_filename, load=json.load)
    except FileNotFoundError:
        app.logger.fatal("O arquivo de configuração '%s' não existe" % (config_filename))
        sys.exit(1)

        @app.route('/')
        @app.route('/index')
        def index():
            return render_template('index.jinja2', title="Página principal")

        return app

