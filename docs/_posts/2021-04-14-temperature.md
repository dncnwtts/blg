---
layout: post
title: "What is 'CMB Temperature'?"
author: "Duncan J. Watts"
categories: journal
tags: [documentation,sample]
<!--image: mountains.jpg-->
---


## What are temperatures?

Going to figure out math here, but the basic idea is to show why CMB fluctuations do not have the same SED as a blackbody.

To the best of our knowledge, the CMB is a blackbody, whose spectral energy distribution (SED) is given by

$$ B_\nu(T)=\frac{2h\nu^3}{c^2}\frac1{e^{h\nu/kT}-1} $$

A few Nobel prizes ago, we discovered that the CMB is basically a monopole with $T_0=2.7275\,\mathrm K$, plus a dipole of order 3.5 mK, and primordial fluctuations on order of $100\,\mathrm{\mu K}$. To the physicist brain, this is a perfect opportunity to Taylor expand, while the astronomer brain recognizes that monopoles are really hard to measure, so we probably want to look at fluctuations anyway. Therefore, it makes more sense to look at the SED 

$$ B_\nu(T_0+\Delta T)\simeq B_\nu(T_0)+\frac{\partial B_\nu}{\partial T}\Delta T. $$

Now this is where things get a little tricky. To make mathematical models, we tend to want to deal with the physical underlying quantities, in this case, $\Delta T$, the fluctuation, in kelvin, about a blackbody $T_0$. But we also want to make measurements, which requires a some kind of prediction of how much power lands on our detector.

So a natural question becomes then, if we have an anistropy of size $\Delta T$, what will its specific intensity be at a frequency $\nu$?

The obvious answer is that, $B_\nu(T_0+\Delta T)$, a blackbody. But of course, we tend to subtract the monopole when making observations just because it is such a difficult quantity to measure, so really what we are measuring is

$$ B_\nu(T_0+\Delta T) - B_\nu(T_0)\simeq\frac{\partial B_\nu}{\partial T}\Delta T. $$

This means that for a single anisotropy brightness, the spectrum is given by

$$ \frac{\partial B_\nu}{\partial T}=\frac{2h\nu^3}{c^2}
\frac{e^{h\nu/kT}}{(e^{h\nu/kT}-1)^2}\frac{h\nu}{kT^2}. $$

This is a sort of weird position, because we want to report fluctuations with respect to the CMB at every frequency, so cosmologists often use units called $\mathrm{K_{CMB}}$, which leave the anisotropies constant over all frequencies. This is weirder than it might seem at first.
