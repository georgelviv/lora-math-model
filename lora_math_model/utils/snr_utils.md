```latex
\mathrm{SNR} = RSSI - N
```

```latex
N_{\mathrm{thermal}}(B) =
-174 \;+\; 10\log_{10}(B) \;+\; NF
```

```latex
N_{\mathrm{env}}^{125}(\mathrm{area}) =
\begin{cases}
-97, & \mathrm{rural}, \\
-90, & \mathrm{suburban}, \\
-85, & \mathrm{urban}, \\
-82, & \mathrm{large\text{-}urban}, \\
-90, & \mathrm{default}.
\end{cases}
```


```latex
N_{\mathrm{env}}(B,\mathrm{area}) =
N_{\mathrm{env}}^{125}(\mathrm{area})
\;+\;
10\log_{10}\!\left(\frac{B}{125000}\right)
```

```latex
N = N_{\mathrm{env}}
    + \max\!\bigl(0,\, 20 + RSSI \bigr)
    + \mathcal{N}(0, \sigma^{2})
```