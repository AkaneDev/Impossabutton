import tkinter as tk
import math
import random

# Create main window
window = tk.Tk()
window.title("Impossible Button")
window.geometry("500x500")

# Initial button position
button_x, button_y = 200, 200
speed = 2  # Initial speed of the button
dx, dy = 1, 1  # Direction of movement (1 for right/down, -1 for left/up)

def update_position():
    global button_x, button_y, speed, dx, dy

    # Get mouse position relative to the window
    mouse_x = window.winfo_pointerx() - window.winfo_rootx()
    mouse_y = window.winfo_pointery() - window.winfo_rooty()

    # Calculate distance from button to mouse
    distance_x = button_x - mouse_x
    distance_y = button_y - mouse_y
    distance = math.sqrt(distance_x**2 + distance_y**2)

    if distance < 200:  # Only move if the mouse is within 200 pixels
        speed = max(2, 10 - (distance / 20))  # Adjust speed dynamically
        unit_dx = distance_x / distance if distance != 0 else 0
        unit_dy = distance_y / distance if distance != 0 else 0

        button_x += unit_dx * speed
        button_y += unit_dy * speed

        # Check for boundary collision
        if button_x <= 0 or button_x >= window.winfo_width() - 100:
            dx *= -1  # Reverse the horizontal direction
        if button_y <= 0 or button_y >= window.winfo_height() - 50:
            dy *= -1  # Reverse the vertical direction

        # Apply direction to movement
        button_x += dx * speed
        button_y += dy * speed

        # Keep button inside the window boundaries
        button_x = max(0, min(window.winfo_width() - 100, button_x))
        button_y = max(0, min(window.winfo_height() - 50, button_y))

    button.place(x=button_x, y=button_y)
    window.after(10, update_position)  # Update every 10ms

# Explosion effect
def explode():
    global button_x, button_y
    # Remove the button
    button.place_forget()

    # Display "BOOM!" text at button's position
    boom_text = tk.Label(window, text="BOOM!", font=("Arial", 50), fg="red", bg="black")
    boom_text.place(x=button_x - 100, y=button_y - 50)

    # Create random explosion "particles"
    for _ in range(50):  # Increase particles for a bigger explosion
        particle = tk.Label(window, text="*", font=("Arial", random.randint(20, 30)), fg=random.choice(['red', 'orange', 'yellow', 'green', 'blue']), bg="black")
        particle.place(x=button_x + random.randint(-100, 100), y=button_y + random.randint(-100, 100))

    # After 1 second, close the window
    window.after(1000, window.quit)  # Closes the window after the explosion

# Create button
button = tk.Button(window, text="Click Me!", font=("Arial", 14), command=explode)

# Start the movement loop
update_position()

# Run the main loop
window.mainloop()
