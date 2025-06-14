def bmi_app():
    print("👋 Welcome to the Friendly BMI Calculator!")
    print("Let’s find out your Body Mass Index (BMI).")
    print("Choose your unit system:")
    print("1. Imperial (pounds & inches)")
    print("2. Metric (kilograms & meters)")

    choice = input("Enter 1 for Imperial or 2 for Metric: ").strip()

    if choice == '1':
        try:
            weight_lb = float(input("Enter your weight in pounds (lbs): "))
            height_in = float(input("Enter your height in inches (in): "))
            weight = weight_lb / 2.20462
            height = height_in * 0.0254
        except ValueError:
            print("Oops! That doesn’t look like a number. Try again.")
            return
    elif choice == '2':
        try:
            weight = float(input("Enter your weight in kilograms (kg): "))
            height = float(input("Enter your height in meters (m): "))
        except ValueError:
            print("Oops! That doesn’t look like a number. Try again.")
            return
    else:
        print("❌ Invalid choice. Please restart and enter 1 or 2.")
        return

    bmi = weight / (height ** 2)
    print(f"✅ Your BMI is: {bmi:.2f}")

    # Optional: add interpretation
    if bmi < 18.5:
        print("🔍 You're underweight. A snack might not hurt!")
    elif 18.5 <= bmi < 25:
        print("🎯 You're in the healthy range. Keep it up!")
    elif 25 <= bmi < 30:
        print("⚠️ You're slightly overweight. Maybe skip that extra donut?")
    else:
        print("🚨 You're in the obese range. Consider chatting with a healthcare professional.")

# Run the app
bmi_app()
