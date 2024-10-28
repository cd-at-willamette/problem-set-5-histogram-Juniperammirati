from pgl import *

#1a
def create_histogram_array(data: list[int]) -> list[int]:
    max_value = max(data) if data else 0  # Find max value and handle empty list
    histogram = [0] * (max_value + 1)  # Create a list of zeros of length max(data) + 1

    for value in data:  # Loop over data
        histogram[value] += 1  # Increment the count at the index equal to the current value

    return histogram


#1b
def print_histogram(hist: list[int]) -> None: 
    for index, count in enumerate(hist):
        print(f"{index}: {'*' * count}") # showing in astricks 


#1c
def graph_histogram(hist: list[int], width: int, height: int) -> None:
    gw = GWindow(400,400)  # Create a GWindow instance big enough for the graph

    def my_rect(x, y, w, h, color):
        rect = GRect(x, y, w, h)  
        rect.set_filled(True)  
        rect.set_color(color)  
        gw.add(rect)  

    num_bars = len(hist)  # Number of bars in the histogram
    bar_width = width / num_bars  # Calculate the width of each bar 
    max_value = max(hist)  # Maximum based on teh scale
    pixel_per_value = height / max_value  # height for the histogram

    for index, value in enumerate(hist):
        bar_height = value * pixel_per_value  # Calculate the height of the bar
        x_position = index * bar_width  # X position based on the index
        y_position = height - bar_height  # Y position from the bottom

        # Draw the rectangle for the histogram bar
        my_rect(x_position, y_position, bar_width, bar_height, "red")  # Draw the rectangle
    

    #pass

# Some testing printouts for your use!
PI_DIGITS = [3,1,4,1,5,9,2,6,5,3,5,5,8,9,7,9]
hist = create_histogram_array(PI_DIGITS)
print(hist)
print_histogram(hist) # uncomment to test
graph_histogram(hist, 400, 400) # uncomment to test

