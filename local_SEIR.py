
import numpy as np
import numpy as np
import matplotlib as plt
from scipy.integrate import odeint
import matplotlib.pyplot as plt

#MODIFIED VERSION WITH ONE OUTPUT

def solveSEIR(input_parameters):
    
    # for odeint
    def seir_model(y, t, N, beta, alpha, gamma_inv, delta_inv, kappa, lam):
        S, E, I, Q, R, D, P = y
        dSdt = -beta*S*I/N - alpha*S
        dEdt = beta*S*I/N - 1/gamma_inv*E
        dIdt = 1/gamma_inv*E - 1/delta_inv*I
        dQdt = 1/delta_inv*I - lam*Q - kappa*Q
        dRdt = lam*Q
        dDdt = kappa*Q
        dPdt = alpha*S
        
        return dSdt, dEdt, dIdt, dQdt, dRdt, dDdt, dPdt

    # Initial conditions
    N = 14000000
    E0 = 318
    I0 = 389
    Q0 = 700
    R0 = 0
    D0 = 0
    P0 = 0

    S0 = N - E0 - I0 - Q0 - R0 - D0 - P0
    
    # Parameters must be in the same order 
    beta, alpha, gamma_inv, delta_inv, kappa, lam = input_parameters[0]


    # Set time discretization as in the paper
    t = np.linspace(0, 180, 10000)

    # Solve system of differential equations
    # Returns the seven variables S, E, I, Q, R, D, and P at each time point
    sol = odeint(func=seir_model,
                 y0=[S0, E0, I0, Q0, R0, D0, P0],
                 t=t,
                 args=(N, beta, alpha, gamma_inv, delta_inv, kappa, lam))

    
    # dSdt, dEdt, dIdt, dQdt, dRdt, dDdt, dPdt

    # returns infected people
    return sol.T[2]