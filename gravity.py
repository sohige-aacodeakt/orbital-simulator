"""
Gravity and integration functions for orbital mechanics simulator.
"""

# Earth gravitational parameter (m^3/s^2)
MU = 3.986004418e14  # Earth's GM

def gravitational_acceleration(position_vector):
    """
    Calculate gravitational acceleration due to Earth at the origin.
    
    Args:
        position_vector: list or array of 3 floats [x, y, z] (meters)
    
    Returns:
        acceleration_vector: list of 3 floats [ax, ay, az] (m/s^2)
    """
    x, y, z = position_vector
    r = (x**2 + y**2 + z**2)**0.5  # distance from Earth
    # Avoid division by zero
    if r == 0:
        raise ValueError("Position vector is at origin, division by zero.")
    factor = -MU / r**3
    return [factor * x, factor * y, factor * z]

def integrate_euler(state_vector, time_step):
    """
    Forward Euler integration for orbital motion.
    
    Args:
        state_vector: list of 6 floats [x, y, z, vx, vy, vz] (meters, m/s)
        time_step: float (seconds)
    
    Returns:
        new_state_vector: list of 6 floats updated after time_step
    """
    pos = state_vector[:3]
    vel = state_vector[3:]
    
    # Compute acceleration
    acc = gravitational_acceleration(pos)
    
    # Update velocity using acceleration
    new_vel = [vel[i] + acc[i] * time_step for i in range(3)]
    
    # Update position using current velocity (simple Euler)
    new_pos = [pos[i] + vel[i] * time_step for i in range(3)]
    
    return new_pos + new_vel

if __name__ == "__main__":
    # Quick test
    state = [7e6, 0, 0, 0, 7.5e3, 0]  # Low Earth orbit approx
    dt = 1.0
    new_state = integrate_euler(state, dt)
    print("Initial state:", state)
    print("After one second:", new_state)