from paste.httpserver import serve
from pyramid.config import Configurator


def main():
    config = Configurator()
    # enable development mode
    config.registry.settings['debug_templates'] = True
    config.registry.settings['reload_assets'] = True
    config.registry.settings['reload_resources'] = True
    config.registry.settings['reload_templates'] = True
    config.registry.settings['pyramid.debug_templates'] = True
    config.registry.settings['pyramid.reload_assets'] = True
    config.registry.settings['pyramid.reload_resources'] = True
    config.registry.settings['pyramid.reload_templates'] = True
    # normal setup
    config.scan("bottlecap")
    from bottlecap import layout
    config.include(layout.configure)
    app = config.make_wsgi_app()
    return app


if __name__ == '__main__':
    app = main()
    serve(app, host='0.0.0.0')
