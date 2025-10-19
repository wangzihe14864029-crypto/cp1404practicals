"""
CP1404 Practical
Hex colour lookup program
Estimate: 25 minutes
Actual: 33 minutes
"""

COLOR_CODES = {
    "amber": "#ffbf00",
    "antiquewhite": "#faebd7",
    "aqua": "#00ffff",
    "aquamarine": "#7fffd4",
    "azure": "#f0ffff",
    "beige": "#f5f5dc",
    "bisque": "#ffe4c4",
    "black": "#000000",
    "blanchedalmond": "#ffebcd",
    "blue": "#0000ff"
}


def main():
    """Prompt user for color name and display hex code."""
    name = input("Enter color name: ").strip().lower()
    while name != "":
        code = COLOR_CODES.get(name)
        if code:
            print(f"{name.title()} is {code}")
        else:
            print("Invalid color name")
        name = input("Enter color name: ").strip().lower()

main()
