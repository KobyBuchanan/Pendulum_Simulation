import numpy as np
import matplotlib.pyplot as plt


def make_energy_graph(body_list):
    energy_list = [[i,[]] for i,body in enumerate(body_list)]
    iteration_type = []

    with open("energy_data.txt", 'r') as file:
        i = 0
        for line in file:
            #energy = line.replace(' ', '').replace('\n', '').replace(']', '').replace('[', '').split(',')
            energy = line.translate(str.maketrans('', '', ' \n[]')).split(',')

            iteration_type.append(energy[0])
            energy = energy[1:]
            for item in energy:
                energy_list[i][1].append(float(item))
            i += 1
            if i == len(body_list):
                break

        time = np.arange(0, len(energy_list[0][1]), 1)

        plt.figure(figsize=(10, 6))
        for i in range(len(iteration_type)):
            label = f'body {energy_list[i][0]} ' + 'RK4'
            if iteration_type[i] == "True":
                label = f'body {energy_list[i][0]} ' + 'Euler'
            plt.plot(time, energy_list[i][1], label=label)

        plt.title("Total Energy vs. Time", fontsize=14)
        plt.xlabel("Time (s)", fontsize=12)
        plt.ylabel("Energy (J)", fontsize=12)
        plt.grid(True)
        plt.legend()
        plt.savefig("energy_vs_time.png")  # Save the plot
        print("Plot saved to device")
        #plt.show()
