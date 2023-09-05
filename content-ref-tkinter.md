Creating a GUI using the Tkinter library in Python is a great way to build graphical user interfaces for your Python applications. Here's an example script and a brief tutorial on creating a simple GUI window with a button using Tkinter:

```python
import tkinter as tk

# Create the main application window
root = tk.Tk()
root.title("Simple Tkinter GUI")

# Create a label widget
label = tk.Label(root, text="Hello, Tkinter!")

# Pack the label widget into the window
label.pack()

# Create a function to be called when the button is clicked
def button_click():
    label.config(text="Button Clicked!")

# Create a button widget
button = tk.Button(root, text="Click Me", command=button_click)

# Pack the button widget into the window
button.pack()

# Start the Tkinter main loop
root.mainloop()
```

Now, let's break down the key components of this script:

1. Import Tkinter: Import the Tkinter library with the alias `tk`.

2. Create the main window: Use `tk.Tk()` to create the main application window and set its title with `root.title()`.

3. Create a Label: Create a label widget with `tk.Label()` and set its text using the `text` parameter.

4. Pack the Label: Use the `pack()` method to place the label widget inside the window.

5. Create a Button: Create a button widget with `tk.Button()`, set its text, and specify a function to be called when it's clicked using the `command` parameter.

6. Pack the Button: Place the button widget in the window using the `pack()` method.

7. Define the button_click() Function: This function will be called when the button is clicked and will update the label's text.

8. Start the Tkinter Main Loop: Finally, use `root.mainloop()` to start the main event loop, which keeps the GUI application running and responsive.

To run this script, make sure you have Python and Tkinter installed. Save the code in a .py file and execute it. You should see a simple GUI window with a label and a button. When you click the button, the label's text will change.

This is just a basic example to get you started with Tkinter. You can create more complex GUIs by adding more widgets and customizing their behavior and appearance. Tkinter has many other widgets like Entry, Canvas, Listbox, etc., and you can use geometry managers like `pack()`, `grid()`, or `place()` for layout management.
