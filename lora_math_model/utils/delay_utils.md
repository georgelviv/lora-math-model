```latex
\mathrm{DELAY} =
\bigl( \mathrm{base}_{SF}
      + \mathrm{perByte}_{SF} \cdot L \bigr)
\cdot
\mathrm{bw\_scale}
\cdot
\mathrm{cr\_scale}
```


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

```latex
RTOA =
\begin{cases}
TOA + 8 \cdot \dfrac{2^{SF}}{BW} \cdot 10^{3}, & SF \geq 7, \\[6pt]
TOA + 31.8, & SF = 6.
\end{cases}
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
