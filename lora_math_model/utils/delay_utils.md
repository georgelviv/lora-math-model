```latex
\mathrm{TOA}_{\mathrm{total}} =
\Bigl( \mathrm{base}_{SF}
     + \mathrm{slope}_{SF} \cdot L \Bigr)
\cdot \frac{500{,}000}{B}
\cdot \frac{CR}{8}
\;+\;
(p - 10)\,
\frac{2^{SF}}{B}\cdot 1000
```

## Datasheet ToA
\begin{equation}
T_s = \frac{2^{SF}}{BW}
\end{equation}

\begin{equation}
T_{\text{preamble}} =
\left(N_{\text{preamble}} + 4.25\right) \cdot T_s
\end{equation}

\begin{equation}
N_{\text{payload}} =
8 +
\max \left(
\left\lceil
\frac{
8PL - 4SF + 28 + 16CRC - 20IH
}{
4(SF - 2DE)
}
\right\rceil
\cdot (CR + 4),
\; 0
\right)
\end{equation}

\begin{equation}
T_{\text{payload}} = N_{\text{payload}} \cdot T_s
\end{equation}

\begin{equation}
TOA = T_{\text{preamble}} + T_{\text{payload}}
\end{equation}
