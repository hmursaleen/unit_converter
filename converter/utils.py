# Conversion data
LENGTH_CONVERSIONS = {
    'millimeter': 0.001,
    'centimeter': 0.01,
    'meter': 1,
    'kilometer': 1000,
    'inch': 0.0254,
    'foot': 0.3048,
    'yard': 0.9144,
    'mile': 1609.34,
}

WEIGHT_CONVERSIONS = {
    'milligram': 0.000001,
    'gram': 0.001,
    'kilogram': 1,
    'ounce': 0.0283495,
    'pound': 0.453592,
}



def convert_length(value, from_unit, to_unit):
    """
    Convert length from one unit to another.

    :param value: float, the value to convert
    :param from_unit: str, the unit to convert from
    :param to_unit: str, the unit to convert to
    :return: float, the converted value
    :raises ValueError: if inputs are invalid
    """
    if not isinstance(value, (int, float)):
        raise ValueError("Value must be a numeric type.")

    if not from_unit or not to_unit:
        raise ValueError("Both 'from_unit' and 'to_unit' must be provided.")

    if from_unit == to_unit:
        return value

    if from_unit not in LENGTH_CONVERSIONS or to_unit not in LENGTH_CONVERSIONS:
        raise ValueError(f"Invalid units for length conversion: {from_unit}, {to_unit}")

    # Convert input value to meters (base unit)
    value_in_meters = value * LENGTH_CONVERSIONS[from_unit]

    # Convert from meters to the target unit
    return round(value_in_meters / LENGTH_CONVERSIONS[to_unit], 6)








def convert_weight(value, from_unit, to_unit):
    """
    Convert weight from one unit to another.

    :param value: float, the value to convert
    :param from_unit: str, the unit to convert from
    :param to_unit: str, the unit to convert to
    :return: float, the converted value
    :raises ValueError: if inputs are invalid
    """
    if not isinstance(value, (int, float)):
        raise ValueError("Value must be a numeric type.")

    if not from_unit or not to_unit:
        raise ValueError("Both 'from_unit' and 'to_unit' must be provided.")

    if from_unit == to_unit:
        return value

    if from_unit not in WEIGHT_CONVERSIONS or to_unit not in WEIGHT_CONVERSIONS:
        raise ValueError(f"Invalid units for weight conversion: {from_unit}, {to_unit}")

    # Convert input value to kilograms (base unit)
    value_in_kilograms = value * WEIGHT_CONVERSIONS[from_unit]

    # Convert from kilograms to the target unit
    return round(value_in_kilograms / WEIGHT_CONVERSIONS[to_unit], 6)









def convert_temperature(value, from_unit, to_unit):
    """
    Convert temperature from one unit to another.

    :param value: float, the temperature value to convert
    :param from_unit: str, the unit to convert from (Celsius, Fahrenheit, Kelvin)
    :param to_unit: str, the unit to convert to (Celsius, Fahrenheit, Kelvin)
    :return: float, the converted temperature value
    :raises ValueError: if inputs are invalid
    """
    if not isinstance(value, (int, float)):
        raise ValueError("Value must be a numeric type.")

    if not from_unit or not to_unit:
        raise ValueError("Both 'from_unit' and 'to_unit' must be provided.")

    if from_unit == to_unit:
        return value

    # Celsius to other units
    if from_unit == "Celsius":
        if to_unit == "Fahrenheit":
            return round((value * 9/5) + 32, 6)
        elif to_unit == "Kelvin":
            return round(value + 273.15, 6)

    # Fahrenheit to other units
    elif from_unit == "Fahrenheit":
        if to_unit == "Celsius":
            return round((value - 32) * 5/9, 6)
        elif to_unit == "Kelvin":
            return round(((value - 32) * 5/9) + 273.15, 6)

    # Kelvin to other units
    elif from_unit == "Kelvin":
        if to_unit == "Celsius":
            return round(value - 273.15, 6)
        elif to_unit == "Fahrenheit":
            return round(((value - 273.15) * 9/5) + 32, 6)

    raise ValueError(f"Invalid units for temperature conversion: {from_unit}, {to_unit}")

