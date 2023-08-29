# Introduction to web framework- FLASK

This repository contains a Flask web application that demonstrates various routes for displaying messages and rendering HTML templates.

## Routes

### `/`

Displays the message "Hello HBNB!".

### `/hbnb`

Displays the message "HBNB".

### `/c/<text>`

Displays the message "C ", followed by the value of the `text` variable from the URL. The underscores `_` are replaced with spaces.

### `/python/<text>`

Displays the message "Python ", followed by the value of the `text` variable from the URL. The underscores `_` are replaced with spaces. If no `text` is provided, "is cool" is used as the default.

### `/number/<n>`

Displays the message "<n> is a number" if `n` is an integer.

### `/number_template/<n>`

Renders an HTML page with an H1 tag containing the text "Number: n". The `n` value is taken from the URL.

### `/number_odd_or_even/<n>`

Renders an HTML page with an H1 tag containing the text "Number: n is even|odd" depending on whether `n` is even or odd. The `n` value is taken from the URL.


## Template Files

The application uses template files for rendering HTML content.

