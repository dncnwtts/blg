---
layout: post
title: "How do I calculate noise bias?"
author: "Duncan J. Watts"
categories: journal
tags: [documentation,sample]
<!--image: mountains.jpg-->
---

Let's say we have a map with uniform Gaussian white noise. What is its power spectrum, and what is its uncertainty?

In order to be a bit more concrete, let's define some terms, and then we can decide if they are good assumptions or not later.

First, let's say that the noise in every pixel is drawn from a Gaussian distribution with mean zero and variance $\sigma_{p}^{2}$. Let's also assume that all pixels have the same size, $\Delta\Omega_{p}$. Finally, let's pretend that the true underlying sky map is known, a la Gibbs sampling.

In total, our sky map is going to look something like $d=s+n$ so that for every pixel,

$$
d_{p}\sim P(d_{p}\mid s_{p},\sigma_{p}^{2})=\mathcal{N}\left(s_{p},\sigma_{p}^{2}\right)
$$

The spherical harmonic transform of this map is given by

$$
d_{\ell m}=s_{\ell m}+n_{\ell m}
$$

where

$$
a_{\ell m}=\int d\Omega\,Y_{\ell m}\,a\simeq\sum_{p}\Delta\Omega_{p}Y_{\ell m}a_{p}.
$$

I am also using the “real” spherical harmonics here, just so that we don't have to deal with complex number statistics. Again, we are assuming $s_{\ell m}$ is known perfectly, but $n_{\ell m}$ is a Gaussian random field;

$$
n_{\ell m}=\sum_{p}\Delta\Omega_{p}Y_{\ell m}n_{p}.
$$

This is a Gaussian with mean zero, and a variance

$$
\langle n_{\ell m}^{2}\rangle=\sum_{pp'}\Delta\Omega_{p}\Delta\Omega_{p'}Y_{\ell m}(p)Y_{\ell m}(p')\,\left\langle n_{p}n_{p'}\right\rangle .
$$

Since we're assuming Gaussian, white noise, we have $\left\langle n_{p}n_{p'}\right\rangle =\delta_{pp'}\sigma_{p}^{2}$, so that

$$
\langle n_{\ell m}^{2}\rangle=\sum_{p}\Delta\Omega_{p}^{2}|Y_{\ell m}(p)|^{2}\sigma_{p}^{2}
$$

We can also assume that the $Y_{\ell m}$ are normalized such that 

$$
\int d\Omega\,|Y_{\ell m}|^{2}=\sum\Delta\Omega_{p}\,|Y_{\ell m}|^{2}=1,
$$
so that

$$
\langle n_{\ell m}^{2}\rangle=\Delta\Omega_{p}\sigma_{p}^{2}\equiv w^{-1}
$$
where w is the weight per pixel. 

To make a long story short;

$$
d_{\ell m}=s_{\ell m}+n_{\ell m}\sim\mathcal{N}\left(s_{\ell m},w^{-1}\right)
$$

Now for the actual power spectrum;

$$
\hat{C}_{\ell}=\frac{1}{2\ell+1}\sum_{m}\left(|s_{\ell m}|^{2}+|n_{\ell m}|^{2}+2s_{\ell m}n_{\ell m}\right)
$$

The first term is just the on-sky power spectrum, $\sigma_{\ell}$. The second term is the noise bias, and is proportional to a $\chi_{2\ell+1}^{2}$ distribution;

$$
\frac{1}{2\ell+1}\sum_{m}|n_{\ell m}|^{2}=\frac{w^{-1}}{2\ell+1}\sum_{m}|\eta|^{2}=\frac{w^{-1}}{2\ell+1}\chi_{2\ell+1}^{2}
$$

The final term is a bit more difficult, but still just a sum of Gaussians;

$$
\frac{2}{2\ell+1}s_{\ell m}n_{\ell m}\sim\mathcal{N}\left(0,\frac{4}{(2\ell+1)^{2}}s_{\ell m}^{2}w^{-1}\right)
$$

$$
\sum_{m}\frac{2}{2\ell+1}s_{\ell m}n_{\ell m}\sim\mathcal{N}\left(0,\frac{4w^{-1}}{(2\ell+1)^{2}}\sum_{m}s_{\ell m}^{2}\right)=\mathcal{N}\left(0,\frac{4w^{-1}}{2\ell+1}\sigma_{\ell}\right)
$$

So in principle, the power spectrum should be distributed as something like;
$$
\hat{C}_{\ell}=\sigma_{\ell}+\frac{w^{-1}}{2\ell+1}\chi_{2\ell+1}^{2}+\eta\sqrt{\frac{4w^{-1}}{2\ell+1}\sigma_{\ell}}.
$$

Since the mean of the $\chi^{2}_{2\ell+1}$ distribution is $2\ell+1$, the total power spectrum should be $\hat C_\ell=\sigma_\ell+w^{-1}$.

This $w^{-1}$ value is sort of useful, because CMB experiments often define the map sensitivity in terms of $w^{-1/2}$, which has units of temperature-angle, e.g., $\mathrm{\mu K\,arcmin}$. Therefore, if we want to estimate the noise bias power spectrum, $N_\ell$, we simply need to square the map sensitivity and convert it to $\mathrm{K^2\,sr}$.


```python
import matplotlib.pyplot as plt
import numpy as np
import healpy as hp
ell = np.arange(200)
Cl = np.zeros(len(ell))
Cl[2:] = 1.0 / ell[2:] ** 2
m = hp.synfast(Cl, 128)
sl = hp.anafast(m, lmax=ell.max())
n = np.random.randn(m.size)
clhat = hp.anafast(m+n, lmax=ell.max())
N_l = np.ones_like(ell)*hp.nside2pixarea(128)
Clhat_2 = sl + hp.nside2pixarea(128)*np.random.chisquare(2*ell+1)/(2*ell+1) + np.random.randn(ell.size)*np.sqrt(2*hp.nside2pixarea(128)*sl/(2*ell+1))
plt.loglog(ell[2:], Cl[2:] + N_l[2:])
plt.loglog(ell[2:], sl[2:], label=r'$\sigma_\ell$')
plt.loglog(ell[2:], N_l[2:], label=r'$N_\ell$')
plt.loglog(ell[2:], clhat[2:], label=r'$\hat C_\ell$')
plt.loglog(ell[2:], Clhat_2[2:], label=r'$\hat C_\ell^\mathrm{pred}$')
plt.xscale('linear')
plt.legend(loc='best')
plt.xlabel(r'$\ell$')
plt.ylabel(r'$C_\ell\,[\mathrm{K^2\,sr}]$')
plt.savefig('noise_bias.png', bbox_inches='tight')
```


![Example of simulated noise bias](https://raw.githubusercontent.com/dncnwtts/blg/gh-pages/docs/assets/img/noise_bias.png "Python plot")

