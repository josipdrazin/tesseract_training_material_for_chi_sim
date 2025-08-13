from fontTools.ttLib import TTFont
import os, pathlib

pwd = os.getenv("PWD")
text = open(os.path.join(pwd, "trainer2.txt"), "r+")
lines=[ch for c in text.readlines() for ch in c]
#lines2 = ["".join(str(i) for i in [lines.pop(0) for i in range(100)]) for j in range(int(len(lines)/100))]
#lines2.append( "".join(str(i) for i in [lines.pop(0) for i in range(len(lines))]) )
fontdir=os.path.join(pwd, "fonts")
unicharset=os.path.join(pwd,"langdata/chi_sim.unicharset")
fonts=[os.path.join(dp, f) for dp, dn, fn in os.walk(os.path.join(pwd,"fonts")) for f in fn]
fonts=[y for y in fonts if (y.endswith(".otf") or y.endswith(".ttf"))]
fonts_trunc=[pathlib.Path(y).stem for y in fonts]
text.close()
compat_chars={pathlib.Path(k).stem : [] for k in fonts }

cincmap=False
# Example usage
for font in fonts:
	font_trunc=pathlib.Path(font).stem
	fnt = TTFont(font)
	for char in lines:
		cincmap=False
		for cmap in fnt['cmap'].tables:
			if ord(char) in cmap.cmap:
				cincmap=True
		if cincmap:
			compat_chars[str(font_trunc)].append(char)
		print(f"\r{font_trunc} - {char} - {lines.index(char)} / {len(lines)} ", end=" ", flush=True)

for k in compat_chars.keys():
	print(f"{k} -- {len(compat_chars[k])}") 
"""print(compat_chars.keys())
d={k : [len(list(set(lines)-set(compat_chars[k])))] for k in compat_chars.keys()}
m=[]
m= [len(v) for k,v in compat_chars.items()]
print(min(m))
m = list(d.keys())[m.index(min(m))]
print(m)
a=open(os.path.join(pwd, "trainer2.txt"), "w+")
b= "".join(c for c in compat_chars[m])
a.writelines(b)
a.close()"""
