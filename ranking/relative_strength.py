def calculate_relative_strength(analysis):

    return (
        analysis["weekly_return"]
        +
        analysis["monthly_return"]
    )