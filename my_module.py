def test(ctx, x, a, b, c, d, e):
	print "Hello, I am in module"
	print x, a, b, c, d, e
	ctx.setVariable('y', e + 3)