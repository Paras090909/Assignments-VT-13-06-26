import os
import random
import numpy as np
import matplotlib.pyplot as plt

def run_monte_carlo(runs=1000, years=30, initial_investment=100_000.0, min_return=0.08, max_return=0.15):
    ending_balances = []
    all_trajectories = []
    
    # Set seed for reproducibility
    random.seed(42)
    np.random.seed(42)
    
    for run in range(runs):
        balance = initial_investment
        trajectory = [balance]
        for year in range(1, years + 1):
            ann_return = random.uniform(min_return, max_return)
            balance = balance * (1 + ann_return)
            trajectory.append(balance)
        ending_balances.append(balance)
        all_trajectories.append(trajectory)
        
    return np.array(ending_balances), np.array(all_trajectories)

def main():
    print("=" * 60)
    print("         SMART INVESTMENT PREDICTOR")
    print("=" * 60)
    
    runs = 1000
    years = 30
    initial_investment = 100_000.0
    
    balances, trajectories = run_monte_carlo(runs, years, initial_investment)
    
    best_idx = np.argmax(balances)
    worst_idx = np.argmin(balances)
    
    best_outcome = balances[best_idx]
    worst_outcome = balances[worst_idx]
    average_outcome = np.mean(balances)
    median_outcome = np.median(balances)
    
    print(f"Initial Investment  : Rs. {initial_investment:,.2f}")
    print(f"Simulation Duration : {years} Years")
    print(f"Number of Runs      : {runs:,}\n")
    
    print(f"--- Outcomes ---")
    print(f"Best Outcome (Max)  : Rs. {best_outcome:,.2f}")
    print(f"Worst Outcome (Min) : Rs. {worst_outcome:,.2f}")
    print(f"Average Outcome     : Rs. {average_outcome:,.2f}")
    print(f"Median Outcome      : Rs. {median_outcome:,.2f}")
    print("=" * 60)
    
    # Save the outcomes report to CSV for completeness
    import pandas as pd
    df_outcomes = pd.DataFrame({
        'Simulation_Run': range(1, runs + 1),
        'Ending_Balance_INR': balances
    })
    df_outcomes.to_csv("investment_report.csv", index=False)
    print("All ending balances saved to 'investment_report.csv'")
    
    # Plotting results
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    
    # Chart 1: Trajectories (Best, Worst, and sample runs)
    time_axis = list(range(years + 1))
    
    # Plot first 50 sample trajectories in light gray
    for i in range(min(50, runs)):
        ax1.plot(time_axis, trajectories[i], color='gray', alpha=0.15, linewidth=1)
        
    # Plot Best, Worst, and Average trajectories
    ax1.plot(time_axis, trajectories[best_idx], color='#2ecc71', label=f'Best (Ending: Rs. {best_outcome:,.0f})', linewidth=2.5)
    ax1.plot(time_axis, trajectories[worst_idx], color='#e74c3c', label=f'Worst (Ending: Rs. {worst_outcome:,.0f})', linewidth=2.5)
    
    # Plot average trajectory
    avg_trajectory = np.mean(trajectories, axis=0)
    ax1.plot(time_axis, avg_trajectory, color='#3498db', label=f'Mean Trajectory (Ending: Rs. {average_outcome:,.0f})', linewidth=2.5, linestyle='--')
    
    ax1.set_title('Investment Growth Trajectories (30 Years)', fontsize=12, fontweight='bold')
    ax1.set_xlabel('Year', fontsize=10)
    ax1.set_ylabel('Balance (Rs.)', fontsize=10)
    ax1.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'Rs. {x:,.0f}'))
    ax1.grid(True, ls="--", alpha=0.5)
    ax1.legend(fontsize=9, loc='upper left')
    
    # Chart 2: Ending Balance Distribution (Histogram)
    # Using seaborn for styling if possible, otherwise standard matplotlib
    n, bins, patches = ax2.hist(balances, bins=40, color='#9b59b6', alpha=0.7, edgecolor='white')
    
    # Add vertical lines for mean, min, and max
    ax2.axvline(average_outcome, color='#3498db', linestyle='dashed', linewidth=2, label=f'Average (Rs. {average_outcome:,.0f})')
    ax2.axvline(worst_outcome, color='#e74c3c', linestyle='dotted', linewidth=2, label=f'Worst (Rs. {worst_outcome:,.0f})')
    ax2.axvline(best_outcome, color='#2ecc71', linestyle='dotted', linewidth=2, label=f'Best (Rs. {best_outcome:,.0f})')
    
    ax2.set_title('Distribution of Ending Balances (1,000 Runs)', fontsize=12, fontweight='bold')
    ax2.set_xlabel('Ending Balance (Rs.)', fontsize=10)
    ax2.set_ylabel('Frequency', fontsize=10)
    ax2.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'Rs. {x:,.0f}'))
    ax2.grid(True, ls="--", alpha=0.5)
    ax2.legend(fontsize=9, loc='upper right')
    
    plt.tight_layout()
    plt.savefig('investment_outcomes.png', dpi=300)
    print("Plot saved as 'investment_outcomes.png'")

if __name__ == '__main__':
    main()
