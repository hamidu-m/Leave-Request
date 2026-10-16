
import pandas
from datetime import datetime
from leave_calculator import calculate_accrued_leave

# Load the file
data_file = pandas.read_csv("data.csv")

agent_names = data_file.Name.to_list()

print(agent_names)

check_agent = input("Enter agent's name: ").title()

# Filter row for the specific agent
agent = data_file[data_file.Name == check_agent]
print(agent)

# Check if agent exists before calculating
if not agent.empty:
    # Use .values[0] to grab just the raw text inside the cell
    hire_date_1 = agent.Hire.values[0]

    # Calculate leave using the live calendar date automatically
    leave_days, months = calculate_accrued_leave(hire_date_1, current_date_str=None)

    print(
        f"\nAgent: {check_agent} (Tenure: {months} month(s)) \n Accrued Leave: {leave_days} days"
    )
else:
    print(f"\nError: Agent '{check_agent}' not found in the database.")


