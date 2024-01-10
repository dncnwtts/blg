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
\ddot y=\frac12\rho v^2 C_d A/m-g
$$


This is a hard enough equation to solve that I'm going to put it off for a moment, but the main thing to notice is that there is a special velocity where the acceleration is zero;

$$
v=\sqrt{\frac{2mg}{\rho C_d A}}
\propto\sqrt{\frac{m}{A}}
$$


My claim that I'm going to leave unproven right now is that this is the velocity that an object would hit the ground. This actually kind of comports with our intuition, that the object's terminal velocity will be higher if it weighs more, and it will be moving slower if it has a larger area (think of a flying squirrel or a parachute).


Again, I'm too lazy to do the actual algebra, but <a href="https://www.wolframalpha.com/input?i=sqrt%282*+130+grams*gravitational+acceleration%2F%28air+density*6.33+inches*3.07+inches%29%29">WolframAlpha</a> gives about 28 mph, where I've just assumed $C_d=1$ and an iPhone 14 pro that is flat. The actual answer isn't going to be that much different.

I can do the same thing assuming that I'm (ahem) 100 kg, 6 feet tall, and 15 inches wide, giving 100 miles per hour. These aren't so far off from the reported answers I've found online, and the fact that people can get twice as fast isn't that surprising to me.


One of the reasons that we have to get in the details a bit is that, using the same equation in the first part, an iPhone dropped from waist height has a speed of about 10 mph when it hits the ground, only three times slower than the one falling out of the plane.

I also know from personal experience that _sometimes_ an iPhone will be undamaged when dropped on the ground, and _sometimes_ the screen will crack. I don't think I've heard of an iPhone actually _breaking_ from a fall, and I'm not sure that it would happen. Materials physics is clearly difficult! I think the fact that modern phones are trying to be as light and large as possible is both making air resistance help from long falls, while also making them more damage-prone. There are clearly many things happening here.
