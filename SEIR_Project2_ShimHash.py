import sys
import requests
from bs4 import BeautifulSoup

def fetch_content(url):
    try:
        r = requests.get(url)
    except:
        print("Error:", url)
        return ""

    soup = BeautifulSoup(r.text, "html.parser")

    if soup.body:
        return soup.body.get_text().lower()
    return ""

def words(t):
    mp = {}
    cur = ""
    for ch in t:
        if ch.isalnum():
            cur += ch
        else:
            if cur != "":
                if cur in mp:
                    mp[cur] += 1
                else:
                    mp[cur] = 1
                cur = ""
    if cur != "":
        if cur in mp:
            mp[cur] += 1
        else:
            mp[cur] = 1
    return mp

def code(w):
    p = 53
    m = 2**64
    val = 0
    pw = 1

    for c in w:
        val = (val + ord(c) * pw) % m
        pw = (pw * p) % m

    return val

def build(mp):
    arr = [0] * 64
    for k in mp:
        wt = mp[k]
        hv = code(k)
        for i in range(64):
            if (hv >> i) & 1:
                arr[i] += wt
            else:
                arr[i] -= wt
    out = 0
    for i in range(64):
        if arr[i] > 0:
            out = (1 << i)

    return out

def matching_bit(x, y):
    total = 0
    for i in range(64):
        if ((x >> i) & 1) == ((y >> i) & 1):
            total += 1
    return total

if len(sys.argv) != 3:
    sys.exit(1)

a = sys.argv[1]
b = sys.argv[2]

txt1 = fetch_content(a)
txt2 = fetch_content(b)
m1 = words(txt1)
m2 = words(txt2)
h1 = build(m1)
h2 = build(m2)
print(h1)
print(h2)
print("Common Bit in h1 and h2:", matching_bit(h1, h2))