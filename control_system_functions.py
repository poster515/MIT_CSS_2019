#   update_L will take in tank level (L_current), time resolution in seconds
#   (delta_t) the incoming volumetric flow rate in gallons/hr, and
#   the outgoing tank volumetric flow rate in gallons/hr

def update_L(L_current, delta_t, m_dot1, m_dot2):
#   assume that temperature is constant
    L_next = L_current + (m_dot1 - m_dot2)*(1/3600)*delta_t

    return L_next

    # update_m_dot1 will take in the current pump controller state (ON, OFF), the
    # value of m_dot1 when the pump controller is ON, and the value of m_dot1 when
    # the pump controller is OFF

def update_m_dot1(c_a, m_dot1_on, m_dot1_off):
    if c_a == ON:
        return m_dot1_on
    elif c_a == OFF:
        return m_dot1_off
