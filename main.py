
si=["775.5K","615","189K"]
for s in si:
    if "K" in s:
        cislo = float(s.replace("K", "")) * 1000
        
    elif "M" in s:
        pass
    else: cislo = float(s)
    print(cislo)