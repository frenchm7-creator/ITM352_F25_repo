# Determine whether a list of purchases is within our budget or not.
# Name: Micah French
# Date: Oct 1, 2025

recent_purchases = [36.13, 23.87, 183.35, 22.93, 11.62]
budget = 500
total_spent = 0
for purchase in recent_purchases:
    total_spent += purchase

if total_spent > budget:
    print(f"You spent ${total_spent:.2f} and that is over your budget of ${budget:.2f}")
else:
    print(f"You spent ${total_spent:.2f} and that is within your budget of ${budget:.2f}")