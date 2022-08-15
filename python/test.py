
def box_volume(a,b,c):
    try:
        a,b,c = float(a), float(b), float(c)
        v = a * b * c
    except:
        print('There is an error in the scripts')
    return v

from math import isclose

def test_box_volume():
    assert isclose(box_volume(1,1,1), 1)
    assert isclose(box_volume(5,10,20), 1000)
    assert isclose(box_volume(2.0,4.0,6.0), 48.0)
    assert isclose(box_volume(55.12,39.44,92.1254), 200274.42877311996)

test_box_volume()
print(box_volume(14,4,10))
print('Works')