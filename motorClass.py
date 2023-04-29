import csv

# Define the path to the CSV file
csv_file = "force_data.csv"

# Read the data from the CSV file
force = []
time = []
with open(csv_file) as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    for row in reader:
        force.append(float(row[0]))
        time.append(float(row[1]))

# Calculate the time intervals
dt = []
for i in range(len(time)-1):
    dt.append(time[i+1] - time[i])

# Calculate the impulse
impulse = 0
for i in range(len(force)-1):
    avg_force = (force[i] + force[i+1]) / 2
    impulse += avg_force * dt[i]

# Calculate the burn time
burn_time = time[-1] - time[0]

# Determine the motor classification according to the Newton/s scale
impulse_newton_sec = impulse * 9.81
if impulse_newton_sec < 2.5:
    motor_class = "A"
elif impulse_newton_sec < 5:
    motor_class = "B"
elif impulse_newton_sec < 10:
    motor_class = "C"
elif impulse_newton_sec < 20:
    motor_class = "D"
elif impulse_newton_sec < 40:
    motor_class = "E"
elif impulse_newton_sec < 80:
    motor_class = "F"
elif impulse_newton_sec < 160:
    motor_class = "G"
elif impulse_newton_sec < 320:
    motor_class = "H"
elif impulse_newton_sec < 640:
    motor_class = "I"
elif impulse_newton_sec < 1280:
    motor_class = "J"
elif impulse_newton_sec < 2560:
    motor_class = "K"
elif impulse_newton_sec < 5120:
    motor_class = "L"
elif impulse_newton_sec < 10240:
    motor_class = "M"
elif impulse_newton_sec < 20480:
    motor_class = "N"
elif impulse_newton_sec < 40960:
    motor_class = "O"
elif impulse_newton_sec < 81920:
    motor_class = "P"
elif impulse_newton_sec < 163840:
    motor_class = "Q"
elif impulse_newton_sec < 327680:
    motor_class = "R"
elif impulse_newton_sec < 655360:
    motor_class = "S"
elif impulse_newton_sec < 1310720:
    motor_class = "T"
elif impulse_newton_sec < 2621440:
    motor_class = "U"
elif impulse_newton_sec < 5242880:
    motor_class = "V"
elif impulse_newton_sec < 10485760:
    motor_class = "W"
else:
    motor_class = "X"

# Print the results
print("Impulse: %.2f kg/s" % impulse)
print("Burn time: %.2f s" % burn_time)
print("Motor class: %s" % motor_class)
