# Constants and Assumptions (as defined in Plan Step 1)

# Costs
ANNUAL_BUS_RUNNING_COST = 10000.00
ANNUAL_INSURANCE_COST = 1000.00
ANNUAL_STAFF_SALARIES_BASE = 140000.00  # Base salaries, if any, separate from hourly
ANNUAL_STARLINK_COST = 20000.00

# Fuel
DIESEL_CONSUMPTION_L_PER_100KM = 13.0
# Assumption: Diesel Price
DIESEL_PRICE_PER_L = 1.50  # Currency unit per Litre

# Staff
HOURLY_PAY_PER_STAFF = 30.00
NUM_STAFF_ON_ROUTE = 2

# Sales & Market
MARKET_PENETRATION_RATE = 0.10  # 10%
AVERAGE_SALE_ORDER_VALUE = 100.00

# Operational Assumptions (can be adjusted or made into inputs later)
# These are primarily for annualizing costs and calculating overall cost/km
ASSUMED_OPERATIONAL_DAYS_PER_YEAR = 250
ASSUMED_DAILY_ROUTE_KM = 200.0  # km
ASSUMED_NUM_VILLAGES_PER_DAY = 3
ASSUMED_DRIVING_HOURS_PER_DAY = 3.5 # hours
ASSUMED_SETUP_HOURS_PER_VILLAGE = 0.75 # hours


def calculate_annual_fixed_costs():
    """Calculates the total annual fixed costs."""
    total_fixed_costs = (
        ANNUAL_BUS_RUNNING_COST +
        ANNUAL_INSURANCE_COST +
        ANNUAL_STAFF_SALARIES_BASE +
        ANNUAL_STARLINK_COST
    )
    return total_fixed_costs

def calculate_fuel_cost_per_km():
    """Calculates the cost of fuel per kilometer."""
    fuel_cost_per_100km = DIESEL_CONSUMPTION_L_PER_100KM * DIESEL_PRICE_PER_L
    return fuel_cost_per_100km / 100

def calculate_hourly_staff_cost_rate():
    """Calculates the combined hourly cost for all staff on the route."""
    return HOURLY_PAY_PER_STAFF * NUM_STAFF_ON_ROUTE

if __name__ == '__main__':
    # Initial calculations (not trip specific yet, but general rates)
    annual_fixed_costs = calculate_annual_fixed_costs()
    fuel_cost_per_km = calculate_fuel_cost_per_km()
    hourly_staff_rate = calculate_hourly_staff_cost_rate()

    print("--- General Cost Parameters ---")
    print(f"Annual Fixed Costs: ${annual_fixed_costs:,.2f}")
    print(f"Fuel Cost per KM: ${fuel_cost_per_km:.2f}")
    print(f"Hourly Staff Cost Rate (for {NUM_STAFF_ON_ROUTE} staff): ${hourly_staff_rate:.2f}/hour")
    # print("\\n--- End of Initial Setup ---") # Keep output clean for now

# --- Trip-Specific Calculation Functions ---

def calculate_trip_variable_costs(
    route_km,
    num_villages,
    driving_hours,
    setup_hours_per_village,
    fuel_cost_per_km_val,  # Renamed to avoid conflict with global
    hourly_staff_rate_val # Renamed to avoid conflict with global
):
    """
    Calculates the total variable costs for a single trip.
    Includes fuel and hourly staff costs.
    """
    # Fuel Cost for the trip
    trip_fuel_cost = route_km * fuel_cost_per_km_val

    # Staff Cost for the trip
    total_setup_hours = num_villages * setup_hours_per_village
    total_operational_hours = driving_hours + total_setup_hours
    trip_staff_cost = total_operational_hours * hourly_staff_rate_val

    total_variable_costs = trip_fuel_cost + trip_staff_cost

    return total_variable_costs, trip_fuel_cost, trip_staff_cost

def calculate_trip_revenue(
    total_population_on_route,
    penetration_rate_val=MARKET_PENETRATION_RATE, # Default to global
    avg_order_value_val=AVERAGE_SALE_ORDER_VALUE # Default to global
):
    """
    Calculates the projected revenue from a single trip.
    """
    potential_customers = total_population_on_route * penetration_rate_val
    # Assuming potential_customers can be fractional if it represents an average
    # If sales must be integer, one might use math.floor or math.ceil here
    projected_sales_orders = potential_customers # Each customer places one average order

    total_revenue = projected_sales_orders * avg_order_value_val

    return total_revenue, projected_sales_orders

if __name__ == '__main__':
    # Initial calculations (general rates)
    annual_fixed_costs = calculate_annual_fixed_costs()
    fuel_cost_per_km = calculate_fuel_cost_per_km()
    hourly_staff_rate = calculate_hourly_staff_cost_rate()

    print("--- General Cost Parameters ---")
    print(f"Annual Fixed Costs: ${annual_fixed_costs:,.2f}")
    print(f"Fuel Cost per KM: ${fuel_cost_per_km:.2f}")
    print(f"Hourly Staff Cost Rate (for {NUM_STAFF_ON_ROUTE} staff): ${hourly_staff_rate:.2f}/hour")
    print("\\n")

    # --- Example Trip Calculation ---
    print("--- Example Trip Calculation ---")
    # Define parameters for a sample trip (can be taken from user input later)
    sample_trip_route_km = ASSUMED_DAILY_ROUTE_KM # Using assumed daily values for example
    sample_trip_num_villages = ASSUMED_NUM_VILLAGES_PER_DAY
    sample_trip_driving_hours = ASSUMED_DRIVING_HOURS_PER_DAY
    sample_trip_setup_hours_per_village = ASSUMED_SETUP_HOURS_PER_VILLAGE
    sample_trip_population = 5000 # Example population for the route

    trip_variable_costs, trip_fuel_cost, trip_staff_cost = calculate_trip_variable_costs(
        route_km=sample_trip_route_km,
        num_villages=sample_trip_num_villages,
        driving_hours=sample_trip_driving_hours,
        setup_hours_per_village=sample_trip_setup_hours_per_village,
        fuel_cost_per_km_val=fuel_cost_per_km,
        hourly_staff_rate_val=hourly_staff_rate
    )

    trip_revenue, projected_sales = calculate_trip_revenue(
        total_population_on_route=sample_trip_population
        # Using default penetration rate and avg order value from constants
    )

    print(f"Sample Trip Details:")
    print(f"  Route Distance: {sample_trip_route_km} km")
    print(f"  Number of Villages: {sample_trip_num_villages}")
    print(f"  Driving Hours: {sample_trip_driving_hours} hours")
    print(f"  Setup Hours per Village: {sample_trip_setup_hours_per_village} hours")
    print(f"  Route Population: {sample_trip_population} people")
    print("\\n")
    print(f"Trip Variable Costs:")
    print(f"  Fuel Cost: ${trip_fuel_cost:,.2f}")
    print(f"  Staff Cost: ${trip_staff_cost:,.2f}")
    print(f"  Total Variable Costs for Trip: ${trip_variable_costs:,.2f}")
    print("\\n")
    print(f"Trip Projected Revenue:")
    print(f"  Projected Sales Orders: {projected_sales:.1f}") # Can be fractional
    print(f"  Total Projected Revenue: ${trip_revenue:,.2f}")

    # Profit/Loss for the trip
    trip_profit_loss = trip_revenue - trip_variable_costs
    print("\\n")
    print(f"Trip Profit/Loss: ${trip_profit_loss:,.2f}")
    print("NB: This trip P/L does not account for allocated fixed costs.")
    print("\\n")

    # --- Overall Annual & Per KM Cost Calculation ---
    print("--- Overall Annual & Per KM Cost Calculation (based on assumptions) ---")
    # Calculate total annual variable costs based on assumptions
    # 1. Annual Fuel Cost
    total_annual_km = ASSUMED_DAILY_ROUTE_KM * ASSUMED_OPERATIONAL_DAYS_PER_YEAR
    annual_fuel_cost = total_annual_km * fuel_cost_per_km

    # 2. Annual Hourly Staff Cost
    daily_total_setup_hours = ASSUMED_NUM_VILLAGES_PER_DAY * ASSUMED_SETUP_HOURS_PER_VILLAGE
    daily_total_operational_hours = ASSUMED_DRIVING_HOURS_PER_DAY + daily_total_setup_hours
    annual_operational_hours = daily_total_operational_hours * ASSUMED_OPERATIONAL_DAYS_PER_YEAR
    annual_hourly_staff_cost = annual_operational_hours * hourly_staff_rate

    total_annual_variable_costs = annual_fuel_cost + annual_hourly_staff_cost
    total_annual_operating_costs = annual_fixed_costs + total_annual_variable_costs

    overall_cost_per_km = 0
    if total_annual_km > 0:
        overall_cost_per_km = total_annual_operating_costs / total_annual_km
    else:
        print("Cannot calculate overall cost per km as total annual km is zero.")

    print(f"Assumptions for Annual Calculation:")
    print(f"  Operational Days per Year: {ASSUMED_OPERATIONAL_DAYS_PER_YEAR}")
    print(f"  Daily Route KM: {ASSUMED_DAILY_ROUTE_KM} km")
    print(f"  Daily Driving Hours: {ASSUMED_DRIVING_HOURS_PER_DAY} hrs")
    print(f"  Villages per Day: {ASSUMED_NUM_VILLAGES_PER_DAY}")
    print(f"  Setup Hours per Village: {ASSUMED_SETUP_HOURS_PER_VILLAGE} hrs")
    print("\\n")
    print(f"Total Annual Fixed Costs: ${annual_fixed_costs:,.2f}")
    print(f"Total Annual Variable Costs (estimated):")
    print(f"  Estimated Annual Fuel Cost: ${annual_fuel_cost:,.2f} (for {total_annual_km:,} km)")
    print(f"  Estimated Annual Hourly Staff Cost: ${annual_hourly_staff_cost:,.2f} (for {annual_operational_hours:,} operational hours)")
    print(f"Total Annual Operating Costs (Fixed + Variable): ${total_annual_operating_costs:,.2f}")
    print("\\n")
    print(f"Overall Average Cost Per KM (annualized): ${overall_cost_per_km:.2f}")
    print("\\n--- End of Script ---")
