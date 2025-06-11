#!/usr/bin/env python3
"""Temperature Converter: Fahrenheit ↔ Celsius (IPO model demonstration)."""

from typing import Literal


def calculate_celsius(fahrenheit: float) -> float:
    """Convert °F to °C."""
    return (fahrenheit - 32) * 5 / 9


def calculate_fahrenheit(celsius: float) -> float:
    """Convert °C to °F."""
    return celsius * 9 / 5 + 32


def get_choice() -> Literal["C", "F"]:
    """Prompt user until a valid conversion choice is entered."""
    while True:
        choice = input("Enter F to convert to Fahrenheit or C to convert to Celsius: ").strip().upper()
        if choice in ("C", "F"):
            return choice
        print("⚠️  Please enter only 'C' or 'F'.")


def get_temperature(label: str) -> float:
    """Prompt user until a numeric temperature is entered."""
    while True:
        raw = input(f"Enter {label} temperature: ").strip()
        try:
            return float(raw)
        except ValueError:
            print("⚠️  Please enter a number (e.g., 36.6).")


def display_result(src_temp: float, src_label: str, dst_temp: float, dst_label: str) -> None:
    """Nicely print the conversion result."""
    print(f"\n{src_temp:.2f}°{src_label[0]} is {dst_temp:.2f}°{dst_label[0]}\n")


def main() -> None:
    """Coordinator function implementing the IPO flow."""
    choice = get_choice()

    if choice == "C":                                        # convert to Celsius
        fahrenheit = get_temperature("Fahrenheit")
        result = calculate_celsius(fahrenheit)
        display_result(fahrenheit, "Fahrenheit", result, "Celsius")
    else:                                                    # convert to Fahrenheit
        celsius = get_temperature("Celsius")
        result = calculate_fahrenheit(celsius)
        display_result(celsius, "Celsius", result, "Fahrenheit")


if __name__ == "__main__":
    main()
