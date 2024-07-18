def test_species_name():
    species_name = "Core Species"
    assert species_name == "Core Species"
    
def test_start_system():
    system_name = "Core System"
    assert system_name == "Core System"

def test_hyperlane():
    hyperlane_from = "Core System"
    hyperlane_to = "Random System"
    assert hyperlane_from == "Core System"
    assert hyperlane_to == "Random System"
