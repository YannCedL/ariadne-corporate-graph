# test du moteur de graphe d'actionnariat
from ariadne_corporate_graph.graph import build_company_graph

def test_construction_graphe_airbus():
    contract = build_company_graph("airbus")
    assert contract is not None
    assert contract.result["total_nodes"] >= 3
    assert contract.result["total_edges"] >= 2
    assert len(contract.evidence) >= 1
