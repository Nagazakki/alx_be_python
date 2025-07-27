"""
Weather Advice and Clothing Recommendation Script
Asks about weather and gives clothing advice using if/elif/else statements.
"""

print("=== Weather Clothing Advisor ===")
print()
print("What is the weather like today? (sunny, rainy, cold):")
weather = input().strip().lower()

if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I do not have recommendations for this weather.")