---
layout: post
title: "Why didn't that iPhone braek?"
author: "Duncan J. Watts"
categories: journal
tags: [documentation,sample]
<!--image: mountains.jpg-->
---


After getting asked by a friend of a friend how an iPhone could survive falling from an airplane, I got a little curious, because it's a problem that can get arbitrarily difficult the more you think about it. Roughly speaking, introductory physics gives you all of the answers, just requires judicious use of Newton's second law, $F=ma$.

So the first question, how fast would an object falling be moving once it hit the ground? Assuming uniform gravity, we get

$$
m\ddot y=-mg
$$

$$
\dot y=v_{0,y}-gt
$$

$$
y=y_0+v_{0,y}t-gt^2/2
$$

Doing a little algebra, and using that $t=mv/g$, we get a nice equation connecting the height and the velocity;

$$
y=y_0-\frac12 v^2/g
\Rightarrow
v=\sqrt{2g(y_0-y)}
$$

Plugging this into <a href="https://www.wolframalpha.com/input?i=sqrt%282*gravitational+acceleration*16000+feet%29">WolframAlpha</a> gives 700 miles per hour. This is weird for a couple of reasons, one that the mass of the falling object didn't matter, and another that this not how fast normal things hit the ground, including, for example, raindrops.



The first thing a physicist will try to fix is adding air resistance, or drag. This just requires modifying Newton's second law;

$$
m\ddot y=F_{\mathrm{gravity}}+F_{\mathrm{drag}}
$$

Usually we assume that drag at high velocities is given by $F_D = \frac12\rho v^2 C_d A$, where $C_d$ is the "drag coefficient", which is basically a fudge factor that takes into account the shape of the object, $A$ is the projected area of the object, and $\rho$ is the density of the air itself. Newton's law therefore gives

$$
\ddot y=\frac12\rho v^2 nC_d A/m-g
$$
