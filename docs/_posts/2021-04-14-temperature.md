---
layout: post
title: "What is 'CMB Temperature'?"
author: "Duncan J. Watts"
categories: journal
tags: [documentation,sample]
<!--image: mountains.jpg-->
---

To the best of our knowledge, the CMB is a blackbody, whose spectral energy distribution (SED) is given by

$$ B_\nu(T)=\frac{2h\nu^3}{c^2}\frac1{e^{h\nu/kT}-1} $$

A few Nobel prizes ago, we discovered that the CMB is basically a monopole with $T_0=2.7275\,\mathrm K$, plus a dipole of order 3.5 mK, and primordial fluctuations on order of $100\,\mathrm{\mu K}$. To the physicist brain, this is a perfect opportunity to Taylor expand, while the astronomer brain recognizes that monopoles are really hard to measure, so we probably want to look at fluctuations anyway. Therefore, it makes more sense to look at the SED 

$$ B_\nu(T_0+\Delta T)\simeq B_\nu(T_0)+\frac{\partial B_\nu}{\partial T}\Delta T. $$

Now this is where things get a little tricky. To make mathematical models, we tend to want to deal with the physical underlying quantities, in this case, $\Delta T$, the fluctuation, in kelvin, about a blackbody $T_0$. But we also want to make measurements, which requires a some kind of prediction of how much power lands on our detector.

So a natural question becomes then, if we have an anistropy of size $\Delta T$, what will its specific intensity be at a frequency $\nu$?

The obvious answer is that, $B_\nu(T_0+\Delta T)$, a blackbody. But of course, we tend to subtract the monopole when making observations just because it is such a difficult quantity to measure, so really what we are measuring is

$$ B_\nu(T_0+\Delta T) - B_\nu(T_0)\simeq\frac{\partial B_\nu}{\partial T}\Delta T. $$

This means that for a single anisotropy brightness, the spectrum is given by

$$
\frac{\partial B_\nu}{\partial T}=\frac{2h\nu^3}{c^2}
\frac{e^{h\nu/kT}}{(e^{h\nu/kT}-1)^2}\frac{h\nu}{kT^2}.
$$

This is a sort of weird position, because we want to report fluctuations with respect to the CMB at every frequency, so cosmologists often use units called $\mathrm{K_{CMB}}$, which leave the anisotropies constant over all frequencies. This is weirder than it might seem at first.

The main thing that I had forgotten is that *the CMB is a blackbody* but *the fluctuations are not blackbodies*. It might seem a bit obvious, but while we often look at maps of the CMB fluctuations, those are not the physical photons that we are looking at, so these mathematical conveniences no longer are governed by the well-known Planck SED $B_\nu(T)$.

```python
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
```

![Anisotropy scaling](https://raw.githubusercontent.com/dncnwtts/blg/gh-pages/docs/assets/img/dBdT.png)
