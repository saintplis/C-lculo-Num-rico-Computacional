def bissec(xa, xb, ep1, ep2, nMax, f):
	k = 0
	xm = 0.5 * (xa + xb)
	print(
	    '********Metodo de bissecção********\n k|    xm   | abs(xb-xa)| f(xm) '
	)
	while (k < nMax) and (abs(xb - xa) > ep1) and (abs(f(xm)) > ep2):
		k = k + 1
		xm = 0.5 * (xa + xb)
		print(f'{k:2d}| {xm:.5f} |  {abs(xb - xa):.5f}  | {f(xm):.5f}')
		if f(xa) * f(xm) < 0:
			xb = xm
		else:
			xa = xm
	return xm, k


def falsaPosicao(xa, xb, ep1, ep2, nMax, f):
	k = 0
	xm = (xa * f(xb) - xb * f(xa)) / (f(xb) - f(xa))
	print(
	    '*******Metodo da Falsa Posição*******\n k|   xm   | abs(xb-xa)|  f(xm)   '
	)
	while (k < nMax) and (abs(xb - xa) > ep1) and (abs(f(xm)) > ep2):
		k = k + 1
		xm = (xa * f(xb) - xb * f(xa)) / (f(xb) - f(xa))
		print(f'{k:2d}| {xm:.5f}| {abs(xb-xa):.5f}   | {f(xm):.5f}')
		if f(xa) * f(xm) < 0:
			xb = xm
		else:
			xa = xm
	return xm, k


def newtonRaphson(x0, ep1, ep2, nMax, f, f1):
	k = 0
	x = x0 - f(x0) / f1(x0)
	print(
	    '***********Metodo de Newton-Raphson***********\n k|    xm   | abs(x-x0)|   f(x)  |   f1(x)  '
	)
	while (k < nMax) and (abs(x - x0) > ep1) and (abs(f(x)) > ep2):
		x0 = x
		k = k + 1
		x = x0 - f(x0) / f1(x0)
		print(f'{k:2d}| {x:.5f} | {abs(x-x0):.5f}  | {f(x):.5f} | {f1(x):.5f}')
	return x, k
