from z3 import *
s=[Int('serial%d' % i) for i in range(60)]
solver = Solver()

for num in s:
    solver.add(num > 32)
    solver.add(num < 128)

mod = [[0, 9, 2], [2, 7, 12], [0, 5, 10], [1, 0, 8], [6, 4, 9], [4, 10, 5], [2, 7, 12], [4, 7, 4], [4, 6, 12], [6, 4, 9], [4, 7, 4], [0, 9, 2], [6, 4, 9], [2, 4, 10], [0, 5, 10], [2, 1, 9], [4, 7, 4], [6, 4, 9], [4, 3, 11], [4, 7, 4], [2, 1, 9], [0, 5, 10], [3, 5, 11], [1, 0, 8], [2, 4, 10], [2, 7, 12], [4, 6, 12], [2, 7, 12], [4, 7, 4], [4, 10, 5], [3, 8, 0], [4, 6, 12], [6, 5, 0], [4, 7, 4], [3, 8, 0], [5, 0, 6], [2, 1, 9], [4, 7, 4], [0, 5, 10], [4, 6, 12], [4, 7, 4], [0, 5, 10], [3, 5, 11], [4, 7, 4], [3, 5, 11], [4, 6, 12], [3, 8, 0], [2, 4, 10], [4, 6, 12], [4, 7, 4], [6, 4, 9], [4, 3, 11], [4, 7, 4], [4, 6, 12], [6, 4, 9], [2, 4, 10], [4, 6, 12], [5, 7, 0], [2, 4, 10], [2, 7, 12]]

for i in range(60):
    solver.add(s[i] % 7 == mod[i][0])
    solver.add(s[i] % 11 == mod[i][1])
    solver.add(s[i] % 13 == mod[i][2])

print(solver.check())
answer=solver.model()
print(answer)

tidy_answer = ""
for each in s :
	tidy_answer += str(chr(int(str(answer[each]))))

print("hkcert22{"+tidy_answer+"}")

#flag: hkcert22{w31c0m3_t0_w0r1d_0f_d1scr3t3_m4th_4nd_1t_1s_st4rt_0f_t0rtur3}