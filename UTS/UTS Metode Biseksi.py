def bisection(f, p, q, e=0.5, N = 100):
  x_p = p
  x_q = q
  
  if f(x_p)*f(x_q) >= 0:
    print("Use another guess range")
    return None
  
  for n in range (1,N):
    x_m = (x_p + x_q)/2
    if abs(f(x_m)) < e:
      return x_m, n
    else:
      if f(x_p)*f(x_m) < 0:
        x_q = x_m
      elif f(x_q)*f(x_m) < 0:
        x_p = x_m
  return x_m, n

f = lambda x: 2*x**3-4*x**2-24
p = 2
q = 9

x_root, iteration = bisection(f,p,q)
print('Result : ',"%.4f" % x_root)
print('In %d iteration' %iteration)