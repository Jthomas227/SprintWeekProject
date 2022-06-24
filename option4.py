# Option 4

from matplotlib import pyplot as plt
from matplotlib import style

def get_month_rev_chart():
    style.use("seaborn-dark-palette")

    x_axis = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    y_axis = []

    for x in x_axis:
        revenue = float(input(f"Enter monhtly revenue for {x}: "))
        y_axis.append(revenue)

    fig, ax = plt.subplots()

    ax.bar(x_axis, y_axis, align='center' )

    ax.set_title('Nl Chocolate Monthly Revenue Chart')
    ax.set_ylabel('Monthly Revenue ($)')
    ax.set_xlabel('Month')

    ax.set_xticks(x_axis)
    ax.set_xticklabels(("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"))

    plt.show()

    cont = input("Press any Key to continue...")