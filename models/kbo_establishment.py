from datetime import datetime
from typing import List

from pyldes_kbo.models.kbo_address import KboAddress
from pyldes_kbo.models.kbo_base import KboBase
from pyldes_kbo.models.kbo_contact import KboContact
from pyldes_kbo.namespace.kbo import KBO
from pyldes_kbo.namespace.locn import LOCN
from pyldes_kbo.namespace.termname import TERMNAME
from rdflib import Graph, URIRef, Literal, BNode, RDF, ORG, XSD


class KboEstablishment(KboBase):

    def __init__(self):
        self.estblishment_number: str = None
        self.start_date: datetime = None
        self.enterprise_number: datetime = None
        self.contacts: List[KboContact] = None
        self.addresses: List[KboAddress] = None

    def to_rdf(self, graph: Graph, as_blank_node: bool = False) -> URIRef:
        if as_blank_node:
            establihment_ref = BNode()
        else:
            establihment_ref = URIRef(f"{KBO._NS}{self.estblishment_number.replace('.', '')}")
        graph.add((establihment_ref, RDF.type, ORG.Site))
        graph.add((establihment_ref, RDF.type, KBO.Establishment))
        graph.add((establihment_ref, TERMNAME.issued,
                   Literal(datetime.strptime(self.start_date, '%d-%m-%Y').strftime('%Y-%m-%d'), datatype=XSD.date)))
        for address in self.addresses:
            addr_ref = address.to_rdf(graph, as_blank_node=as_blank_node)
            graph.add((establihment_ref, LOCN.Address, addr_ref))
        for contact in self.contacts:
            contact.load_entity_contact(graph, establihment_ref)
        return establihment_ref

    def to_rdf_version(self, graph: Graph, as_blank_node: bool = False) -> URIRef:
        if as_blank_node:
            establihment_ref = BNode()
        else:
            establihment_ref = URIRef(f"{KBO._NS}{self.estblishment_number.replace('.', '')}")
        graph.add((establihment_ref, RDF.type, ORG.Site))
        graph.add((establihment_ref, RDF.type, KBO.Establishment))
        graph.add((establihment_ref, TERMNAME.issued,
                   Literal(datetime.strptime(self.start_date, '%d-%m-%Y').strftime('%Y-%m-%d'), datatype=XSD.date)))
        for address in self.addresses:
            addr_ref = address.to_rdf_version(graph, as_blank_node=as_blank_node)
            graph.add((establihment_ref, LOCN.Address, addr_ref))
        for contact in self.contacts:
            contact.load_entity_contact(graph, establihment_ref)
        return establihment_ref
