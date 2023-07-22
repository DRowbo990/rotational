"""transform point or vector in 3D space by rotation matrix"""
import matplotlib.pyplot as plt
import numpy as np
from numpy import typing as npt


#########################################################################################
# Method to plot vector
def vector_old(
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


#########################################################################################
def vector(
    head: npt.NDArray[np.float64],
    translation: npt.NDArray[np.float64],
    angle: float,
) -> None:
    """Plots an axis and a rotated axis with a given vector in 3D space.

    Args:
    base: The base of the vector in x y z.
    head: The head of the vector in x y z.
    translation: The translation of the vector in x y z.
    angle: The angle of rotation in x y.
    Returns: None
    """

    # converts to np.array to make code easier to work with.
    head = np.reshape(np.array(head), (3, 1))
    translation = np.reshape(np.array(translation), (3, 1))
    angle = np.deg2rad(angle)

    # Create the rotation matrix & rotate the vector
    rotation_matrix = np.array(
        [
            [np.cos(angle), -np.sin(angle), 0],
            [np.sin(angle), np.cos(angle), 0],
            [0, 0, 1],
        ]
    )
    rotated_head = rotation_matrix.T @ head
    print(rotated_head)

    # Create a new figure and axes
    fig = plt.figure()
    axis = fig.add_subplot(111, projection="3d")

    max_range = max(
        abs(head[0, 0]),
        abs(head[1, 0]),
        abs(head[2, 0]),
        abs(rotated_head.item(0)),
        abs(rotated_head.item(1)),
        abs(rotated_head.item(2)),
    )

    # plot original axis
    axis.quiver(
        (0, 0),
        (0, 0),
        (0, 0),
        (0, max_range),
        (max_range, 0),
        (0, 0),
        color="r",
        label="Original Axis",
    )

    axis.text(
        max_range,
        0,
        0,
        "X",
        ha="right",
        va="bottom",
        color="r",
    )

    axis.text(
        0,
        max_range,
        0,
        "Y",
        ha="right",
        va="bottom",
        color="r",
    )

    # plot vector
    axis.quiver(
        (0, translation[0, 0]),
        (0, translation[1, 0]),
        (0, translation[2, 0]),
        (head[0, 0], head[0, 0]),
        (head[1, 0], head[1, 0]),
        (head[2, 0], head[2, 0]),
        color="g",
        label="Vector",
    )

    axis.text(
        head[0, 0],
        head[1, 0],
        head[2, 0],
        np.array2string(head.T),
        ha="right",
        va="bottom",
        color="r",
    )

    axis.text(
        translation[0, 0] + head[0, 0],
        translation[1, 0] + head[1, 0],
        translation[2, 0] + head[2, 0],
        np.array2string(rotated_head.T),
        ha="left",
        va="bottom",
        color="b",
    )

    # Plot the rotated coordinate frame. rotation matrix not transposed as the frame is given in frame 2.
    # This is because we start from the new_origin and then rotate the frame.
    axis.quiver(
        (translation[0, 0], translation[0, 0]),
        (translation[1, 0], translation[1, 0]),
        (translation[2, 0], translation[2, 0]),
        (
            (max_range) * rotation_matrix[0, 0],
            (max_range) * rotation_matrix[0, 1],
        ),
        (
            (max_range) * rotation_matrix[1, 0],
            (max_range) * rotation_matrix[1, 1],
        ),
        (
            (max_range) * rotation_matrix[2, 0],
            (max_range) * rotation_matrix[2, 1],
        ),
        color="b",
        label="Rotated axis",
    )

    # rotated x axis label
    axis.text(
        (translation[0, 0] + max_range * rotation_matrix[0, 0]),
        (translation[1, 0] + max_range * rotation_matrix[1, 0]),
        (translation[2, 0] + max_range * rotation_matrix[2, 0]),
        "X",
        ha="left",
        va="bottom",
        color="b",
    )

    # rotated y axis label
    axis.text(
        (translation[0, 0] + max_range * rotation_matrix[0, 1]),
        (translation[1, 0] + max_range * rotation_matrix[1, 1]),
        (translation[2, 0] + max_range * rotation_matrix[2, 1]),
        "Y",
        ha="left",
        va="bottom",
        color="b",
    )

    # Set axis limits, labels, show plot. abs() on translation to account for negative translation.
    axis.set_xlim(
        -max_range - abs(translation.item(0)), max_range + abs(translation.item(0))
    )
    axis.set_ylim(
        -max_range - abs(translation.item(1)), max_range + abs(translation.item(1))
    )
    axis.set_zlim(
        -max_range - abs(translation.item(2)), max_range + abs(translation.item(2))
    )
    axis.set_zlabel("Z")
    axis.set_title("Rotation in 3D")
    axis.legend()
    plt.show()


###################################################################################################
def point_old(
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
    print("original shape:", points.shape)
    points = np.reshape(points, (3, 1))
    print("new shape:", points.shape)
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
    rotated_point = translation + rotation_matrix @ points
    # rotated_point = translation + (np.dot(points, rotation_matrix))
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
        points[0, 0],
        points.item(1),
        points[2, 0],
        rotated_point.item(0),
        rotated_point.item(1),
        rotated_point.item(2),
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


###################################################################################################
def point(
    points: npt.NDArray[np.float64],
    translation: npt.NDArray[np.float64],
    angle: float,
) -> None:
    """Plots a point and its given rotation and translation in 3D space.

    Args:
    points: The point to be rotated in x y z.
    translation: The translation of the point in x y z.
    angle: The angle of rotation in x y.
    Returns: None
    """

    # converts to np.array to make code easier to work with
    points = np.reshape(np.array(points), (3, 1))
    translation = np.reshape(np.array(translation), (3, 1))
    angle = np.deg2rad(angle)

    # Create the rotation matrix & rotate the point. From B to A.
    rotation_matrix = np.array(
        [
            [np.cos(angle), -np.sin(angle), 0],
            [np.sin(angle), np.cos(angle), 0],
            [0, 0, 1],
        ]
    )

    # rotation matrix from A to B * (point in A - translation from A to B expressed in A).
    rotated_point = rotation_matrix.T @ (points - translation)
    print(rotated_point)

    # size axis based on furthest away point on either axis
    max_range = max(
        abs(points[0, 0]),
        abs(points[1, 0]),
        abs(points[2, 0]),
        abs(rotated_point.item(0)),
        abs(rotated_point.item(1)),
        abs(rotated_point.item(2)),
    )

    # beginning of plotting
    # Create a 3D plot. Plot the point
    fig = plt.figure()
    axis = fig.add_subplot(111, projection="3d")
    axis.scatter(points[0], points[1], points[2], c="g", marker="o", label="Point")

    # plot original axis
    axis.quiver(
        (0, 0),
        (0, 0),
        (0, 0),
        (0, max_range),
        (max_range, 0),
        (0, 0),
        color="r",
        label="Original Axis",
    )

    # original x axis label
    axis.text(
        max_range,
        0,
        0,
        "X",
        ha="right",
        va="bottom",
        color="r",
    )

    # original y axis label
    axis.text(
        0,
        max_range,
        0,
        "Y",
        ha="right",
        va="bottom",
        color="r",
    )

    # coordinates of point in o and R frame
    axis.text(
        points[0, 0],
        points[1, 0],
        points[2, 0],
        np.array2string(points.T),
        ha="right",
        va="bottom",
        color="r",
    )

    axis.text(
        points[0, 0],
        points[1, 0],
        points[2, 0],
        np.array2string(rotated_point.T),
        ha="left",
        va="bottom",
        color="b",
    )

    # Plot the rotated coordinate frame. rotation matrix not transposed as the frame is given in frame 2.
    # This is because we start from the new_origin and then rotate the frame.
    axis.quiver(
        (translation[0, 0], translation[0, 0]),
        (translation[1, 0], translation[1, 0]),
        (translation[2, 0], translation[2, 0]),
        (
            (max_range) * rotation_matrix[0, 0],
            (max_range) * rotation_matrix[0, 1],
        ),
        (
            (max_range) * rotation_matrix[1, 0],
            (max_range) * rotation_matrix[1, 1],
        ),
        (
            (max_range) * rotation_matrix[2, 0],
            (max_range) * rotation_matrix[2, 1],
        ),
        color="b",
        label="Rotated Axis",
    )

    # rotated x axis label
    axis.text(
        (translation[0, 0] + max_range * rotation_matrix[0, 0]),
        (translation[1, 0] + max_range * rotation_matrix[1, 0]),
        (translation[2, 0] + max_range * rotation_matrix[2, 0]),
        "X",
        ha="left",
        va="bottom",
        color="b",
    )

    # rotated y axis label
    axis.text(
        (translation[0, 0] + max_range * rotation_matrix[0, 1]),
        (translation[1, 0] + max_range * rotation_matrix[1, 1]),
        (translation[2, 0] + max_range * rotation_matrix[2, 1]),
        "Y",
        ha="left",
        va="bottom",
        color="b",
    )

    # Set axis limits, labels, show plot
    axis.set_xlim(
        -max_range - abs(translation.item(0)), max_range + abs(translation.item(0))
    )
    axis.set_ylim(
        -max_range - abs(translation.item(1)), max_range + abs(translation.item(1))
    )
    axis.set_zlim(
        -max_range - abs(translation.item(2)), max_range + abs(translation.item(2))
    )
    axis.set_zlabel("Z")
    axis.set_title("Rotation in 3D")
    axis.legend()
    plt.show()
