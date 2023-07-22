"""A test case for the rotational module."""
import rotational
import numpy as np


def get_point(into: int) -> None:
    """Get point/vector and translation from user and plot.

    args:
        into: 1 for point, 2 for vector
        return: None
    """
    while True:
        try:
            point_array_split = input(
                "Enter point/vector as a list separated by spaces: "
            )
            point_array = list(map(float, point_array_split.split(" ")))
            break
        except ValueError:
            print("Invalid input. Enter point/vector as an array: ")

    while True:
        try:
            translation_array_split = input(
                "Enter translation from frame A as a list separated by spaces: "
            )
            translation_array = list(map(float, translation_array_split.split(" ")))
            break
        except ValueError:
            print("Invalid input. Enter translation as an array: ")

    while True:
        try:
            angle = float(input("Enter angle of rotation in degrees: "))
            break
        except ValueError:
            print("Invalid input. angle of rotation in degrees: ")

    if into == 1:
        rotational.point(np.array(point_array), np.array(translation_array), angle)
    else:
        rotational.vector(np.array(point_array), np.array(translation_array), angle)


# Main
run = 1
# loop to run program
while run == 1:
    # Set plot object as point or vector
    get_point(int(input("Press 1 for point. Press any other number to vector: ")))
    # loop to run program again
    while True:
        try:
            run = int(input("Press 1 to continue. Press any other number to quit: "))
            break
        except ValueError:
            print(
                "Invalid input. Press 1 to continue. Press any other number to quit: "
            )
