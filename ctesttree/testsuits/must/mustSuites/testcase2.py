
#
# SPEC for Tree Spec Must test case - 2
# SPEC Conform:
# When the current page is a tree:Node, there MUST be a property
# linking the current page URL to the URI of the tree:Collection.
#
# Verify: "Each tree:Node in the LDES Collection has
# a link between current page to tree:Collection."
#

from rdflib import Graph
import pyshacl
import requests

headers_get_json = {
    'accept': 'application/ld+json'
}
url_view = 'https://apim-iow-apimanagement.azure-api.net/ldes/devices/devices-by-time?pageNumber=1'


class MustTestCase2:
    def get_result(self):
        shapes_graph = Graph().parse("../mustShapes/testcase2.ttl", format="ttl")
        # data_graph = Graph().parse(requests.request("GET", url_view, headers=headers_get_json).content, format="json-ld")
        data_graph = Graph().parse("../../../../automation/expected/expected_timebase/random.turtle", format="ttl")
        results = pyshacl.validate(
            data_graph,
            shacl_graph=shapes_graph,
            data_graph_format="json-ld",
            shacl_graph_format="rdfs",
            inference="rdfs",
            debug=True,
            serialize_report_graph="ttl",
        )

        conforms, report_graph, report_text = results
        return conforms