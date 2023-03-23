import numpy as np
import numpy as np
import matplotlib as plt
from scipy.integrate import odeint
import matplotlib.pyplot as plt

#MODIFIED VERSION WITH ONE OUTPUT

def solveSEIR_UQpy(input_parameters):
    
    # for odeint
    def seir_model(y, t, N, alpha, beta, gamma_inv, delta_inv, lam, kappa):
        S, E, I, Q, R, D, P, R0 = y #C are the cumulative cases
        dSdt = -beta*S*I/N - alpha*S
        dEdt = beta*S*I/N - 1/gamma_inv*E
        dIdt = 1/gamma_inv*E - 1/delta_inv*I
        dQdt = 1/delta_inv*I - lam*Q - kappa*Q
        dRdt = lam*Q
        dDdt = kappa*Q
        dPdt = alpha*S
        R0t = (1 + (np.log(I+Q/t)*gamma_inv)) * (1 + (np.log(I+Q/t)/lam))

        
        return dSdt, dEdt, dIdt, dQdt, dRdt, dDdt, dPdt, R0t

    # Initial conditions
    N = 14000000
    E0 = 318
    I0 = 389
    Q0 = 700
    R0 = 0
    D0 = 0
    P0 = 0
    R0t0=5744
  #  C0=I0
    #??? INITIAL CONDITION FOR RHO0 - but it does not matter actually

    S0 = N - E0 - I0 - Q0 - R0 - D0 - P0
    
    # unpack the input parameters
    # Parameters must be in the same order 
    alpha, beta, gamma_inv, delta_inv, lam, kappa = input_parameters[0]


    # Set time discretization as in the paper
    t = np.linspace(1e-1, 180, 10000) #aggiornata partendo da t

    # Solve system of differential equations
    # Returns the seven variables S, E, I, Q, R, D, and P at each time point AND RHO 0
    sol = odeint(func=seir_model,
                 y0=[S0, E0, I0, Q0, R0, D0, P0, R0t0],
                 t=t,
                 args=(N, alpha, beta, gamma_inv, delta_inv, lam, kappa))

    
    # dSdt, dEdt, dIdt, dQdt, dRdt, dDdt, dPdt, R0t

    # returns infected people
    return sol.T[2]



def solveSEIR(input_parameters):

    # for odeint
    def seir_model(y, t, N, alpha, beta, gamma_inv, delta_inv, lam, kappa):
        S, E, I, Q, R, D, P, R0, Ct = y
        dSdt = -beta*S*I/N - alpha*S
        dEdt = beta*S*I/N - 1/gamma_inv*E
        dIdt = 1/gamma_inv*E - 1/delta_inv*I
        dQdt = 1/delta_inv*I - lam*Q - kappa*Q
        dRdt = lam*Q
        dDdt = kappa*Q
        dPdt = alpha*S
        R0t = (1 + (np.log(I+Q/t)*gamma_inv)) * (1 + (np.log(I+Q/t)/lam))
        dIdt2=beta*S*I/N - I*(1/gamma_inv)
        Ct=Ct+dIdt2
        
        return dSdt, dEdt, dIdt, dQdt, dRdt, dDdt, dPdt, R0t, Ct

    # Initial conditions
    N = 14000000
    E0 = 318
    I0 = 389
    Q0 = 700
    R0 = 0
    D0 = 0
    P0 = 0
    R0t0=5744
    C0=I0

    S0 = N - E0 - I0 - Q0 - R0 - D0 - P0
    
    # Parameters must be in the same order 
    alpha, beta, gamma_inv, delta_inv, lam, kappa = input_parameters


    # Set time discretization as in the paper
    t = np.linspace(1e-1, 180, 10000)

    # Solve system of differential equations
    # Returns the seven variables S, E, I, Q, R, D, and P at each time point
    sol = odeint(func=seir_model,
                 y0=[S0, E0, I0, Q0, R0, D0, P0, R0t0,C0],
                 t=t,
                 args=(N, alpha, beta, gamma_inv, delta_inv, lam, kappa))

    return sol.T