import numpy as np

"""
Function line_intersection returns the point P(x,y) where two given lines intersect.
The lines are given by their endpoints.
"""

def perp(a) :
    b = np.empty_like(a)
    b[0] = -a[1]
    b[1] = a[0]
    return b


def line_intersection(a1,a2, b1,b2) :
    # TODO: Check: √
    da = a2-a1
    db = b2-b1
    dp = a1-b1
    dap = perp(da)
    denom = np.dot( dap, db)
    num = np.dot( dap, dp )

    if denom.astype(float) == 0:
        return (False, False)
    res = (num / denom.astype(float))*db + b1

    return res

# p1 = np.array( [0.0, 0.0] )
# p2 = np.array( [1.0, 0.0] )
#
# p3 = np.array( [4.0, -5.0] )
# p4 = np.array( [4.0, 2.0] )
#
#
# print line_intersection( p1,p2, p3,p4)

