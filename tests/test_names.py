from names import make_full_name, extract_given_name, extract_family_name
import pytest

def test_make_full_name():
    assert make_full_name("", "") == ";"
    assert make_full_name(" Sally", "Brown") == "Brown; Sally"
    assert make_full_name(" Luke", "Juarez") == "Juarez; Luke"
    assert make_full_name(" Napoleon", "Dynamite") == "Dynamite; Napoleon"
    assert make_full_name(" Cee-Lo", "Green") == "Green; Cee-Lo"

def test_extract_family_name():
    assert extract_family_name(", ") == ""
    assert extract_family_name("Brown, Sally") == "Brown"
    assert extract_family_name("Juarez, Luke") == "Juarez"
    assert extract_family_name("Dynamite, Napoleon") == "Dynamite"
    assert extract_family_name("Green, Cee-Lo") == "Green"

def test_extract_given_name():    
    assert extract_given_name(", ") == ""
    assert extract_given_name("Brown, Sally") == "Sally"
    assert extract_given_name("Juarez, Luke") == "Luke"
    assert extract_given_name("Dynamite, Napoleon") == "Napoleon"
    assert extract_given_name("Green, Cee-Lo") == "Cee-Lo"

# Call the main function that is part of pytest so that
# the test functions in this file will start executing.


pytest.main(["-v", "--tb=line", "-rN", "test_names.py"])