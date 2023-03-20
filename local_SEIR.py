
import numpy as np
import numpy as np
import matplotlib as plt
from scipy.integrate import odeint
import matplotlib.pyplot as plt

#MODIFIED VERSION WITH ONE OUTPUT

def solveSEIR(input_parameters):
    
    #for odeint
    def seir_model(y, t, N, beta, alpha, gamma, delta, kappa, lam):
        S, E, I, Q, R, D, P = y
        dSdt = -beta*S*I/N - alpha*S
        dEdt = beta*S*I/N - gamma*E
        dIdt = gamma*E - delta*I
        dQdt = delta*I - lam*Q - kappa*Q
        dRdt = lam*Q
        dDdt = kappa*Q
        dPdt = alpha*S
        
        return dSdt, dEdt, dIdt, dQdt, dRdt, dDdt, dPdt

    # Set initial conditions with values from the paper
 #   N = 14000000
 #   E0 = 318
 #   I0 = 389
 #   Q0 = 700
 #   R0 = 0
 #   D0 = 0
 #   P0 = 0
 #   
    #Initial conditions
    N = 14000000
    E0 = 318
    I0 = 389
    Q0 = 700
    R0 = 0
    D0 = 0
    P0 = 0

    S0 = N - E0 - I0 - Q0 - R0 - D0 - P0
    
    # Parameters must be in the same order 
    beta,alpha,gamma,delta,kappa,lam = input_parameters[0]

    # Set time discretization as in the paper
    t = np.linspace(0, 180, 10000)

    # Solve system of differential equations
    # Returns the seven variables S, E, I, Q, R, D, and P at each time point
    sol = odeint(seir_model, [S0, E0, I0, Q0, R0, D0, P0], t, args=(N, beta, alpha, gamma, delta, kappa, lam))

    
    # dSdt, dEdt, dIdt, dQdt, dRdt, dDdt, dPdt

    # returns susceptible people
    return sol.T[0]