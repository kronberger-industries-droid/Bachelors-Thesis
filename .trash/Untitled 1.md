# Equations, Tables, and Charts for Compressible Flow

## Energy Relations

The law of conservation of energy gives:

$$ dq = du + dw \quad \text{(first law of thermodynamics)} $$

$$ = du + p \, dv = dh - v \, dp $$

$$ dq = c_v \, dT + p \, dv \quad \text{[therm perf]} $$

$$ = c_p \, dT - v \, dp $$

## Specific Heats

The specific heats at constant pressure and constant volume are defined by:

$$ c_p = \left( \frac{\partial h}{\partial T} \right)_p \quad \tag{11} $$

$$ c_v = \left( \frac{\partial u}{\partial T} \right)_v \quad \tag{12} $$

It can be shown that:

$$ c_p - c_v = T \left[ \left( \frac{\partial p}{\partial T} \right)_v \left( \frac{\partial v}{\partial T} \right)_p \right] \quad \tag{13a} $$

$$ c_p - c_v = R \quad \text{[therm perf]} \quad \tag{13b} $$

The ratio of specific heats is defined as:

$$ \gamma = \frac{c_p}{c_v} \quad \tag{14} $$

According to the kinetic theory of gases, for many gases over a moderate range of temperature:

$$ \gamma = \frac{n+2}{n} \quad \tag{15} $$

where $ n $ is the number of effective degrees of freedom of the gas molecules.

### Useful Relations for Thermally Perfect Gases

$$ c_p = \frac{dh}{dT} = c_v + R = \frac{R}{\gamma - 1} \quad \text{[therm perf]} \quad \tag{16} $$

$$ c_v = \frac{du}{dT} = c_p - R = \frac{R}{\gamma - 1} \quad \text{[therm perf]} \quad \tag{17} $$

## Enthalpy

The enthalpy of a gas is defined by:

$$ h = u + pv \quad \tag{18} $$

It follows that:

$$ dh = du + p \, dv + v \, dp = dq + v \, dp $$

$$ dh = \left[ c_v + T \left( \frac{\partial p}{\partial T} \right)_v \right] dT + \left[ p + T \left( \frac{\partial p}{\partial T} \right)_T \right] dv $$

$$ dh = (c_v + R)dT = c_p dT \quad \text{[therm perf]} \quad \tag{19b} $$

$$ h = (c_v + R)T + u_0 = c_p T + u_0 \quad \text{[perf]} \quad \tag{20} $$

## Entropy

The entropy is defined by:

$$ ds = \frac{dq}{T} \quad \tag{21} $$

It follows that:

$$ ds = \left( \frac{du + dw}{T} \right)_{rev} = \left( \frac{du + p \, dv}{T} \right)_{rev} = c_v \frac{dT}{T} + \left( \frac{\partial p}{\partial T} \right)_v dv \quad \tag{22a} $$

$$ ds = c_v \frac{dT}{T} - R \frac{dp}{p} \quad \text{[therm perf]} \quad \tag{22b} $$

$$ ds = c_p \frac{dT}{T} - R \frac{dp}{p} $$

$$ s - s_0 = c_p \ln \frac{T}{T_r} - R \ln \frac{p}{p_r} \quad \text{[perf]} \quad \tag{23a} $$

$$ s - s_0 = c_p \ln \frac{T}{T_r} - c_v \ln \frac{\rho}{\rho_r} \quad \tag{23b} $$

$$ s - s_0 = c_v \ln \frac{T}{T_r} + R \ln \frac{\rho_r}{\rho} \quad \text{[perf]} $$

$$ p = p_r \left( \frac{\rho}{\rho_r} \right)^\gamma \, e^{-\gamma - 1 / \gamma (s - s_0)} \quad \text{[perf]} \quad \tag{24} $$

The second law of thermodynamics requires that:

$$ s - s_0 \geq 0 \quad \text{[adiab]} \quad \tag{25} $$

## Continuous One-Dimensional Flow

### Basic Equations and Definitions

The basic equations for the continuous flow of an inviscid, non-heat-conducting gas along a streamline are as follows:

**Thermal equation of state:**

$$ p = \frac{R \, T}{\rho} \quad \text{[therm perf]} \quad \tag{26} $$

**Dynamic equation:**

$$ \frac{1}{\rho} dp + V dV = 0 \quad \tag{27} $$
aaa