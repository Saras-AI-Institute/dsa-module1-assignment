import pytest
from assignment import analyze_text, manipulate_tuple_and_set, SimpleQueueADT, SimpleGraphADT

def test_analyze_text():
    text = "Data Structures"
    char_count, freq_map, unique_words = analyze_text(text)
    
    assert char_count == 15
    assert freq_map['D'] == 1
    assert freq_map['a'] == 2
    assert unique_words == ['data', 'structures']

def test_manipulate_tuple_and_set():
    sample_list = [1, 2, 2, 3, 1]
    res_tuple, res_set = manipulate_tuple_and_set(sample_list)
    
    assert isinstance(res_tuple, tuple)
    assert isinstance(res_set, set)
    assert len(res_set) == 3
    assert res_set == {1, 2, 3}

def test_queue_adt():
    q = SimpleQueueADT()
    assert q.is_empty() is True
    
    q.enqueue("A")
    q.enqueue("B")
    assert q.is_empty() is False
    
    assert q.dequeue() == "A"
    assert q.dequeue() == "B"
    
    with pytest.raises(IndexError):
        q.dequeue()

def test_graph_adt():
    g = SimpleGraphADT()
    g.add_vertex("A")
    g.add_edge("A", "B")
    g.add_edge("B", "C")
    
    assert "A" in g.graph
    assert g.get_neighbors("B") == {"A", "C"}
