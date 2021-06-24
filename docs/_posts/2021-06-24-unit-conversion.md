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
