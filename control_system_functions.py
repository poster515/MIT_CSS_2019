#   update_L will take in tank level (L_current), time resolution in seconds
#   (delta_t) the incoming volumetric flow rate in gallons/hr, and
#   the outgoing tank volumetric flow rate in gallons/hr

def update_L(before, after, delta_t):
    
    L_current = before[-1: K_LEVEL]
    m_dot1 = before[-1:K_FLOW_IN]
    m_dot2 = before[-1:K_FLOW_OUT]

    L_next = L_current + (m_dot1 - m_dot2)*(1/3600)*delta_t

    return L_next

    # update_m_dot1 will take in the current pump controller state (ON, OFF), the
    # value of m_dot1 when the pump controller is ON, and the value of m_dot1 when
    # the pump controller is OFF

def update_m_dot1(before, after, delta_t):

    c_state = before[-1:K_PUMP_ON]
    m_dot1 = before[-1:K_FLOW_IN]
    m_dot2 = before[-1:K_FLOW_OUT]

    if c_state == 1:
        return m_dot1_on
    elif c_state == 0:
        return m_dot1_off
