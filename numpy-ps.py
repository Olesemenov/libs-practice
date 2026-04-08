# Setup
import numpy as np
import pandas as pd
import kagglehub

# Live Coding 1
views = np.array([15000, 32000, 8500, 45000])
likes = np.array([1200, 3000, 800, 4100])
comments = np.array([150, 400, 50, 600])

# TODO:
# total_interactions = likes+comments
# engagement_rate = total_interactions/views*100
# print(f'the engagement_rate is {np.round(engagement_rate, 2)}')



# Guided Practice 1
rpm = np.array([1.5, 2.0, 0.8, 2.5])
production_cost = np.array([10, 30, 5, 50])

# TODO:
salary = views/1000*rpm
total_income = salary - production_cost
print(f'the total_income is {np.round(total_income)}, the best video was {np.argwhere(total_income == np.max(total_income))}')
print(np.max(total_income))


# Live Coding 2
cpu_load = np.array([
    [45, 50, 55, 40, 48],  # Server 1
    [88, 92, 95, 89, 94],  # Server 2
    [20, 25, 22, 18, 30]   # Server 3
])

# TODO:
mean_load = np.mean(cpu_load, axis=1)
absolute_max = np.max(cpu_load, axis=1)
critical_load = cpu_load[cpu_load > 90]
print("Mean load", mean_load)
print("Absolute max", absolute_max)
print("Critical loads", critical_load)
print("Count of accidents", critical_load.size)





# Guided Practice 2
pings = np.array([
    [45, 50, 48, 55],       # Server 1
    [120, 115, 210, 130],   # Server 2
    [300, 250, 310, 280],   # Server 3
    [15, 20, 18, 22]        # Server 4
])

# TODO:
minimum = np.min(pings, axis=1)
mean_ping = np.mean(pings)
overping = pings[pings > 200]
amount_of_overpings = len(overping)
print("Minimum pings", minimum)
print("Mean pings", mean_ping)
print("Amount of overpings", amount_of_overpings)
pri




# Live Coding 3
# kagglehub.dataset_download("alitaqishah/global-mental-health-crisis-index-2026",
#                                   output_dir="datasets", force_download=True)
# df = pd.read_csv("datasets/Global_Mental_Health_Crisis_Index_2026.csv")
# print(df.head())

# TODO: