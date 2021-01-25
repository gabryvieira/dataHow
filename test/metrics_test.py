import json
import unittest

from data.metrics import Metrics
from data import metricsJson


class TestMetrics(unittest.TestCase):

    def test_unique_ip_addresses(self):
        metrics = Metrics()
        ip_addresses = metrics.getUniqueIPAdresses(metricsJson.metricsLog)
        self.assertEqual(ip_addresses, 4)

    def test_get_number_of_connections(self):
        metrics = Metrics()
        total_connections = metrics.getNumberOfConnections(metricsJson.metricsLog)
        self.assertEqual(total_connections, 6)

    def test_get_different_urls(self):
        metrics = Metrics()
        different_urls = metrics.getDifferentURLs(metricsJson.metricsLog)
        self.assertEqual(different_urls, 2)

    def test_get_next_id(self):
        metrics = Metrics()
        next_id = metrics.getNextID(metricsJson.metricsLog)
        self.assertEqual(next_id, 7)
