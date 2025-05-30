
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


# from rocket_performance import RocketPerformance

# # ex1 = RocketPerformance(200, 130, 110, 3, 240)
# ex2 = RocketPerformance(1210, 215, )

# print(ex1.final_acceleration())


from Rocket_Solvers.performance import Performance


ex2 = Performance(t = 40, m_0 = 1210, m_f = 215, F = 62250, P = 7e6, P2 = 70000, P3 = 101325, D_x = 8.55e-2, D_2 = 27.03e-2)

# mass_flow = ex2.gen_eq.propellant_mass_flow_rate()

print(ex2.gen_eq.propellant_mass_flow_rate())

# print(ex2.gen_eq.area())

print(ex2.gen_eq.characteristic_velocity('D_2'))

print(ex2.gen_eq.effective_exhaust_velocity())

print(ex2.gen_eq.pressure_thrust('D_2'))

print(ex2.gen_eq.exit_velocity('D_2'))










