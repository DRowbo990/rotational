"""transform point or vector in 3D space by rotation matrix"""
import matplotlib.pyplot as plt
import numpy as np
from numpy import typing as npt


#########################################################################################
# Method to plot vector
def vector(
    base: npt.NDArray[np.float64],
    head: npt.NDArray[np.float64],
    translation: npt.NDArray[np.float64],
    angle: float,
) -> None:
    """Plots a given vector in 3D space.

    Args:
    base: The base of the vector in x y z.
    head: The head of the vector in x y z.
    translation: The translation of the vector in x y z.
    angle: The angle of rotation in x y.
    Returns: None

    """
    # converts to np.array to make code easier to work with
    # assigns variables
    head = np.array(head)
    base = np.array(base)
    translation = np.array(translation)
    angle = np.deg2rad(angle)
    thead = head - base

    # Create the rotation matrix & rotate the vector
    rotation_matrix = np.array(
        [
            [np.cos(angle), -np.sin(angle), 0],
            [np.sin(angle), np.cos(angle), 0],
            [0, 0, 1],
        ]
    )
    rotated_head = translation + (np.dot(thead, rotation_matrix))
    rotated_head = rotated_head + base
    print(rotated_head)

    # Create a new figure and axes
    fig = plt.figure()
    axis = fig.add_subplot(111, projection="3d")

    # Plot the original vector
    axis.quiver(
        [base[0]],
        [base[1]],
        [base[2]],
        [thead[0]],
        [thead[1]],
        [thead[2]],
        color="b",
        label=" Original Vector",
    )

    # Plot the rotated vector
    axis.quiver(
        [base[0] + translation[0]],
        [base[1] + translation[1]],
        [base[2] + translation[2]],
        [rotated_head[0] - base[0] - translation[0]],
        [rotated_head[1] - base[1] - translation[1]],
        [rotated_head[2] - base[2] - translation[2]],
        color="r",
        label="Rotated Vector",
    )

    # Set axis limits, labels, show plot
    max_range = np.max((np.max(np.abs(head)), np.max(np.abs(rotated_head))))
    axis.set_xlim(base[0] - max_range - 1, base[0] + max_range + 1)
    axis.set_ylim(base[1] - max_range - 1, base[1] + max_range + 1)
    axis.set_zlim(base[2] - max_range - 1, base[2] + max_range + 1)
    axis.set_xlabel("X")
    axis.set_ylabel("Y")
    axis.set_zlabel("Z")
    axis.set_title("3D Vector")
    axis.legend()
    plt.show()


###################################################################################################
def point(
    points: npt.NDArray[np.float64],
    translation: npt.NDArray[np.float64],
    angle: float,
) -> None:
    """Plots a point and its given rotation in 3D space.

    Args:
    points: The point to be rotated in x y z.
    translation: The translation of the point in x y z.
    angle: The angle of rotation in x y.
    Returns: None
    """

    # converts to np.array to make code easier to work with
    points = np.array(points)
    translation = np.array(translation)
    angle = np.deg2rad(angle)

    # Create the rotation matrix & rotate the point
    rotation_matrix = np.array(
        [
            [np.cos(angle), -np.sin(angle), 0],
            [np.sin(angle), np.cos(angle), 0],
            [0, 0, 1],
        ]
    )
    rotated_point = translation + (np.dot(points, rotation_matrix))
    print(rotated_point)

    # Create a 3D plot
    fig = plt.figure()
    axis = fig.add_subplot(111, projection="3d")

    # Plot the original point
    axis.scatter(
        points[0], points[1], points[2], c="r", marker="o", label="Original Point"
    )

    # Plot the rotated point
    axis.scatter(
        rotated_point[0],
        rotated_point[1],
        rotated_point[2],
        c="b",
        marker="o",
        label="Rotated Point",
    )
    # Set labels and title. Add a legend and show the plot
    max_range = max(
        points[0],
        points[1],
        points[2],
        rotated_point[0],
        rotated_point[1],
        rotated_point[2],
    )
    # Set axis limits, labels, show plot
    axis.set_xlim(-max_range - 1, max_range + 1)
    axis.set_ylim(-max_range - 1, max_range + 1)
    axis.set_zlim(-max_range - 1, max_range + 1)
    axis.set_xlabel("X")
    axis.set_ylabel("Y")
    axis.set_zlabel("Z")
    axis.set_title("Rotation in 3D")
    axis.legend()
    plt.show()
