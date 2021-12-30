from final_project import main, open_file, find_word, proclamation, gettysburg, wrecked
import pytest

def test_open_file():
    assert open_file("proclamation.txt") == '1'
    assert open_file(2) == "gettysburg.txt"
    assert open_file(3) == "wrecked.txt"


'''
def test_extract_given_name():    
    assert extract_given_name(", ") == ""
    assert extract_given_name("Brown, Sally") == "Sally"
    assert extract_given_name("Juarez, Luke") == "Luke"
    assert extract_given_name("Dynamite, Napoleon") == "Napoleon"
    assert extract_given_name("Green, Cee-Lo") == "Cee-Lo"

# Call the main function that is part of pytest so that
# the test functions in this file will start executing.
'''

pytest.main(["-v", "--tb=line", "-rN", "final_project.py"])