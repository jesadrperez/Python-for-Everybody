text = "X-DSPAM-Confidence:    0.8475";

idx = text.find('0')
num = text[idx:]
num = float(num)

print num