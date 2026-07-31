# puppydog does group decomposition!
r'''
 #############    ,------------------------.
#  __~~~~~__  #   | i wruff group theory ! |
# \_ O   O _/ #  <_________________________/
#   \  '  /   #
#    =====    #
 ##/~%~%~%~\##                                   '''
(source): "https://www.tumblr.com/shiftythrifting/\
823683395572858880/goodwill-grand-junction-colorado"

# =============== How To Use! ===============
# 1. Input the name of a finite group, such as
#    "C15" for the cyclic group of order 15.
# 2. Wait a little while for the number to get
#    decomposed by the puppydog.
# 3. Watch as the precise decomposition gets
#    printed to your terminal!
# ===========================================

def entry():
    numberoid = parse(input("Group please: "))
    print("Here you go!", classify_group(numberoid), "=", end=" ", flush=True)
    for Q, ext in decompose(numberoid):
        print(Q + ext, end="", flush=True)
    print(__doc__)

# puppydog says: here's the main algorithm! it's pretty pawsome!
def decompose(G):
    while True:
        try:
            Hs = G.unique_proper_subgroups()
            N = max(filter(G.is_normal, Hs), key=lambda H: H.order)
            Q = G / N
            yield classify_group(Q), classify_extension(N, G, Q)
            G = N
        except ValueError:
            yield classify_group(G), ""
            break

# puppydog says: this only supports cyclic groups for now :3
def parse(s):
    if s.startswith("C"):
        import sys
        sys.path.append([p for p in sys.path if p.endswith("site-packages")][0] + "/src")
        from finite_algebras import generate_cyclic_group
        return generate_cyclic_group(int(s[1:]))

# puppydog says: this only supports cyclic groups for now :3
def classify_group(G):
    if G.is_cyclic():
        return f"C{G.order}"

# puppydog says: this only supports direct products for now :3
def classify_extension(N, G, Q):
    Q = Q.copy_algebra([e[1:] for e in Q.elements])
    # puppydog reminds you of the schur-zassenhaus theorem
    from math import gcd
    if gcd(N.order, Q.order) == 1:
        if G.is_normal(Q):
            return "×"
        else:
            return "⋊"
    elif set(N.elements) <= set(G.center()):
        return "×ᶜ"
    # puppydog doesn't know how solve the extension problem :(
    return "?"

# puppydog is excited to play with you !
entry()

# puppydog says good bye... i love you <3
