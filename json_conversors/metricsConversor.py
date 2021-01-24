import logging

from flask import jsonify

from data.metrics import Metrics

def uniqueIPAddressesToJSON(metricsList):
    assert metricsList is not None, "Cannot get unique ip addresses!"

    metrics = Metrics()
    uniqueIPAddresses = metrics.getUniqueIPAdresses(metricsList)

    return jsonify({"Number of unique IP addresses": uniqueIPAddresses})

def getAllMetricsToJSON(metricsList):
    assert metricsList is not None, "Cannot get metrics!"

    metrics = Metrics()
    allMetrics = metrics.getMetrics()

    return jsonify({"Metrics": allMetrics})

def lastConnectionToJSON(metricsList):
    assert metricsList is not None, "Cannot the most recent connection!"

    metrics = Metrics()
    lastConnection = metrics.getLastConnection(metricsList)

    return jsonify({"Last connection at": lastConnection})