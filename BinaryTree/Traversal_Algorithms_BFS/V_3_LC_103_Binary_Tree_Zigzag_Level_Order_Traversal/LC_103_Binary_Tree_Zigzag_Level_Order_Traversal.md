

















# Double Ended Queue



           q.appendleft                   q.append
                    \                   /
                   --\-----------------/-----
                      \               /
q = deque()                     1
                                      \
                   ----/----------------\-------
                      /                  \
                     /                    \
            q.popleft                      q.pop