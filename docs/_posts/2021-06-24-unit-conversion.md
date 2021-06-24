---
layout: post
title: "How do unit conversions work?"
author: "Duncan J. Watts"
categories: journal
tags: [documentation,sample]
<!--image: mountains.jpg-->
---


My chemistry teacher, Mr. David Walsh, once said "Let the units be your guide," and I honestly still follow that advice. At some level, you know that if you want a temperature and you have an energy, the Boltzmann constant must be involved, because it has units of Joules per kelvin.

In the real world, things get harder. Who knew?

As was described completely in 10.1051/0004-6361/201321531, you have to take into account the instrument when you are doing unit conversions, since you generally assume some calibration when you make a measurement. I got confused, so I'm writing this up.

If there is a source with specific intensity $I_\nu$ and the instrument has a bandpass $\tau(\nu)$ such that $\int\,\mathrm d\nu\,\tau(\nu)=1$, then the power that the experiment receives per second (or flux) is $\int\,\mathrm d\nu\,\tau(\nu)\,I_\nu$.

Generally though, we try to convert the data into some more physical quantity, say temperature or specific intensity, and say how much energy per interval in that quantity actually reached the detector. Essentially, the total energy per unit, $X_i$, becomes

$$
\int\,\mathrm d\nu\,\tau(\nu)\frac{dI_\nu}{dX_i}.
$$

So that's the total energy binned in $dX_i$.

Part of where I get confused by this is that you have to make a choice that may not actually correspond to the "right answer" before you report your answer. But of course, units are just a convention, so we must have the total energy per frequency bin be the same per unit conversion; if you use $X_i$ and $X_j$, the answer should physically be the same;

$$
dI_\nu=\frac{dI_\nu}{dX_i}\,\mathrm dX_i=\frac{dI_\nu}{dX_j}\,\mathrm dX_j.
$$

At the end of the day then, if you want to convert from units $X_i$ to units $X_j$, you must multiply by the conversion factor 

$$
\frac{dX_i}{dX_j}
=\frac{\int \mathrm d\nu\,\tau(\nu)\frac{dI_\nu}{dX_j}}{\int\,\mathrm d\nu\,\tau(\nu) \frac{dI_\nu}{dX_i}}.
$$

Pleasantly enough, this has the expected behavior if you replace $\tau(\nu)$ with a Dirac delta function bandpass $\delta(\nu-\nu_0)$.


This is so simple that it kind of gets confusing. So let's try and be explicit, and bear with me, those who are actually trying to learn something.

One convention that people use is the IRAS convention, defined such that $\nu\,\mathrm dI_\nu$ is constant, or that you have some emission $I_\nu=I_c(\nu_c/\nu)$, such that you're referencing the value at some reference frequency. Therefore, if you want to look at the specific intensity per $I_c$, you need to use $dI_\nu/dI_c=\nu_c/\nu$.


Another convention people use is $\mathrm{K_{CMB}}$, where you assume that your emission is due to the CMB, and you want to look at the fluctuations as a function of the actual CMB temperature. As I showed in a previous post, with a blackbody $B_\nu$, you want to see how much energy is being emitted per $T_\mathrm{CMB}$, so we get the amount of energy per bin

$$
b_\nu'\equiv \frac{\partial B_\nu}{\partial T_\mathrm{CMB}}
=\frac{2h\nu^3}{c^2}\frac{e^{h\nu/kT_\mathrm{CMB}}}{(e^{h\nu/kT_\mathrm{CMB}}-1)^2}\frac{h\nu}{kT_\mathrm{CMB}^2}.
$$

It is worth mentioning something about the units here; $dI_\nu/dI_c$ is unitless, whereas $dI_\nu/dT_\mathrm{CMB}$ has units of $\mathrm{MJy\,sr^{-1}\,K_{CMB}^{-1}}$. If we are to let the units be our guide, then you would imagine wanting to multiplying a quantity with units of $K_\mathrm{{CMB}}$ with something that's a function of $b_\nu'$ to get it into $|mathrm{MJy\,sr^{-1}}$.

With this all done, we have successfully put ourselves in a position to reproduce Equation (32) of Planck IX 2013;

$$
\frac{dX_\mathrm{IRAS}}{dX_\mathrm{CMB}}
=
\frac{\int\,\mathrm d\nu\,\tau(\nu)\,b_\nu'}
{
\int\,\mathrm d\nu\,\tau(\nu)\,(\nu_c/\nu)
}
$$

This gives us the "color correction", "bandpass coefficient", or something, $U(\mathrm{K_{CMB}}\to\mathrm{MJy\,sr^{-1}})$, that will take a map that has been calibrated in thermodynamic CMB units to the IRAS convention, after taking into account the bandpass.
