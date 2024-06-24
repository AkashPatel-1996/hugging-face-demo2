from app import greet

def test_greet_file():
    data = greet("akash")
    assert data == "Name is akash"