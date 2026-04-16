"""
Tests for Ariadne Corporate Graph engine
"""

from ariadne_corporate_graph import build_company_graph
from genesis_core import EpistemicStatus

def test_build_company_graph():
    contract = build_company_graph("383474814")
    assert contract.confidence > 0.9
    assert contract.result.get("total_nodes") >= 3
    assert len(contract.result.get("edges")) >= 2
    assert contract.evidence[0].status == EpistemicStatus.FACT
