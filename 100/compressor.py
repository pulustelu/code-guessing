with open("setup.py") as f:
    src = f.read().encode()

out = ""
for c in src:
    out += f"{c:08b}".replace("0", "\u200b").replace("1", "\u200c")
print("behold:", out.replace("\u200b", "0").replace("\u200c", "1"))
with open("compressed.txt", "w") as f:
    f.write(out)
g = {}
exec(src, g)
print(g["poy"])