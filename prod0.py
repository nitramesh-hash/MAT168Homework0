import cvxpy as cp
XB = cp.Variable()
XC = cp.Variable()
constraints = [(1/200) * XB + (1/140) * XC <= 40, 0 <= XB, XB <= 6000, 0 <= XC, XC <= 4000]
profit = cp.Maximize(25 * XB + 30 * XC)
prob = cp.Problem(profit, constraints)
prob.solve()
print("status:", prob.status)
print("optimal value = ", prob.value)
print("XB = ", XB.value)
print("XC = ", XC.value)
