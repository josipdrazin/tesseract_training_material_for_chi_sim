from fontTools.ttLib import TTFont
import os, subprocess, pathlib

text = open("trainer2.txt", "r+")
lines=[ch for c in text.readlines() for ch in c]
lines2 = ["".join(str(i) for i in [lines.pop(0) for i in range(100)]) for j in range(int(len(lines)/100))]
lines2.append( "".join(str(i) for i in [lines.pop(0) for i in range(len(lines))]) )
lines=lines2
#print(lines)
pwd = os.getenv("PWD")
fontdir=os.path.join(pwd, "fonts")
unicharset=os.path.join(pwd,"langdata/chi_sim.unicharset")
fonts=[os.path.join(dp, f) for dp, dn, fn in os.walk(os.path.join(pwd,"fonts")) for f in fn]
count=len(lines)
fonts=[y for y in fonts if (y.endswith(".otf") or y.endswith(".ttf"))]
text.close()
for font in fonts:
	#count=0
#	if not ( font.endswith(".ttf") or font.endswith(".otf")):
#		pass
	print(pathlib.Path(font).stem)
	font_trunc=pathlib.Path(font).stem
	fnt=TTFont(font)
	for char in lines:
		if not os.path.exists(os.path.join(pwd, f"t2i/lines[{count-len(lines)}]")):
	                os.mkdir(os.path.join(pwd, f"t2i/lines[{count-len(lines)}]"))
		print(f"{font} -- {char}")
		#lines.append(char)
		basedir = os.path.join(pwd, f"t2i/lines[{count-len(lines)}]")
		print(f" basedir {basedir}")
		txt=os.path.join(pwd, f"t2i/lines[{count-len(lines)}]/lines_{count-len(lines)}.txt")
		o=open(txt, "w+")
		o.writelines(char)
		o.close()
		basefile = f"chi_sim_{count-len(lines)}"
		command=f"""text2image --find_fonts \
--fonts_dir ./.fonts \
--text {txt} \
--min_coverage 0.99975 \
--render_per_font=false \
--outputbase {os.path.join(basedir, basefile)} \
--xsize 800 \
--ysize 300 \
--ptsize 50 """
#		subprocess.run([command])
#		lines.pop(0)
		comd=f" -font {font} -pointsize 50 -fill black -background white -size 300x150 text:{txt} {os.path.join(basedir, basefile)}.tiff"
		subprocess.run(["text2image",
"--find_fonts",
f"--fonts_dir={fontdir}",
f"--font={font_trunc}",
f"--text={txt}",
"--min_coverage=0.99975",
f"--outputbase={os.path.join(basedir, basefile)}",
"--ptsize=9",
"--xsize=3800",
"--ysize=2400",
"--resolution=700",
"--box_padding=200",
"--writing_mode=horizontal",
"--margin=400",
"--rotate_image=false",
"--char_spacing=5",
f"--unicharset_file={unicharset}"])
		lines.pop(0)
