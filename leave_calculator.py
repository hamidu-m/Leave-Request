from datetime import datetime


def calculate_accrued_leave(hire_date_str, current_date_str=None):
    """Calculates total leave days accrued based on tenure with the company.

    Accrual rate: 1.25 days per completed/partial month (15 days / year).
    """
    # Use standard format string "%Y-%m-%d" to parse the dates
    DATE_FORMAT = "%Y-%m-%d"

    # If current_date_str is provided, parse it; otherwise, use the live system time
    if current_date_str:
        current_date = datetime.strptime(current_date_str, DATE_FORMAT)
    else:
        current_date = datetime.now()

    # Move this down so current_date is already defined before parsing hire_date
    hire_date = datetime.strptime(hire_date_str, DATE_FORMAT)

    if hire_date > current_date:
        raise ValueError("Hire date cannot be in the future.")

    # Calculate total completed months of tenure
    years_diff = current_date.year - hire_date.year
    months_diff = current_date.month - hire_date.month
    total_months = (years_diff * 12) + months_diff

    # Include partial month if current day of month is >= hire day of month
    if current_date.day < hire_date.day and total_months > 0:
        total_months -= 1

    # 3. RESTART LOGIC: Use modulo to reset months tracking after every 12 months
    current_cycle_months = total_months % 12

    # Monthly accrual rate: 15 days / 12 months = 1.25
    MONTHLY_RATE = 1.25
    accrued_days = current_cycle_months * MONTHLY_RATE

    return round(accrued_days, 2), current_cycle_months


# --- Test scenarios ---

# Example 1: Passing None triggers the live, automatically updating date
hire_date_1 = "2026-09-09"
leave_days, months = calculate_accrued_leave(hire_date_1, current_date_str=None)

print(f"Today's Date: {datetime.now().strftime('%Y-%m-%d')}")
print(f"Agent 1 (Tenure: {months} month(s)) -> Accrued Leave: {leave_days} days")

    #
    # # Example 2: Agent hired 6 months ago
    # hire_date_2 = "2026-04-09"
    # leave_days, months = calculate_accrued_leave(hire_date_2, today)
    # print(f"Agent 2 (Tenure: {months} month(s)) -> Accrued Leave: {leave_days} days")
    #
    # # Example 3: Agent hired 1 year ago (12 months)
    # hire_date_3 = "2025-10-09"
    # leave_days, months = calculate_accrued_leave(hire_date_3, today)
    # print(f"Agent 3 (Tenure: {months} month(s)) -> Accrued Leave: {leave_days} days")