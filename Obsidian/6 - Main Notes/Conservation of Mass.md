2024-08-05 11:49

Status: [[in work]]

Tags: [[calculation]], [[conservation law]]

# Conservation of Mass
## Principle
The conservation of mass principle states that mass cannot be created or destroyed within a closed system. It must be conserved as it moves through the system.
$$
\frac{\partial \rho}{\partial t} + \nabla \cdot (\rho \mathbf{v}) = 0
$$
$\rho\dots$fluid density ( $\frac{kg}{m^3}$ )
$\mathbf{v}\dots$fluid velocity ( $\frac{m}{s}$ )
$\nabla \cdot (\rho \mathbf{v})\dots$divergence of the mass flux
## Application in Fluid Mechanics
### Incompressible Flow:
For incompressible flow, where the fluid density $\rho$ is constant, the conservation of mass simplifies to:

$$
\nabla \cdot \mathbf{v} = 0
$$

This indicates that the divergence of the velocity field is zero, meaning the volume of any fluid element remains constant as it moves.
### Compressible Flow:

In compressible flow, where density $ \rho $ can change significantly, the full continuity equation must be used. The conservation of mass must account for changes in density and velocity:

$$
\frac{\partial \rho}{\partial t} + \nabla \cdot (\rho \mathbf{v}) = 0
$$

This formulation ensures that the mass entering a volume minus the mass leaving that volume, plus any change in mass within the volume, equals zero.

#### Usage in steady flow systems

$$
\frac{dM}{dt} = \dot{m}_{\text{in}} - \dot{m}_{\text{out}}=0\quad\to\quad \dot{m}_{in}=\dot{m}_{out}
$$

$\frac{dM}{dt}\dots$rate of change of mass within the control volume
$\dot{m}_{\text{in}}\dots$mass flow rate into the control volume
$\dot{m}_{\text{out}}\dots$mass flow rate out of the control volume

For a control volume with variable density, the mass flow rate is given by:

$$
\dot{m} = \rho \cdot \mathbf{v} \cdot \mathbf{A}
$$

$\dot{m}\dots$mass flow rate
$\mathbf{v}\dots$is the velocity vector
$\mathbf{A}\dots$area vector of the control surface
$\rho\dots$density of the fluid


## References