import logging

from flask import jsonify

from data.metrics import Metrics

def uniqueIPAddressesToJSON(metricsList):
    assert metricsList is not None, "Cannot get unique ip addresses!"

    metrics = Metrics()
    uniqueIPAddresses = metrics.getUniqueIPAdresses(metricsList)

    return jsonify({"unique_ip_addresses": uniqueIPAddresses})

def getAllMetricsToJSON(metricsList):
    assert metricsList is not None, "Cannot get metrics!"

    metrics = Metrics()
    allMetrics = metrics.getMetrics()

    return jsonify({"all_metrics": allMetrics})

def lastConnectionToJSON(metricsList):
    assert metricsList is not None, "Cannot the most recent connection!"

    metrics = Metrics()
    lastConnection = metrics.getLastConnection(metricsList)

    return jsonify({"last_connection_at": lastConnection})