import hw5a as pta
import random as rnd
from matplotlib import pyplot as plt
import math
# endregion

# region functions
def ffPoint(Re, rr):
    """
    This function takes Re and rr as parameters and outputs a friction factor according to the following:
    1.  if Re>4000 use Colebrook Equation
    2.  if Re<2000 use f=64/Re
    3.  else calculate a probabilistic friction factor where the distribution has a mean midway between the prediction
        of the f=64/Re and Colebrook Equations and a standard deviation of 20% of this mean
    :param Re:  the Reynolds number
    :param rr:  the relative roughness
    :return:  the friction factor
    """
    if Re>=4000:
        return pta.ff(Re, rr,CBEQN=True)
    if Re<=2000:
        return pta.ff(Re, rr)

    CBff= pta.ff(Re, rr, CBEQN=True)  #prediction of Colebrook Equation in Transition region
    Lamff= pta.ff(Re, rr)  #prediction of Laminar Equation in Transistion region
    mean=Lamff + (CBff - Lamff) * (Re - 2000) / 2000 # Compute mean friction factor
    sig=0.2*mean
    return rnd.gauss(mean, sig)  #use normalvariate to select a number randomly from a normal distribution

def PlotPoint(Re,f):
    if 2000 <= Re <= 4000:
        marker_style = "^" if 2000 <= Re <= 4000 else "o"  # Triangle for transition flow

        color = "red" if 2000 <= Re <= 4000 else "black"# Circle for laminar/turbulent flow

    # Call the Moody diagram function to ensure plot is available
    pta.plotMoody(plotPoint=True)

    # Plot the new point on the diagram
    plt.scatter(Re, f, marker=marker_style, s=100, edgecolor=color, facecolor="none", linewidth=2)

    # Update and refresh the plot
    plt.draw()
    plt.pause(0.1)

def main():
    """
    Runs the interactive Moody diagram program.
    Allows users to input multiple parameter sets while tracking previous results.
    """
    while True:
        try:
            Re = float(input("Enter the Reynolds number (or -1 to exit): "))
            if Re == -1:
                break  # Exit condition
            rr = float(input("Enter the relative roughness: "))

            f = ffPoint(Re, rr)  # Compute friction factor
            print(f"Re: {Re:.1f}, rr: {rr:.5f}, f: {f:.5f}")

            PlotPoint(Re, f)  # Plot point on Moody diagram
        except ValueError:
            print("Invalid input. Please enter numerical values.")
# endregion

# region function calls
if __name__=="__main__":
    main()
# endregion