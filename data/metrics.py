from data.metricsJson import metricsLog
from datetime import datetime, timezone

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