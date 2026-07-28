"""Two warehouses each list their inventory as (sku, quantity) lines. They suspect duplicate SKUs due to merger. Determine, for each SKU appearing in either warehouse: total quantity across both, whether it's "shared" or "unique", and finally print the top K SKUs by total quantity (ties broken by SKU ascending).

Input Format

Line 1: N M K. Next N lines: warehouse A entries. Next M lines: warehouse B entries

Constraints

1 ≤ N, M ≤ 10^5. 1 ≤ K ≤ N+M. SKU is alphanumeric, length ≤ 16. Quantity in [1, 10^6].

Output Format

K lines: sku total_qty SHARED|UNIQUE"""

import sys
import heapq

def main():
    d = sys.stdin.buffer.read().split()
    if not d:
        return

    n, m, k = map(int, d[:3])
    i = 3
    inv = {}

    for w, count in ((1, n), (2, m)):
        for _ in range(count):
            sku = d[i]
            qty = int(d[i + 1])
            i += 2

            e = inv.get(sku)
            if e is None:
                inv[sku] = [qty, w]
            else:
                e[0] += qty
                e[1] |= w

    top = heapq.nsmallest(
        k,
        inv.items(),
        key=lambda x: (-x[1][0], x[0])
    )

    out = [
        sku + b' ' +
        str(v[0]).encode() + b' ' +
        (b'SHARED' if v[1] == 3 else b'UNIQUE')
        for sku, v in top
    ]

    sys.stdout.buffer.write(b'\n'.join(out))

if __name__ == "__main__":
    main()
