2024-08-05 12:43

Status:

Tags: [[gas velocity]],  [[mach number]], 

# Mach number ( 1 )
## Calculation

$$Ma=\frac{u}{c}$$
$Ma\dots$mach number ( 1 )
$u\dots$gas velocity ( $\frac{m}{s}$ )
$c\dots$[[Local Speed of Sound ( m s⁻¹ )]] ( $\frac{m}{s}$ )
### From area ratio
This non linear formula usually has to be solved numerically.
$$\frac{A}{A^*} = \frac{1}{Ma} \left[ \frac{2}{\gamma + 1} \left( 1 + \frac{\gamma - 1}{2} Ma^2 \right) \right]^{\frac{\gamma + 1}{2 (\gamma - 1)}}$$

$\frac{A}{A^*}\dots$reference area to throat area ratio ( $1$ )
$Ma\dots$[[31 - Mach number ( 1 )|Mach number]] ( $1$ )
$\gamma\dots$[[Specific Heat Ratio ( 1 )|Specific heat ratio]] ( 1 )
#### Linearized function
To be able to calculate the Mach number without numerical methods "Someone" derived a linear version of the formula
$$ Ma = \left[ k_1 \frac{A}{A_*} + (1 - k_1) \right]^{k_2} $$

where $k_1$ and $k_2$ are functions of the specific heat ratio and with values given by a *non-linear polynomial regression analysis* as

$$ k_1 = 218.0629 - 243.5764 \gamma + 71.7925 \gamma^2$$
$$ k_2 = -0.122450 + 0.281300 \gamma$$
#### [[Subsonic Regime ( 0.3 < Ma < 1.0 )]]
At every part of the duct other then the throat moves at subsonic speeds. 
#### [[Sonic Regime ( Ma = 1 )]]
In converging Ducts sonic flow is a limit phenomenon for converging ducts which only is possible when a diverging section follows, creating a section with a minimum in cross section which is called the throat.
#### [[Super Sonic Regime ( M > 1)]]
Its not possible to achieve supersonic flow inside of a converging duct. This stems from the fact that for subsonic conditions the velocity increases while traveling through the duct. Once the velocity crosses sonic speeds this characteristic changes to the opposite. Now the velocity would decrease again, which now limits the gases velocity to subsonic velocities and in the limit to sonic speeds. 

## References