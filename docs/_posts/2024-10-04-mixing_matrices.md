---
layout: post
title: "How do mixing matrices work?"
author: "Duncan J. Watts"
categories: journal
tags: [documentation,sample]
<!--image: mountains.jpg-->
---


Something I have been asked about for a while is how "mixing matrices" work. What is that? Fundamentally, in creating a model of the sky, we maps of "components", $\boldsymbol a_c$, and they get transformed into maps at certain detectors, $\boldsymbol m_b$.

In equation form, we could write this as
$$
\boldsymbol m=\mathsf M\boldsymbol a+\boldsymbol n_b
$$
The simplest way to do this, and therefore the way I will do it, is to assume that all maps are at the same resolution, and are pixelized in the same way. So to be extremely explicit, the equation above applies to only one pixel at a time, a generalization of this which is beyond the scope of this note, which I'm writing on a Friday afternoon.

$$
\begin{pmatrix}
m_1\\
m_2
\\
\vdots
\\
m_{n_b}
\end{pmatrix}
=
\begin{pmatrix}
f_1(\nu_1) & f_2(\nu_1) & \cdots & f_{n_c}(\nu_1)
\\
f_1(\nu_2) & f_2(\nu_2) & \cdots & f_{n_c}(\nu_2)
\\
\vdots
\\
f_1(\nu_{n_b}) & f_2(\nu_{n_b}) & \cdots & f_{n_c}(\nu_{n_b})
\end{pmatrix}
\begin{pmatrix}
a_1\\
a_2\\
\vdots\\
a_{n_c}
\end{pmatrix}
+
\begin{pmatrix}
n_1\\ n_2
\\
\vdots
\\
n_{n_b}
\end{pmatrix}
$$
$
=
\begin{pmatrix}
a_1f_1(\nu_1) +a_2f_2(\nu_1) + \cdots + a_{n_c}f_{n_c}(\nu_1)
+n_1
\\
a_1f_1(\nu_2) + a_2f_2(\nu_2) + \cdots + a_{n_c}f_{n_c}(\nu_2)
+n_2
\\
\vdots
\\
a_1f_1(\nu_{n_b}) + a_2f_2(\nu_{n_b}) + \cdots + a_{n_c}f_{n_c}(\nu_{n_b})
+n_{n_b}
\end{pmatrix}
$$

So this is really just basic SED fitting. The mixing matrix basically is a series of functions that give the expected contribution of a component at a certain band. For example, we often assume that synchrotron emission is given by a power law, so we would write
$$
f_\mathrm{sync}(\nu)=\left(\frac\nu{\nu_0}\right)^{\beta_\mathrm s}.
$$
This could be easily expanded to arbitrary components.


One key point here is that we are taking the parameters of the SED as known. Fitting for $\beta_{\mathrm s}$, for example, requires nonlinear optimization, and can be a bit nasty. But if we don't assume this, then $\mathsf M$ is just a simple array of numbers, and we can use standard linear algebra. If you can afford to be lazy, $\mathtt{np.linalg.solv(M,m)}$ will work just fine for you. But often we want to sample, so let's do that.

The maximum likelihood solution is the equation that minimizes $(\boldsymbol m-\mathsf M\boldsymbol a)^T\mathsf N^{-1}(\boldsymbol m-\mathsf M\boldsymbol a)$, or
$$
(\mathsf M^T\mathsf N^{-1}\mathsf M)\hat{\boldsymbol a}=
\mathsf M^T\mathsf N^{-1}\boldsymbol m
$$
In principle, pretty easy. $\mathsf M^T\mathsf N^{-1}\mathsf M)\hat{\boldsymbol a}$ is an $n_c\times n_c$ matrix. $n_c$ is in practice on the order of 10, so not too much of a computational issue.

As always though, being Gibbs samplers, we want to draw samples rather than just get the maximum likelihood solution. In that case, we solve the modified equation
$$
(\mathsf M^T\mathsf N^{-1}\mathsf M)\hat{\boldsymbol a}=
\mathsf M^T\mathsf N^{-1}\boldsymbol m
+\mathsf M^T\mathsf N^{1/2}\boldsymbol\eta
$$
and if you want to add some sort of prior $\mathsf N(\boldsymbol\mu,\mathsf S)$, the equation gets modified to
$$
(\mathsf S^{-1}\mathsf M^T\mathsf N^{-1}\mathsf M)\hat{\boldsymbol a}=
\mathsf M^T\mathsf N^{-1}\boldsymbol m
\mathsf S^{-1}\boldsymbol\mu
+\mathsf M^T\mathsf N^{1/2}\boldsymbol\eta_1
+\mathsf S^{-1/2}\boldsymbol\eta_2.
$$


I think one of the main utilities of the mixing matrices is its ability to smooth calculations when things get a bit more complicated. For instance, you don't actually observe at a single frequency, you observe with a bandpass $\tau(\nu)$ that is integrated over. In this case, the elements of the mixing matrix are
$$
\mathsf M_{ij}=\int\,\mathrm d\nu\,\tau_i(\nu) f_{j}(\nu\mid\theta).
$$
The really neat thing here is that each mixing matrix element is a continuous function of whatever parameters you are including in $f_{i}(\nu\mid\theta)$, like $\beta_\mathrm s$ for example. If you're smart, you precompute the mixing matrix at a few parameter values and interpolate over them if the parameters change.
