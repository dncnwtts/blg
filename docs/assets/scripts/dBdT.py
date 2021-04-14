import matplotlib.pyplot as plt
import numpy as np
from astropy import units as u
from astropy import constants as c

def B(nu, T):
    A = 2*c.h*nu**3/c.c**2
    x = c.h*nu/(c.k_B*T)
    return A.si/np.expm1(x.si)

def dBdT(nu, T):
    x = c.h*nu/(c.k_B*T)
    A = 2*c.k_B*nu**2/c.c**2
    return A.si*x.si**2*np.exp(x.si)/np.expm1(x.si)**2

T0 = 2.7275*u.K
dT = 3.5*u.mK
nu = np.linspace(0, 1000)*u.GHz

plt.figure(figsize=(4,3))

plt.plot(nu, B(nu,T0), label=r'$B_\nu(T_0)$')
plt.plot(nu, B(nu,T0+dT)-B(nu,T0), label=r'$\Delta B_\nu$')
plt.plot(nu, dBdT(nu, T0)*dT.si,'k:', label=r'$\frac{\partial B_\nu}{\partial T}\Delta T$')

plt.yscale('log')
plt.legend(loc='best')
plt.xlabel(r'$\nu$ [GHz]')
plt.ylabel(r'Specific intensity [Jy/sr]')
plt.savefig('../img/dBdT.png', bbox_inches='tight')
