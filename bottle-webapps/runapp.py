import argparse
import bottle


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run a web user interface for labeling camera trap images for classification.')
    parser.add_argument('--host', type=str, default='0.0.0.0', help='Web server host to bind to.')## default='localhost', help='Web server host to bind to.')
    parser.add_argument('--port', type=int, default=8080, help='Web server port port to listen on.')
    args = parser.parse_args(sys.argv[1:])


    # -------------------------------------------------------------------------------- #
    # CREATE AND SET UP A BOTTLE APPLICATION FOR THE WEB UI
    # -------------------------------------------------------------------------------- #
    
    webapp = bottle.Bottle()
    webapp.add_hook("after_request", enable_cors)
    webapp_server_kwargs = {
        "server": "tornado",
        "host": args.host,
        "port": args.port
    }

    @webapp.route('/')
    def index():
        return bottle.static_file("index.html", root='static/html')

    webapp.run(**webapp_server_kwargs)