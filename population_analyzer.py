import os
import pandas as pd

def simulate_population(years=50, initial_pop=50_000, growth_rate=0.07, migration_loss=0.02):
    years_list = []
    population = []
    growth_contribution = []
    migration_contribution = []
    
    current_pop = float(initial_pop)
    
    # Year 0 initialization
    years_list.append(0)
    population.append(current_pop)
    growth_contribution.append(0.0)
    migration_contribution.append(0.0)
    
    year_exceed_million = None
    
    # Run simulation
    # We will simulate up to 100 years or until it exceeds 1 million,
    # but the primary report is for the specified 'years' (50 years).
    max_sim_years = max(years, 200) # Ensure we simulate long enough to find when it hits 1M
    
    for year in range(1, max_sim_years + 1):
        prev_pop = population[-1]
        
        # Calculate growth and migration for the year
        added = prev_pop * growth_rate
        removed = prev_pop * migration_loss
        current_pop = prev_pop + added - removed
        
        years_list.append(year)
        population.append(current_pop)
        growth_contribution.append(added)
        migration_contribution.append(removed)
        
        if current_pop >= 1_000_000 and year_exceed_million is None:
            year_exceed_million = year
            
    # Create DataFrames: one for the 50-year report, one for the full simulation
    df_full = pd.DataFrame({
        'Year': years_list,
        'Population': population,
        'Growth_Added': growth_contribution,
        'Migration_Loss': migration_contribution
    })
    
    df_report = df_full[df_full['Year'] <= years].copy()
    
    return df_report, df_full, year_exceed_million

def main():
    print("=" * 60)
    print("         AI POPULATION GROWTH ANALYZER")
    print("=" * 60)
    
    target_years = 50
    df_report, df_full, year_exceed_million = simulate_population(target_years)
    
    final_pop = df_report.iloc[-1]['Population']
    
    print(f"Simulation Duration: {target_years} Years")
    print(f"Starting Population: 50,000 residents\n")
    
    print(f"--- Results after {target_years} Years ---")
    print(f"Final Population: {final_pop:,.2f} (~{round(final_pop):,})")
    print("-" * 60)
    
    print("--- Milestones ---")
    if year_exceed_million:
        print(f"Year population exceeds 1 Million: Year {year_exceed_million}")
    else:
        print("Population did not exceed 1 Million in the simulation window.")
    print("=" * 60)
    
    # Save the 50-year yearly report to CSV
    df_report.to_csv("population_report.csv", index=False)
    print("Yearly report saved as 'population_report.csv'")
    
if __name__ == '__main__':
    main()
