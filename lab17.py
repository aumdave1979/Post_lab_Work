import sympy as sp

def Z_transform_of_exponential():
    n,z =sp.symbols('n z')
    x_n =3**n*sp.Heaviside(n)
    X_z =sp.summation(x_n*z**(-n),(n, 0, sp.oo))
    print("Z-transform of x[n] = 3^n u[n]:",sp.simplify(X_z))

def z_transform_of_cosine():
    n,z,w =sp.symbols('n z w')
    x_n =sp.cos(w*n)*sp.Heaviside(n)
    X_z =sp.summation(x_n*z**(-n),(n,0,sp.oo))
    print("Z-transform of x[n] = cos(wn)u[n]:",sp.simplify(X_z))


z_transform_of_cosine()