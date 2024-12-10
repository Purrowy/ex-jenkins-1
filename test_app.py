from app import home

def test_home():
    result = home().split()[-1]
    assert float(result)