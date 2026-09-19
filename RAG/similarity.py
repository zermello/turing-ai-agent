""" 
the logic is from the cosine similarity formula
cosine similarity (a,b) = dot product (a.b) / (magnitude A (|A|) * magnitude B (|B|))
"""


from math import sqrt

def dot_product(a,b):
    no = 0

    for x,y in zip(a,b):
        no = no + (x*y)
    return no

def magnitude(vector):

    no = 0

    for i in vector:
        i = i**2
        no = no + i
    return (sqrt(no))

def cosine_similarity(a,b):
    dot = dot_product(a,b)
    mag_a = magnitude(a)
    mag_b = magnitude(b)

    return dot / (mag_a * mag_b)