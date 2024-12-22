from src.use_cases.capture_image import capture_image

if __name__ == "__main__":
    action = input("Press '1' to clock-in or '2' to clock-out: ").strip()
    if action == "1":
        action = "clock-in"
    elif action == "2":
        action = "clock-out"
    else:
        print("Invalid action. Please press '1' or '2'.")
        exit()

    print("Hit [Enter] to capture image.")
    capture_image(action)