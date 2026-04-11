import math

def toi_gian(tu, mau):
    u = math.gcd(tu, mau)
    return tu // u, mau // u

def cong(p1, p2):
    tu = p1[0] * p2[1] + p2[0] * p1[1]
    mau = p1[1] * p2[1]
    return toi_gian(tu, mau)

def tru(p1, p2):
    tu = p1[0] * p2[1] - p2[0] * p1[1]
    mau = p1[1] * p2[1]
    return toi_gian(tu, mau)

def nhan(p1, p2):
    tu = p1[0] * p2[0]
    mau = p1[1] * p2[1]
    return toi_gian(tu, mau)

def chia(p1, p2):
    tu = p1[0] * p2[1]
    mau = p1[1] * p2[0]
    return toi_gian(tu, mau)