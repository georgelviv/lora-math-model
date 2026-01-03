```latex
RSSI(d, SF) = RSSI_{\text{phys}}(d) + b(SF)
```

```latex
RSSI = P_{\text{TX}} - PL + X_{\text{sh}} + F_{\text{fading}}
```

```latex
PL_{\mathrm{FS}}(d,f) =
20 \log_{10}(d) +
20 \log_{10}(f) - 147.55
```

```latex
PL = PL_{\mathrm{Hata}}(d, f, h_b, h_m, \mathrm{area})
```

```latex
X_{\sigma} \sim \mathcal{N}(0, \sigma^{2})
```

```latex
F_{\text{Rayleigh}} = 20 \log_{10}(R), 
\qquad
R \sim \mathrm{Rayleigh}(1).
```

```latex
RSSI_{\text{chip}} =
P_{\text{TX}}
- PL_{\text{Hata}}(d, f, h_b, h_m, \text{area})
+ X_{\sigma}
+ F_{\text{Rayleigh}}
+ \left( 1.5 + 0.7\,(SF - 7) \right)
```

```latex
RSSI_{\text{chip}} = RSSI_{\text{phys}} + b(SF)
```

```latex
b(SF) = 1.5 + 0.7\,(SF - 7)
```