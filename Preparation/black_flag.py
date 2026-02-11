plunder_days = int(input())
daily_plunder = int (input())
expected_plunder = int(input())
current_plunder = 0

for i in range(1,plunder_days + 1):
    current_plunder += daily_plunder
    if i % 3 == 0:
        current_plunder += daily_plunder*0.5
    if i % 5 == 0:
        current_plunder -= (current_plunder * 0.3)


if current_plunder >= expected_plunder:
    print(f"Ahoy! {current_plunder:.2f} plunder gained.")
else:
    print(f"Collected only {((100*current_plunder)/expected_plunder):.2f}% of the plunder.")