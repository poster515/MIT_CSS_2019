
# coding: utf-8

# In[87]:


import random
import math

ON = 1
OFF = 0

def next_mdot1(current_mdot1_state, current_mc_state):
    if current_mc_state == ON:
        return 100
    else:
        return 0
    
def next_mdot2(current_mdot2_state):
#     print("current mdot2: " + str(current_mdot2_state))
    
    next_state = 0
    
    if current_mdot2_state > 95:
        next_state = current_mdot2_state + random.randint(-10, 10)
        if next_state > 100:
            return 100
        else:
            return next_state
        
    elif current_mdot2_state < 5:
        next_state = current_mdot2_state + random.randint(10, 10)
        if next_state < 0:
            return 0
        else:
            return next_state
        
    else:
        return current_mdot2_state + random.randint(-10, 10)
    
def next_L(current_L, current_mdot1, current_mdot2, delta_t):
    
    return current_L + (current_mdot1 - current_mdot2)*(1/3600)*delta_t


# In[88]:


import matplotlib.pyplot as plt

class simple_system:
    OFF = 0
    ON = 1
    
    # initialize indices
    mc_state_idx = 0
    mdot1_idx = 1
    mdot2_idx = 2
    L_idx = 3
    
    # initialize alarm setpoints
    low_lvl_alarm = 1 # gallons
    high_lvl_alarm = 9 #gallons
    MAX_TANK_LEVEL = 10 #gallons
    
    # simulation params
    delta_t = 1 #seconds (i.e., 1 millisecond)
    run_time = 10000 # total data points
    
    # placeholders for initial condition
    mc_state_i = OFF
    m_dot1_i = 0 #gallons/hr
    m_dot2_i = 0 #gallons/hr
    L_i = 9.8 #gallons
    
    def __init__(self, mc_state, m_dot1, m_dot2, L):
        self.mc_state_i = mc_state
        self.m_dot1_i = m_dot1
        self.m_dot2_i = m_dot2
        self.L_i = L
        
    # complete initial condition array
    initial_state = []
    initial_state.append(mc_state_i)
    initial_state.append(m_dot1_i)
    initial_state.append(m_dot2_i)
    initial_state.append(L_i)
        
    # now add to the overall state array
    state = []
    state.append(initial_state)
    
    # create plot data arrays
    time = []
    level = []
    mc = []
    
    # execute simulation
    for i in range(run_time):
#         print("i = " + str(i))
#         print(state[len(state) - 1][mc_state_idx])
#         print(state[len(state) - 1][mdot1_idx])
#         print(state[len(state) - 1][mdot2_idx])
#         print(state[len(state) - 1][L_idx])
        
        if state[len(state) - 1][L_idx] > high_lvl_alarm:
#             print("Reached high level alarm, shutting off pump.")
            state.append([OFF, 
                      next_mdot1(state[len(state) - 1][mdot1_idx], state[len(state) - 1][mc_state_idx]), 
                      next_mdot2(state[len(state) - 1][mdot2_idx]), 
                      next_L(state[len(state) - 1][L_idx], state[len(state) - 1][mdot1_idx], state[len(state) - 1][mdot2_idx], delta_t)])
            
        elif state[len(state) - 1][L_idx] < low_lvl_alarm:
#             print("Reached low level alarm, turning on pump.")
            state.append([ON, 
                      next_mdot1(state[len(state) - 1][mdot1_idx], state[len(state) - 1][mc_state_idx]), 
                      next_mdot2(state[len(state) - 1][mdot2_idx]), 
                      next_L(state[len(state) - 1][L_idx], state[len(state) - 1][mdot1_idx], state[len(state) - 1][mdot2_idx], delta_t)])
        else:
#             print("Level is in band.")
            state.append([state[len(state) - 1][mc_state_idx], 
                      next_mdot1(state[len(state) - 1][mdot1_idx], state[len(state) - 1][mc_state_idx]), 
                      next_mdot2(state[len(state) - 1][mdot2_idx]), 
                      next_L(state[len(state) - 1][L_idx], state[len(state) - 1][mdot1_idx], state[len(state) - 1][mdot2_idx], delta_t)])
        time.append(i/1000)
        level.append(next_L(state[len(state) - 1][L_idx], state[len(state) - 1][mdot1_idx], state[len(state) - 1][mdot2_idx], delta_t))
        mc.append(MAX_TANK_LEVEL * state[len(state) - 1][mc_state_idx])
    
    plt.figure(figsize = (20,5))
    plt.plot(time, level, label="Tank Level")
    plt.plot(time, mc, "--", label="Pump State")
    plt.title("Tank Level and Pump State vs Time")
    plt.xlabel('Time (ms)')
    plt.ylabel('Level (gal)')
    plt.legend()
    plt.show()

