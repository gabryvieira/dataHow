import threading

from flask import Flask, jsonify
import config

app1 = Flask(__name__)
app2 = Flask(__name__)


# def index() -> str:
#     # transform a dict into an application/json response
#     return jsonify({"message": "It Works"})

@app1.route('/')
def index1():
    return 'Logs micro service. Please go to /logs page'

@app2.route('/')
def index2():
    return 'Logs micro service. Please go to /metrics page'


@app1.route('/logs')
def logs():
    return 'Hello World 1'

@app2.route('/metrics')
def metrics():
    return 'Hello World 2'


# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=900)

# With Multi-Threading Apps, YOU CANNOT USE DEBUG!
# Though you can sub-thread.
def runLogs():
    app1.run(host=config.config_logs["host"], port=config.config_logs["port"], debug=False, threaded=True)

def runMetrics():
    app2.run(host=config.config_metrics["host"], port=config.config_metrics["port"], debug=False, threaded=True)


if __name__ == '__main__':
    # Executing the Threads seperatly.
    t1 = threading.Thread(target=runLogs)
    t2 = threading.Thread(target=runMetrics)
    t1.start()
    t2.start()
