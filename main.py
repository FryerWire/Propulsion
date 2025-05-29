
# from isentropic_flow import IsentropicFlow

# IF = IsentropicFlow('P_Pt', 0.39)

# print(IF.P_Pt)
# print(IF.M * 3)
# print(IF.rho_rhot)

# print()

# print(IF)


# from normal_shock import NormalShock

# NS = NormalShock('M', 2)

# print(NS)



# from fanno_flow import FannoFlow

# FF = FannoFlow('M', 3)
# print(FF)


from rocket_performance import RocketPerformance

# ex1 = RocketPerformance(200, 130, 110, 3, 240)
ex2 = RocketPerformance(1210, 215, )

print(ex1.final_acceleration())