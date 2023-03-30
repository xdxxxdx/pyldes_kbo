#!/usr/bin/python
import unittest
from pyldes_kbo.automation.support import Support
from rdflib import Graph
import time
su = Support()

class TestDefaultPagination(unittest.TestCase):
    def test_1_startServices(self):
         su.startService()
         time.sleep(60)
         self.assertEqual(su.serverReady(), 200)
    def test_2_postData_2(self):
         su.postData()
         self.assertEqual(su.serverReady(), 200)
    def test_3_tearDown(self):
         su.stopServer()
