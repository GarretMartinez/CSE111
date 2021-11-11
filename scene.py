import tkinter as tk


def main():
    # The width and height of the scene window.
    width = 800
    height = 500

    # Create the Tk root object.
    root = tk.Tk()
    root.geometry(f"{width}x{height}")

    # Create a Frame object.
    frame = tk.Frame(root)
    frame.master.title("Scene")
    frame.pack(fill=tk.BOTH, expand=1)

    # Create a canvas object that will draw into the frame.
    canvas = tk.Canvas(frame)
    canvas.pack(fill=tk.BOTH, expand=1)

    # Call the draw_scene function.
    draw_scene(canvas, 0, 0, width-1, height-1)

    
    root.mainloop()


def draw_scene(canvas, scene_left, scene_top, scene_right, scene_bottom):
    """Draw a scene in the canvas. scene_left, scene_top,
    scene_right, and scene_bottom contain the extent in
    pixels of the region where the scene should be drawn.
    Parameters
        scene_left: left side of the region; less than scene_right
        scene_top: top of the region; less than scene_bottom
        scene_right: right side of the region
        scene_bottom: bottom of the region
    Return: nothing

    If needed, the width and height of the
    region can be calculated like this:
    scene_width = scene_right - scene_left + 1
    scene_height = scene_bottom - scene_top + 1
    """
    # Call your functions here, such as draw_sky, draw_ground,
    # draw_snowman, draw_tree, draw_shrub, etc.
    sky_left = scene_left
    sky_right = scene_right
    sky_bottom = scene_bottom + 300
    sky_top = scene_top

    draw_background(canvas, sky_top, sky_right, sky_bottom, sky_left)
    draw_sun(canvas)
    draw_mountain(canvas)
    draw_lake(canvas)
    draw_reflection(canvas)
    draw_tree(canvas, 0, 0)
    draw_tree(canvas, 40, 0)
    draw_tree(canvas, -30, -40)
    draw_tree(canvas, -60, -30)
    draw_tree(canvas, 20, -40)
    draw_cloud(canvas, 0, 0)
    draw_cloud(canvas, -30, -30)


# Define more functions here, like draw_sky, draw_ground,
# draw_cloud, draw_tree, draw_kite, draw_snowflake, etc.
def draw_background(canvas, sky_top, sky_right, sky_bottom, sky_left):
    canvas.create_rectangle(sky_top, sky_right, sky_bottom, sky_left, fill="skyblue")

def draw_sun(canvas):
    x0 = 25
    y0 = 25
    x1 = 125
    y1 = 125
    canvas.create_oval(x0, y0, x1, y1, fill="yellow")

def draw_mountain(canvas):
    x0 = 250
    y0 = 50
    x1 = 550
    y1 = 500
    canvas.create_oval(x0, y0, x1, y1, fill="gray")
    x2 = -150
    y2 = 150
    x3 = 500
    y3 = 700
    canvas.create_oval(x2, y2, x3, y3, fill="gray", outline='gray')
    x4 = 350
    y4 = 100
    x5 = 1100
    y5 = 700
    canvas.create_oval(x4, y4, x5, y5, fill="gray", outline='gray')


def  draw_lake(canvas):
    x0 = 150
    y0 = 300
    x1 = 700
    y1 = 550
    canvas.create_oval(x0, y0, x1, y1, fill="cyan", outline="gray")

def draw_reflection(canvas):
    x0 = 300
    y0 = 225
    x1 = 500
    y1 = 375
    canvas.create_oval(x0, y0, x1, y1, fill="gray", outline='gray')


def draw_tree(canvas, locationx, locationy):
    x0 = 425
    y0 = 250
    x1 = 415
    y1= 300
    x2 = 435
    y2 = 300

    canvas.create_polygon(x0 + locationx, y0 + locationy, x1 + locationx, y1 + locationy, x2 + locationx, y2 + locationy, fill="dark green")

def draw_cloud(canvas, locationx, locationy):
    x0 = 600
    y0 = 50
    x1 = 700
    y1= 100
    canvas.create_oval(x0 + locationx, y0 + locationy, x1 + locationx, y1 + locationy, fill="white", outline="white")



# Call the main function so that
# this program will start executing.
main()