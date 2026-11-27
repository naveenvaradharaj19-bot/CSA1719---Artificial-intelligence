# Bayesian Network

# Probability of rain
P_rain = 0.3

# Probability of wet ground
P_wet_given_rain = 0.9
P_wet_given_no_rain = 0.2

# Calculate probability of wet ground
P_wet = (
    P_rain * P_wet_given_rain +
    (1 - P_rain) * P_wet_given_no_rain
)

print("Probability of Rain:", P_rain)
print("Probability of Wet Ground:", round(P_wet, 2))

# Probability of rain given wet ground
P_rain_given_wet = (
    P_rain * P_wet_given_rain
) / P_wet

print("Probability of Rain given Wet Ground:",
      round(P_rain_given_wet, 2))
