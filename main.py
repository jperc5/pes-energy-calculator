VERSION = "1.0.0"

# PES Energy Calculator V1 (CLI)
# Converts power + time -> energy (Wh, kWh)

def to_watts(power: float, unit: str) -> float:
    unit = unit.strip().lower()
    if unit in ["w", "watt", "watts"]:
        return power
    if unit in ["kw", "kilowatt", "kilowatts"]:
        return power * 1000.0
    raise ValueError("Power unit must be W or kW.")

def to_hours(time_value: float, unit: str) -> float:
    unit = unit.strip().lower()
    if unit in ["h", "hr", "hrs", "hour", "hours"]:
        return time_value
    if unit in ["min", "mins", "minute", "minutes"]:
        return time_value / 60.0
    raise ValueError("Time unit must be h or min.")

def calc_energy_wh(power_w: float, time_h: float) -> float:
    # W × h = Wh
    return power_w * time_h

def main():
    print(f"=== PES Energy Calculator v{VERSION} ===")

    try:
        power_value = float(input("Enter power value: ").strip())
        power_unit = input("Enter power unit (W or kW): ").strip()

        time_value = float(input("Enter time value: ").strip())
        time_unit = input("Enter time unit (h or min): ").strip()

        power_w = to_watts(power_value, power_unit)
        time_h = to_hours(time_value, time_unit)

        energy_wh = calc_energy_wh(power_w, time_h)
        energy_kwh = energy_wh / 1000.0

        print("\n--- Result ---")
        print(f"Power:  {power_w:.3f} W")
        print(f"Time:   {time_h:.4f} h")
        print(f"Energy: {energy_wh:.3f} Wh")
        print(f"        {energy_kwh:.6f} kWh")

        print("\nExplanation:")
        print("Energy = Power × Time (W × h = Wh)")

    except ValueError as e:
        print(f"\nInput error: {e}")
    except Exception as e:
        print(f"\nUnexpected error: {e}")

if __name__ == "__main__":
    main()
