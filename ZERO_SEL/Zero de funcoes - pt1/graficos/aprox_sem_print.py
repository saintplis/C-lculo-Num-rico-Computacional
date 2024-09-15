def bissec(xa, xb, ep1, ep2, nMax, f):
    xm = 0
    k = 0
    xm = 0.5 * (xa + xb)
    while (k<nMax) and (abs(xb-xa) > ep1) and (abs(f(xm)) > ep2):
        k = k + 1
        xm = 0.5 * (xa + xb)
        if f(xa) * f(xm) < 0:
            xb = xm
        else:
            xa = xm
    
    return xm, k

def falsaPosicao(xa, xb, ep1, ep2, nMax, f):
    xm = 0
    k = 0
    xm = (xa*f(xb) - xb*f(xa)) / (f(xb) - f(xa))
    while (k<nMax) and (abs(xb-xa) > ep1) and (abs(f(xm)) > ep2):
        k = k + 1
        xm = (xa*f(xb) - xb*f(xa)) / (f(xb) - f(xa))
        if f(xa) * f(xm) < 0:
            xb = xm
        else:
            xa = xm
    
    return xm, k

def newtonRaphson(x0, ep1, ep2, nMax, f, f1):
    x = 0
    k = 0
    x = x0 - f(x0) / f1(x0)
    while (k < nMax) and (abs(x-x0) > ep1) and (abs(f(x)) > ep2):
        x0 = x
        k = k + 1
        x = x0 - f(x0) / f1(x0)
    
    return x, k
        
    