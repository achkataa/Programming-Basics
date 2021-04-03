

number = float(input())
measure_unit_input = input()
measure_unit_output = input()
if measure_unit_input == "mm" and measure_unit_output == "m":
    final_result = number / 1000
    print(f"{final_result:.3f}")
elif measure_unit_input == "m" and measure_unit_output == "cm":
    final_result = number * 100
    print(f"{final_result:.3f}")
elif measure_unit_input == "cm" and measure_unit_output == "mm":
    final_result = number * 10
    print(f"{final_result:.3f}")
elif measure_unit_input == "mm" and measure_unit_output == "cm":
    final_result = number / 10
    print(f"{final_result:.3f}")
elif measure_unit_input == "cm" and measure_unit_output == "m":
    final_result = number / 100
    print(f"{final_result:.3f}")
elif measure_unit_input == "m" and measure_unit_output == "mm":
    final_result = number * 1000
    print(f"{final_result:.3f}")


