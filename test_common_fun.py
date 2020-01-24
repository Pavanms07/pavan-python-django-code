from common_func import linear_search

def test_key_present_ls():
    l=[10,20,30,40,50,60]
    key=70
    result=linear_search(l,key)
    assert False==result
    
def test_key_not_present_ls():
    l=[10,20,30,40,50,60]
    key=40
    result=linear_search(l,key)
    assert False ==result