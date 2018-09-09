from path import find_num_paths

def test_num_paths():
    start = 2
    end = 2
    total_paths = find_num_paths(start, end)
    assert total_paths == 6

test_num_paths()
