# orbital-simulator
A foundational orbital mechanics simulator in Python

## Core Physics

The simulator uses forward Euler integration to propagate a satellite's orbit under Earth's gravity.

The core implementation is in `gravity.py`:

- `gravitational_acceleration(position_vector)` computes the acceleration vector due to Earth's gravity using Newton's law of universal gravitation, assuming Earth at the origin.
- `integrate_euler(state_vector, time_step)` updates the satellite's position and velocity using the forward Euler method.

The Euler method approximates the state at time t+Δt as:

    position(t+Δt) = position(t) + velocity(t) * Δt
    velocity(t+Δt) = velocity(t) + acceleration(t) * Δt

where acceleration is computed from the gravitational acceleration function.

This simple integrator is suitable for educational purposes and short-duration simulations.