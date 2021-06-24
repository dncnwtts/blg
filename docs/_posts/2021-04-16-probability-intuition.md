---
layout: post
title: "Why is probability hard?"
author: "Duncan J. Watts"
categories: journal
tags: [documentation,sample]
---


There's a kind of famous statistics example that is used to demonstrate Bayesian statistics, basically how likely is it that somebody has a disease given that they tested positive for the idea.

Say that in the population, an estimated 1% of people have a disease. Sort of a baseline probability, $P(d)=0.01$. Now let's pretend we have developed a test for the disease, and we estimated the accuracy of the test, so that there is a 99% chance that someone will test positive if they have the disease, and there is a 1% chance they will test positive if they don't have the disease.

The question then is as follows; given that somebody tests positive, what is the probability that they have the disease?

To answer this question, we use Bayes' Theorem,

$$ P(A\mid B)=\frac{P(B\mid A)P(A)}{P(B)}$$

where $P(A\mid B)$ is the probability of observing event A given event B is true, and $P(A)$ is the probability of event A in the entire universe of probability, i.e., the marginalized probability of event A.

With this, it's actually pretty simple to just plug and play;

$$ P(d\mid+)=\frac{P(+\mid d)P(d)}{P(+)}$$

We know that $P(+\mid d)=0.99$ and $P(d)=0.01$. The denominator, or the "evidence" as it's sometimes called, is given by

$$ P(+)=P(+\mid d)P(d)+P(-\mid \tilde d)P(\tilde d)=0.99\cdot0.01 + 0.01\cdot0.99=0.0198$$

Therefore,

$$ P(d\mid+)=\frac{0.99\cdot0.01}{2\cdot0.99\cdot0.01 }=0.5$$


So if you have a positive test for the disease, then you would say there is a 50% chance of you have the disease.

This is kind of a weird result; isn't the test 99% accurate? And there's only a 1% chance of you having a false positive? Why would that mean "I have a 50/50 chance of having this disease given my positive test?"

I know that there is stuff we can do to explain this result; what I'm more interested here in digging into why this is confusing, and why this flies against my intuition (and others, I suspect).


## First, explaining the result

The simple answer to why the result is so low is because of the prior. There is, a priori, a 1% chance of you having this disease, assuming that you've been randomly selected. The positive measurement takes your base probability $P(d)=0.01$ to $P(d\mid+)=0.5$, meaning that you're fifty times more likely to have the disease than you were before.

The denominator can be a bit confusing as well, but with just two possibilities, it might be easy to just do this brute force;

$$ P(d\mid+)=A\,P(+\mid d)P(d),\qquad P(\tilde d\mid +)=A\,P(+\mid\tilde d) P(\tilde d) $$

Since this is a binary choice, you either have the disease or you don't, we know that $P(d\mid+)+P(\tilde d\mid+)=1$. Given that, you could write

$$ P(\tilde d\mid+)=A\,P(+\mid\tilde d)P(\tilde d)=1-A\,P(+\mid d)P(d) $$

Most of these terms we know; $P(+\mid\tilde d)=0.01$, $P(\tilde d)=0.99$. Therefore, $P(+\mid d)P(d)=P(+\mid\tilde d)P(\tilde d)$, it's pretty easy to show that $A=2\cdot0.99\cdot0.01$.

So our consistency check seems good to me; $P(\tilde d\mid+)=0.5$ as well. But another interesting thing pops up here; $P(\tilde d)=0.99$, and $P(\tilde d\mid+)=0.5$. So this is kind of interesting; 99% means to me, I almost certainly don't have this disease, but now I have a 50% chance of not having the disease; you are now half as sure of your not having the disease.

Perhaps this is getting us in the right direction; a positive test means you are 50 times more likely to have the disease, and you are only half as likely to not have the disease.

### What if the test were negative?

Just for fun, let's consider the probability of having the disease given a negative test. (We'll also assume that the false negative statistics are the same.)

$$ P(d\mid-)=\frac{P(-\mid d)P(-)}{P(-\mid d)P(-)+P(-\mid\tilde d)P(\tilde d)} = \frac{0.01\cdot0.01}{0.01\cdot0.01+0.99\cdot0.99}=0.000102 $$

As expected, if you have a negative test, you are about 100 times less likely to have the disease. 

## A potential explanation

I think the thing that messes with our intuition is the prior. Assuming there is nothing special about you, you would assume, there is a very small chance I have this disease. I think the way my mind works is assigning a "flat prior" to the event ahead of time; I either have the disease or I don't, so the two have equal probabilities, right? Well if that were true, then yeah, we would indeed have 99% chance of having the disease given a positive test.

I think this kind of speaks to a deeper human bias; because two situations are being compared, they must be on somewhat equal footing, right? We wouldn't even be asking the question if we didn't think a priori that they are somehow of comparable prior probability.

This is kind of complicated by the way we usually deal with tests like this. I imagine most people don't go out of their way to get tested for diseases they have no reason to think they have; typically, a test for a disease follows an exposure event. In this case, the prior is different; you're not part of the general population, not just a random sample, and the probability of you having the disease is probably going to be higher than if you were randomly selected from the population at large.


This is probably something that's very obvious to statisticians, but I find it a bit confusing at times, and I think it has to do with this assumption of equal probabilities. If you are given a choice, both things have equal weight; a coin should be assumed fair.
