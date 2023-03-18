import matplotlib.pyplot as plt

def draw_chicken():
    fig, ax = plt.subplots()

    # Draw body
    body = plt.Circle((0, 0), 0.5, color='yellow')
    ax.add_artist(body)

    # Draw head
    head = plt.Circle((-0.5, 0.5), 0.25, color='yellow')
    ax.add_artist(head)

    # Draw beak
    beak = plt.Polygon([[-0.55, 0.6], [-0.75, 0.6], [-0.65, 0.7]], color='orange')
    ax.add_artist(beak)

    # Draw eyes
    left_eye = plt.Circle((-0.6, 0.65), 0.05, color='black')
    ax.add_artist(left_eye)
    right_eye = plt.Circle((-0.4, 0.65), 0.05, color='black')
    ax.add_artist(right_eye)

    # Draw wings
    left_wing = plt.Polygon([[-0.25, 0.2], [-0.75, 0.2], [-0.5, -0.1]], color='yellow')
    ax.add_artist(left_wing)
    right_wing = plt.Polygon([[0.25, 0.2], [0.75, 0.2], [0.5, -0.1]], color='yellow')
    ax.add_artist(right_wing)

    # Draw legs
    left_leg = plt.Line2D([-0.2, -0.4], [-0.5, -0.9], linewidth=3, color='orange')
    ax.add_artist(left_leg)
    right_leg = plt.Line2D([0.2, 0.4], [-0.5, -0.9], linewidth=3, color='orange')
    ax.add_artist(right_leg)

    # Set axes limits
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1, 1)

    # Remove axes
    ax.set_xticks([])
    ax.set_yticks([])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)

    plt.show()

draw_chicken()