import tools.web_search as ws

def test_web_search():
    result = ws.web_search("who is sherlock holmes?")
    assert result