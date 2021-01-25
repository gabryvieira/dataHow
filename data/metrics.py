from flask import jsonify

from data.metricsJson import metricsLog

class Metrics:
    def __init__(self):
        pass

    def getUniqueIPAdresses(self, metricsList):
        unique_ips = len(set(p['ip'] for p in metricsList))
        return unique_ips

    def getMetrics(self):
        return metricsLog

    def getNextID(self, metricsList):
        maxID = max(p['id'] for p in metricsList)
        return maxID+1

    def getNumberOfConnections(self, metricsList):
        return len(metricsList)

    def getDifferentURLs(self, metricsList):
        differentUrls = len(set(p['url'] for p in metricsList))
        return differentUrls

    def getLastConnection(self, metricsList):
        timestamps = max(p['timestamp'] for p in metricsList)
        return timestamps

    ### to json
    def uniqueIPAddressesToJSON(self, metricsList):
        assert metricsList is not None, "Cannot get unique ip addresses!"

        uniqueIPAddresses = self.getUniqueIPAdresses(metricsList)

        return jsonify({"unique_ip_addresses": uniqueIPAddresses})

    def getAllMetricsToJSON(self, metricsList):
        assert metricsList is not None, "Cannot get metrics!"

        allMetrics = self.getMetrics()

        return jsonify({"all_metrics": allMetrics})

    def lastConnectionToJSON(self, metricsList):
        assert metricsList is not None, "Cannot the most recent connection!"

        lastConnection = self.getLastConnection(metricsList)

        return jsonify({"last_connection_at": lastConnection})

    def differentUrlsToJSON(self, metricsList):
        assert metricsList is not None, "Cannot the most recent connection!"

        differentUrls = self.getDifferentURLs(metricsList)

        return jsonify({"different_urls": differentUrls})