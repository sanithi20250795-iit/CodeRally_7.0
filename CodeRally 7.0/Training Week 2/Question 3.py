import sys

input = sys.stdin.readline

def on_segment(px, py, x1, y1, x2, y2):
    cross = (x2 - x1) * (py - y1) - (y2 - y1) * (px - x1)
    if cross != 0:
        return False
    return (
        min(x1, x2) <= px <= max(x1, x2) and
        min(y1, y2) <= py <= max(y1, y2)
    )
# ---------- Point Inside Polygon (Ray Casting) ----------
def inside_polygon(x, y):
    inside = False
    n = len(poly)

    for i in range(n):
        x1, y1 = poly[i]
        x2, y2 = poly[(i + 1) % n]

        # Boundary counts as inside
        if on_segment(x, y, x1, y1, x2, y2):
            return True

        if (y1 > y) != (y2 > y):
            xinters = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
            if xinters > x:
                inside = not inside

    return inside
# ---------- Input ----------
P = int(input())
poly = [tuple(map(int, input().split())) for _ in range(P)]

S = int(input())
sprinklers = []

for _ in range(S):
    x, y, r = map(int, input().split())
    sprinklers.append((x, y, r * r))

Q = int(input())

# ---------- Process Queries ----------
out = []

for _ in range(Q):
    x, y = map(int, input().split())

    if not inside_polygon(x, y):
        out.append("OUTSIDE")
        continue

    wet = False
    for sx, sy, rr in sprinklers:
        dx = x - sx
        dy = y - sy
        if dx * dx + dy * dy <= rr:
            wet = True
            break

    out.append("INSIDE_WET" if wet else "INSIDE_DRY")

sys.stdout.write("\n".join(out))
