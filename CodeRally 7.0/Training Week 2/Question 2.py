
def solve():
   import sys
   data = sys.stdin.read().split()
   n = int(data[0])
   temps = [float(x) for x in data[1:1 + n]]

   alerts = []
   skip = 0
   streak_type = None
   streak_len = 0

   for i in range(n):
       if skip > 0:
           skip -= 1
           streak_type = None
           streak_len = 0
           continue
          
       t = temps[i]
       if t >= 35:
           cat = 'H'
       elif t <= 5:
           cat = 'C'
       else:
           cat = None

       if cat is not None and cat == streak_type:
           streak_len += 1
       else:
           streak_type = cat
           streak_len = 1 if cat is not None else 0

       if streak_len == 3:
           alerts.append(i + 1)
           skip = 2
           streak_type = None
           streak_len = 0

   print(' '.join(map(str, alerts)) if alerts else "NONE")

solve()
