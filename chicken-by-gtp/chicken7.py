import matplotlib.pyplot as plt
import random

def draw_chicken(ax, x, y, scale):
    # Draw body
    body = plt.Circle((x, y), 0.5 * scale, color='yellow')
    ax.add_artist(body)

    # Draw head
    head = plt.Circle((x - 0.5 * scale, y + 0.5 * scale), 0.25 * scale, color='yellow')
    ax.add_artist(head)

    # Draw beak
    beak = plt.Polygon([(x - 0.5 * scale, y + 0.5 * scale), (x - 0.68 * scale, y + 0.45 * scale), (x - 0.5 * scale, y + 0.4 * scale)], color='orange')
    ax.add_artist(beak)

    # Draw eyes
    left_eye = plt.Circle((x - 0.6 * scale, y + 0.6 * scale), 0.05 * scale, color='black')
    ax.add_artist(left_eye)
    right_eye = plt.Circle((x - 0.4 * scale, y + 0.6 * scale), 0.05 * scale, color='black')
    ax.add_artist(right_eye)

    # Draw wings
    left_wing = plt.Polygon([(x - 0.25 * scale, y + 0.2 * scale), (x - 0.75 * scale, y + 0.2 * scale), (x - 0.5 * scale, y - 0.1 * scale)], color='yellow')
    ax.add_artist(left_wing)
    right_wing = plt.Polygon([(x + 0.25 * scale, y + 0.2 * scale), (x + 0.75 * scale, y + 0.2 * scale), (x + 0.5 * scale, y - 0.1 * scale)], color='yellow')
    ax.add_artist(right_wing)

    # Draw legs
    left_leg = plt.Line2D([x - 0.2 * scale, x - 0.4 * scale], [y - 0.4 * scale, y - 0.8 * scale], linewidth=3 * scale, color='orange')
    ax.add_artist(left_leg)
    right_leg = plt.Line2D([x + 0.2 * scale, x + 0.4 * scale], [y - 0.4 * scale, y - 0.8 * scale], linewidth=3 * scale, color='orange')
    ax.add_artist(right_leg)

    # Draw feet
    left_foot = plt.Line2D([x - 0.4 * scale, x - 0.6 * scale], [y - 0.8 * scale, y - 0.7 * scale], linewidth=3 * scale, color='orange')
    ax.add_artist(left_foot)
    right_foot = plt.Line2D([x + 0.4 * scale, x + 0.6 * scale], [y - 0.8 * scale, y - 0.7 * scale], linewidth=3 * scale, color='orange')
    ax.add_artist(right_foot)

fig, ax = plt.subplots()

# Set axes limits
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)

# Remove axes
ax.set_xticks([])
ax.set_yticks([])
ax.spines['top']
