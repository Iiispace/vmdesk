from mathutils import Matrix

TRANSLATION = Matrix.Translation

def rf_linear_01(x0, x1):
    #| f(x) = Ax + b
    x1mx0 = x1 - x0
    if x1mx0 == 0: return lambda x: 0.0
    a = 1.0 / x1mx0
    b = - a * x0
    return lambda x: a * x + b
    #|

def rf_linear_01_inv(x0, x1):
    #| f(x) = Ax + b
    #| f(x), i(y)
    x1mx0 = x1 - x0
    if x1mx0 == 0: return lambda x: 0.0, lambda y: 0.0
    a = 1.0 / x1mx0
    if a == 0: return lambda x: a * x + b, lambda y: 0.0
    b = - a * x0
    return lambda x: a * x + b, lambda y: (y - b) / a
    #|

def rf_linear(x0, x1, y0, y1):
    #|
    x1mx0 = x1 - x0
    if x1mx0 == 0: return lambda x: 0.0
    a = (y1 - y0) / x1mx0
    b = y0 - a * x0
    return lambda x: a * x + b
    #|

def rf_linear_inv(x0, x1, y0, y1):
    #|
    x1mx0 = x1 - x0
    if x1mx0 == 0: return lambda x: 0.0
    a = (y1 - y0) / x1mx0
    if a == 0: return lambda x: a * x + b, lambda y: 0.0
    b = y0 - a * x0
    return lambda x: a * x + b, lambda y: (y - b) / a
    #|



# Vector, Quaternion, Vector
def r_compose(loc, rot, sca):
    #|
    return TRANSLATION(loc) @ rot.to_matrix().to_4x4() @ Matrix(
        ((sca[0],0,0,0), (0,sca[1],0,0), (0,0,sca[2],0), (0,0,0,1)))
    #|

def mat4_to_volume_scale(m):
    return (m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1]) -
        m[1][0] * (m[0][1] * m[2][2] - m[0][2] * m[2][1]) +
        m[2][0] * (m[0][1] * m[1][2] - m[0][2] * m[1][1]))
    #|
