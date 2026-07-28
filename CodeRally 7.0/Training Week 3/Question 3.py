""" You are building a massive, long data center. It can be modeled as a number line. Inside, there are n server racks, each generating a specific amount of heat. You need to install a single, powerful "Central Cooling Unit" at one specific location along this line.

The "cooling load" on the Central Cooling Unit is calculated as the sum of heat_i * distance_i for all servers, where heat_i is the heat output of server i, and distance_i is the absolute distance from the cooling unit to server i. Your goal is to find the location for the cooling unit that minimizes the total cooling load.

This is a weighted version of the classic median problem. The optimal location is the weighted median.

Input Format

The input consists of several test cases. The first line contains the number of test cases. For each test case, the first line contains the integer n (0 < n < 1000), the number of server racks. The next n lines each contain a pair of integers: location and heat (0 < location, heat < 100,000).

Constraints

0 < n < 1000
0 < location, heat < 100,000
Output Format

For each test case, your program must write the minimal total cooling load. """

import sys

def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    T = int(data[idx])
    idx += 1
    out = []
    for _ in range(T):
        n = int(data[idx])
        idx += 1
        points = []
        for _ in range(n):
            loc = int(data[idx])
            idx += 1
            heat = int(data[idx])
            idx += 1
            points.append((loc, heat))
        points.sort(key=lambda p: p[0])

        total_heat = sum(h for _, h in points)

        prefix = 0
        median_loc = points[-1][0]
        for loc, heat in points:
            prefix += heat
            if 2 * prefix >= total_heat:
                median_loc = loc
                break

        cost = sum(heat * abs(loc - median_loc) for loc, heat in points)
        out.append(str(cost))

    sys.stdout.write('\n'.join(out) + '\n')

if __name__ == '__main__':
    main()
