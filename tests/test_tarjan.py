from tarjan import tarjan
from collections import namedtuple

GRAPH_SCC_PAIRING = namedtuple('gscc_pair', ['graph', 'scc_set'])

def test_sanity():
    assert True


def test_trivial():
    assert tarjan({'A': []}) == [{'A'}]


# can't compare nested sets, so freeze em!
# this is quicker then generating permutations and testing for any.
def freeze_then_compare(set1, set2):
    frz1 = {frozenset(scc) for scc in set1}
    frz2 = {frozenset(scc) for scc in set2}
    return frz1 == frz2


def test_simple():
    g = [
        GRAPH_SCC_PAIRING(
            {'A': ['B'], 'B': ['A']},
            [{'A', 'B'}]),
        GRAPH_SCC_PAIRING(
            {'A': [], 'B': []},
            [{'A'}, {'B'}]),
        GRAPH_SCC_PAIRING(
            {
                1: [2, 3, 4, 5],
                2: [1, 3, 5],
                3: [1],
                4: [],
                5: [1, 2, 3, 4, 5],
            },
            [{1, 2, 3, 5}, {4}]),
    ]
    for gscc_pair in g:
        assert freeze_then_compare(tarjan(gscc_pair.graph), gscc_pair.scc_set)
