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
\int\,\mathrm d\nu\,\tau(\nu)\frac{dI_\nu}{dX_i}
$$
So that's the total energy binned in $dX_i$.

Part of where I get confused by this is that you have to make a choice that may not actually correspond to the "right answer" before you report your answer. But of course, units are just a convention, so we must have the total energy per frequency bin be the same per unit conversion; if you use $X_i$ and $X_j$, the answer should physically be the same;
$$
dI_\nu=\frac{dI_\nu}{dX_i}\,\mathrm dX_i=\frac{dI_\nu}{dX_j}\,\mathrm dX_j
$$
