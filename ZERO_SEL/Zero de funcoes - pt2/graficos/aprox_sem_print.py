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
