import numpy as np
import random
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Discrete case, weighted dice
class Dice:
    # Create a dice object
    # It has 2 properties: values, weights and 1 function: roll
    def __init__(self, values, weights):
        self.values = values
        self.weights = weights
    def roll(self, times):
        return random.choices(self.values, weights=self.weights, k=times)

# Plot realization of dice sample results and visualize the convolution
def plot_dice_results(V1=[1,2,3,4,5,6], V2=[1,2,3,4,5,6], weights1=None, weights2=None, N=1000):
    # Initialize Dices
    dice1 = Dice(values = V1, weights = weights1)
    dice2 = Dice(values = V2, weights = weights2)
    # Draw Random Samples form dices
    results1 = dice1.roll(10000)
    results2 = dice2.roll(10000)
    results3 = np.array(results1) + np.array(results2)
    # Count Results
    counts1 = {num: results1.count(num) for num in [1,2,3,4,5,6]}
    counts2 = {num: results2.count(num) for num in [1,2,3,4,5,6]}
    counts3 = {num: results3.tolist().count(num) for num in np.unique(results3)}
    # Create figure object
    fig = make_subplots(rows=3, cols=1, shared_xaxes=False)

    # Add traces for each subplot (bar plots)
    fig.add_trace(go.Bar(x=list(counts1.keys()), y=list(counts1.values()), name='Figure 1'), row=1, col=1)
    fig.add_trace(go.Bar(x=list(counts2.keys()), y=list(counts2.values()), name='Figure 2'), row=2, col=1)
    fig.add_trace(go.Bar(x=list(counts3.keys()), y=list(counts3.values()), name='Figure 3'), row=3, col=1)

    # Add text annotations for the count at the top of each bar
    for fig_counts, row in zip([counts1, counts2, counts3], range(1, 4)):
        for num, count in fig_counts.items():
            fig.add_annotation(
                x=num,
                y=count,
                text=str(count),
                showarrow=True,
                arrowhead=2,
                ax=0,
                ay=-30,
                font=dict(size=10, color='black'),
                row=row,
                col=1
            )


    # Update subplot layout
    fig.update_layout(title_text="Histograms of Sampled Numbers: Dice1, Dice2, Dice1+Dice2", height=800, showlegend=True)

    return fig