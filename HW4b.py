# Collaborated with Marlesha Ellis, we didnt go back and forth over github but sent our pycharm files back and forth
# over the Discord App these are the final outcomes of our work
# marlesha did an initial code but I(Austin) couldnt get it to run so I did an overhaul to get the output and a plot
# Then I passed it back to her to check it againg.
import numpy as np    # numpy used for math and linspace (for even distribution) and np.isclose
from scipy.optimize import fsolve   # used for finding the roots of our equations
import matplotlib.pyplot as plt   # used for plotting

# extra plot for visuals on seeing the lines, where the lines cross are intersecting lines and where they cross zero
# are the roots, I used a range of x=0 to x=4 for finding my roots and intersecting points

x = np.linspace(-5, 5, 1000)
y1 = x - 3 * np.cos(x)
y2 = np.cos(2 * x) * x ** 3

plt.plot([-5, 5], [0, 0], linestyle='-', color='black', label='x=0')  # 15,16 made the 0, 0 grid lines for the graph
plt.plot([0, 0], [-100, 100], linestyle='-', color='black', label='y=0')
plt.plot(x, y1, label='x - 3*cos(x)')     # 17,18 plot our 2 lines
plt.plot(x, y2, label='cos(2x)*x^3')
plt.legend()
plt.show()


def equation1(x):
    """This function defines the first equation"""
    return x - 3 * np.cos(x)


def equation2(x):
    """This function defines the second equation"""
    return np.cos(2 * x) * x ** 3


def find_roots(equation, initial_guesses):
    """Function used to find the roots when given an equation and initial guesses by running iterations to find
    where the lines reach or within tolerance distance from the x axis"""
    roots = []
    for x0 in initial_guesses:
        root = fsolve(equation, x0)
        if len(roots) == 0 or not any(np.isclose(root, existing_root, atol=1e-5) for existing_root in roots):
            roots.append(root[0])
    return roots


def find_intersection_points():
    """This function calls the find roots function to find the roots using our chosen intitial guesses. Then it finds
     the intersection points of the two lines by finding where the difference =0"""
    # Initial guesses for values of the roots
    initial_guesses = [0, 2, 4]

    # Find the roots for the first equation
    roots_equation1 = find_roots(equation1, initial_guesses)

    # Find the roots for the second equation
    roots_equation2 = find_roots(equation2, initial_guesses)

    # Find intersection points
    def diff(x):
        """Function used just for finding the difference in the equations at a given x value"""
        return equation1(x) - equation2(x)

    x_values = np.linspace(0, 4, 1000)
    intersection_points = []
    for i in range(len(x_values) - 1):
        if diff(x_values[i]) == 0 or diff(x_values[i + 1]) == 0 or diff(x_values[i]) * diff(x_values[i + 1]) < 0:
            intersection_points.append(fsolve(diff, x_values[i]))
    # The for loop determines the intersection points by checking the differerences in the equations at different x values
    # then if true places them into a list
    # Create intersection_points_list to make it look a little better when printed down below
    intersection_points_list = [point[0] for point in intersection_points]

    return roots_equation1, roots_equation2, intersection_points, intersection_points_list


if __name__ == "__main__":
    """ Main function to find the roots and intersection points of the two lines in a range of x=0 to x=4"""
    roots_equation1, roots_equation2, intersection_points, intersection_points_list = find_intersection_points()

    # Print the roots and intersection points
    print("In a range of x=0 to x=4")
    print("Roots of x - 3 * cos(x):", roots_equation1)
    print("Roots of cos(2 * x) * x^3:", roots_equation2)

    print("Intersection points:", intersection_points_list)
