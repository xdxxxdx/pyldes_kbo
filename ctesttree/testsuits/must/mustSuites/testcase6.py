# TODO


# SPEC for Tree Spec
# Must test case - 17
# SPEC Conform:
# When no tree:path is defined,
# the tree:value MUST be compared to all members’ triples that can be compared to the tree:value as defined by the
# type of the relation (or when no members or collection are defined, on every triple in the page). When due to
# rdfs:range incompatibility, the object cannot be compared, the object will not be considered for comparison.
#
# Verify:
# All member triple objects on the page containing the relationship that can be compared to the specified
# tree:value satisfy the relationship. Objects that cannot be compared to the relationship value are not considered
# for comparison.
#
# Question posed to tress spec:Is it possible ingest only tree:value not tree:path ?
class MustTestCase6:

    def get_result(self):
        return "UNDEFINED"