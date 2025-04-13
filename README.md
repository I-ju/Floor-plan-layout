# Floor-plan-layout
Project Overview：
This project is a Django-based web application that simulates a floor plan layout tool. The app displays a background image and allows users to add, move, and resize squares representing furniture. The positions and sizes of the squares are automatically saved in a database so that the layout can be restored when the page is reloaded. Additionally, the system prevents overlapping of the squares.

Technologies Used：
Python & Django for the backend
SQLite as the database
JavaScript with jQuery and jQuery UI for interactive front-end features

Features：
• Dynamic Square Creation: Users can create squares with default dimensions and a preset color.
• Draggable and Resizable: The squares can be moved and resized.
• Layout Persistence: Every change is saved to the database via AJAX, and the layout is restored when the page reloads.
• Overlap Prevention: The app checks to ensure that squares do not overlap. If an overlap is detected, it displays an error message.
• Reset Layout: A reset function allows the user to clear all squares and start with a clean layout.

Demo Video: https://drive.google.com/file/d/1_Zssrnp0Mao4HINi-wtdzDK0zC8nZdY-/view?usp=sharing
