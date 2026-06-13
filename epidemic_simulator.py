import os
import matplotlib.pyplot as plt
import pandas as pd

def simulate_epidemic(days=60, initial_infected=10, infect_rate=2.0, recovery_rate=0.15):
    # Lists to store daily logs
    days_list = []
    active_infected = []
    recovered = []
    cumulative_infected = []
    
    # Day 0 initialization
    current_active = float(initial_infected)
    current_recovered = 0.0
    current_cumulative = float(initial_infected)
    
    days_list.append(0)
    active_infected.append(current_active)
    recovered.append(current_recovered)
    cumulative_infected.append(current_cumulative)
    
    day_active_exceed_million = None
    day_cumulative_exceed_million = None
    
    for day in range(1, days + 1):
        # Calculate changes based on previous day's active infected
        prev_active = active_infected[-1]
        
        new_infections = prev_active * infect_rate
        new_recoveries = prev_active * recovery_rate
        
        current_active = prev_active + new_infections - new_recoveries
        current_recovered = recovered[-1] + new_recoveries
        current_cumulative = cumulative_infected[-1] + new_infections
        
        days_list.append(day)
        active_infected.append(current_active)
        recovered.append(current_recovered)
        cumulative_infected.append(current_cumulative)
        
        # Check when thresholds are exceeded
        if current_active >= 1_000_000 and day_active_exceed_million is None:
            day_active_exceed_million = day
        if current_cumulative >= 1_000_000 and day_cumulative_exceed_million is None:
            day_cumulative_exceed_million = day
            
    # Create a DataFrame for easy handling
    df = pd.DataFrame({
        'Day': days_list,
        'Active_Infected': active_infected,
        'Recovered': recovered,
        'Cumulative_Infected': cumulative_infected
    })
    
    return df, day_active_exceed_million, day_cumulative_exceed_million

def main():
    print("=" * 60)
    print("         SMART EPIDEMIC SPREAD SIMULATOR")
    print("=" * 60)
    
    days = 60
    df, day_active_exceed_million, day_cumulative_exceed_million = simulate_epidemic(days)
    
    # Fetch final values
    final_active = df.iloc[-1]['Active_Infected']
    final_recovered = df.iloc[-1]['Recovered']
    final_cumulative = df.iloc[-1]['Cumulative_Infected']
    
    print(f"Simulation Duration: {days} Days")
    print(f"Initial Infected: 10 people\n")
    
    print(f"--- Results on Day {days} ---")
    print(f"Active Infected People : {final_active:,.2f} (~{round(final_active):,})")
    print(f"Recovered People       : {final_recovered:,.2f} (~{round(final_recovered):,})")
    print(f"Cumulative Infections  : {final_cumulative:,.2f} (~{round(final_cumulative):,})")
    print("-" * 60)
    
    print("--- Milestones ---")
    if day_active_exceed_million:
        print(f"Day active infections exceed 1 Million: Day {day_active_exceed_million}")
    else:
        print("Active infections did not exceed 1 Million within the simulation period.")
        
    if day_cumulative_exceed_million:
        print(f"Day cumulative infections exceed 1 Million: Day {day_cumulative_exceed_million}")
    else:
        print("Cumulative infections did not exceed 1 Million within the simulation period.")
    print("=" * 60)
    
    # Save results to CSV
    df.to_csv("epidemic_report.csv", index=False)
    print("CSV report saved as 'epidemic_report.csv'")
    
    # Plotting daily growth
    plt.figure(figsize=(10, 6))
    plt.plot(df['Day'], df['Active_Infected'], label='Active Infected', color='#e74c3c', linewidth=2)
    plt.plot(df['Day'], df['Recovered'], label='Recovered (15% daily)', color='#2ecc71', linewidth=2)
    plt.plot(df['Day'], df['Cumulative_Infected'], label='Cumulative Infected', color='#3498db', linewidth=1.5, linestyle='--')
    
    plt.title('Epidemic Spread Growth (60 Days)', fontsize=14, fontweight='bold', pad=15)
    plt.xlabel('Day', fontsize=12)
    plt.ylabel('Number of People (Log Scale)', fontsize=12)
    plt.yscale('log') # Log scale since growth is exponential
    plt.grid(True, which="both", ls="--", alpha=0.5)
    plt.legend(fontsize=11)
    
    # Highlight 1 Million milestone
    plt.axhline(y=1_000_000, color='r', linestyle=':', label='1 Million Mark')
    plt.text(5, 1_200_000, '1 Million Threshold', color='red', fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('epidemic_growth.png', dpi=300)
    print("Plot saved as 'epidemic_growth.png'")
    
if __name__ == '__main__':
    main()
