#!/usr/bin/env python
# coding: utf-8

# ## Initialize PyGame window

# In[ ]:


import pygame
import random
import math
pygame.init()


# ## Set Window Parameters

# In[ ]:


WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 700
SIDE_PANEL_WIDTH = 300

class WindowInformation:
    # Define Colors
    COLORS = {
        'RED': (255, 99, 71),        # Tomato Red
        'GREEN': (34, 139, 34),      # Forest Green
        'BLUE': (30, 144, 255),      # Dodger Blue
        'WHITE': (255, 255, 255),
        'BLACK': (0, 0, 0),
        'GREY': (105, 105, 105),     # Dim Grey
        'LIGHT_GREY': (169, 169, 169),# Dark Grey
        'DARK_GREY': (40, 40, 40),    # Very Dark Grey for Side Panel
        'YELLOW': (255, 215, 0),      # Gold
        'PURPLE': (138, 43, 226),     # Blue Violet
        'ORANGE': (255, 140, 0),      # Dark Orange
        'CYAN': (0, 255, 255),        # Cyan for additional indicators
    }

    BACKGROUND_COLOR = COLORS['DARK_GREY']
    SIDE_PANEL_COLOR = COLORS['GREY']
    FONT_COLOR = COLORS['WHITE']
    INFO_FONT_SIZE = 20
    TITLE_FONT_SIZE = 30

    HORIZONTAL_PADDING = 50     # Added Missing Attribute
    VERTICAL_PADDING = 50       # Added Missing Attribute

    FONT = pygame.font.SysFont('Arial', INFO_FONT_SIZE)
    TITLE_FONT = pygame.font.SysFont('Arial', TITLE_FONT_SIZE, bold=True)

    # Gradients for bars
    GREYS = [
        COLORS['GREY'],
        COLORS['LIGHT_GREY'],
        COLORS['DARK_GREY']
    ]

    def __init__(self, width, height, lst):
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Sorting Algorithm Visualizer")
        self.set_list(lst)

    def set_list(self, lst):
        self.lst = lst
        self.min_value = min(lst)
        self.max_value = max(lst)

        # Calculate block dimensions
        self.block_width = round((self.width - SIDE_PANEL_WIDTH - 2 * self.HORIZONTAL_PADDING) / len(lst))
        self.block_height = math.floor((self.height - 2 * self.VERTICAL_PADDING) / (self.max_value - self.min_value + 1))
        self.x_start = SIDE_PANEL_WIDTH + self.HORIZONTAL_PADDING // 2

def show_text(surface, text, font, color, x, y):
    text_render = font.render(text, True, color)
    surface.blit(text_render, (x, y))

def draw(draw_info, algo_name, ascending):
    # Fill background
    draw_info.window.fill(draw_info.BACKGROUND_COLOR)

    # Draw Side Panel
    pygame.draw.rect(draw_info.window, draw_info.SIDE_PANEL_COLOR, (0, 0, SIDE_PANEL_WIDTH, draw_info.height))

    # Titles
    show_text(draw_info.window, "Sorting Visualizer", draw_info.TITLE_FONT, draw_info.FONT_COLOR, 20, 20)
    show_text(draw_info.window, f"Algorithm: {algo_name}", draw_info.FONT, draw_info.FONT_COLOR, 20, 70)
    show_text(draw_info.window, f"Order: {'Ascending' if ascending else 'Descending'}", draw_info.FONT, draw_info.FONT_COLOR, 20, 110)

    # Instructions
    control_instructions = [
        "Controls:",
        "R - Reset",
        "SPACE - Start Sorting",
        "A - Ascending",
        "D - Descending",
    ]

    algo_instructions = [
        "Algorithms:",
        "B - Bubble Sort",
        "I - Insertion Sort",
        "M - Merge Sort",
        "Q - Quick Sort",
        "S - Selection Sort",
        "H - Heap Sort",
        "C - Counting Sort",
        "T - Radix Sort",
        "U - Bucket Sort",
    ]

    # Draw Control Instructions
    y_offset = 150
    for instr in control_instructions:
        show_text(draw_info.window, instr, draw_info.FONT, draw_info.FONT_COLOR, 20, y_offset)
        y_offset += 35  # Increased spacing

    # Draw Algorithm Instructions
    y_offset += 10  # Extra spacing between control and algorithm sections
    for instr in algo_instructions:
        show_text(draw_info.window, instr, draw_info.FONT, draw_info.FONT_COLOR, 20, y_offset)
        y_offset += 35  # Increased spacing

    # Draw the list
    draw_list(draw_info)
    pygame.display.update()

def draw_list(draw_info, color_positions={}, clear_background=False):
    lst = draw_info.lst
    if clear_background:
        pygame.draw.rect(draw_info.window, draw_info.BACKGROUND_COLOR, 
                         (SIDE_PANEL_WIDTH, 0, draw_info.width - SIDE_PANEL_WIDTH, draw_info.height))
    
    for i, val in enumerate(lst):
        x = draw_info.x_start + i * draw_info.block_width
        height = (val - draw_info.min_value + 1) * draw_info.block_height
        y = draw_info.height - height - draw_info.VERTICAL_PADDING

        color = draw_info.GREYS[i % 3]
        
        if i in color_positions:
            color = color_positions[i]
        
        pygame.draw.rect(draw_info.window, color, (x, y, draw_info.block_width, height))
    
    if clear_background:
        pygame.display.update()

def random_list_gen(n, min_value, max_value):
    return [random.randint(min_value, max_value) for _ in range(n)]

# Sorting Algorithms (Generators)

## Define Sorting Algorithms
# In[ ]:


def bubble_sort(draw_info, ascending=True):
    lst = draw_info.lst
    n = len(lst)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            num1 = lst[j]
            num2 = lst[j + 1]
            if (num1 > num2 and ascending) or (num1 < num2 and not ascending):
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                draw_list(draw_info, {j: draw_info.COLORS['GREEN'], j + 1: draw_info.COLORS['RED']}, True)
                yield True
    return lst

def insertion_sort(draw_info, ascending=True):
    lst = draw_info.lst
    for i in range(1, len(lst)):
        current_val = lst[i]
        pos = i
        while pos > 0 and ((lst[pos - 1] > current_val and ascending) or (lst[pos - 1] < current_val and not ascending)):
            lst[pos] = lst[pos - 1]
            pos -= 1
            lst[pos] = current_val
            draw_list(draw_info, {pos: draw_info.COLORS['GREEN'], pos + 1: draw_info.COLORS['RED']}, True)
            yield True
    return lst

def merge_sort(draw_info, ascending=True, first=0, last=None):
    lst = draw_info.lst
    if last is None:
        last = len(lst)
    if last - first > 1:
        mid = (first + last) // 2
        yield from merge_sort(draw_info, ascending, first, mid)
        yield from merge_sort(draw_info, ascending, mid, last)
        left = lst[first:mid]
        right = lst[mid:last]
        i = j = 0
        for k in range(first, last):
            color_positions = {}
            if i < len(left):
                color_positions[first + i] = draw_info.COLORS['GREEN']
            if j < len(right):
                color_positions[mid + j] = draw_info.COLORS['RED']
            if i < len(left) and (j >= len(right) or (left[i] < right[j] and ascending) or (left[i] > right[j] and not ascending)):
                lst[k] = left[i]
                i += 1
            else:
                lst[k] = right[j]
                j += 1
            draw_list(draw_info, color_positions, clear_background=True)
            yield True
    return lst

def quick_sort(draw_info, ascending=True, first=0, last=None):
    lst = draw_info.lst
    if last is None:
        last = len(lst) - 1
    if first >= last:
        return lst
    pivot = lst[first]
    left = first + 1
    right = last
    while left <= right:
        if (lst[left] > pivot and ascending) or (lst[left] < pivot and not ascending):
            if (lst[right] < pivot and ascending) or (lst[right] > pivot and not ascending):
                lst[left], lst[right] = lst[right], lst[left]
                draw_list(draw_info, {left: draw_info.COLORS['GREEN'], right: draw_info.COLORS['RED']}, True)
                yield True
        if (lst[left] <= pivot and ascending) or (lst[left] >= pivot and not ascending):
            left += 1
        if (lst[right] >= pivot and ascending) or (lst[right] <= pivot and not ascending):
            right -= 1
    lst[first], lst[right] = lst[right], lst[first]
    draw_list(draw_info, {first: draw_info.COLORS['ORANGE'], right: draw_info.COLORS['PURPLE']}, True)
    yield True
    yield from quick_sort(draw_info, ascending, first, right - 1)
    yield from quick_sort(draw_info, ascending, right + 1, last)
    return lst

def selection_sort(draw_info, ascending=True):
    lst = draw_info.lst
    n = len(lst)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if (lst[j] < lst[min_idx] and ascending) or (lst[j] > lst[min_idx] and not ascending):
                min_idx = j
            draw_list(draw_info, {i: draw_info.COLORS['GREEN'], j: draw_info.COLORS['RED'], min_idx: draw_info.COLORS['BLUE']}, True)
            yield True
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
        draw_list(draw_info, {i: draw_info.COLORS['GREEN'], min_idx: draw_info.COLORS['RED']}, True)
        yield True
    return lst

def heapify(draw_info, n, i, ascending=True):
    lst = draw_info.lst
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and ((lst[l] > lst[largest] and ascending) or (lst[l] < lst[largest] and not ascending)):
        largest = l
    if r < n and ((lst[r] > lst[largest] and ascending) or (lst[r] < lst[largest] and not ascending)):
        largest = r
    if largest != i:
        lst[i], lst[largest] = lst[largest], lst[i]
        draw_list(draw_info, {i: draw_info.COLORS['GREEN'], largest: draw_info.COLORS['RED']}, True)
        yield True
        yield from heapify(draw_info, n, largest, ascending)

def heap_sort(draw_info, ascending=True):
    lst = draw_info.lst
    n = len(lst)
    for i in range(n // 2 - 1, -1, -1):
        yield from heapify(draw_info, n, i, ascending)
    for i in range(n - 1, 0, -1):
        lst[0], lst[i] = lst[i], lst[0]
        draw_list(draw_info, {0: draw_info.COLORS['GREEN'], i: draw_info.COLORS['RED']}, True)
        yield True
        yield from heapify(draw_info, i, 0, ascending)
    return lst

def counting_sort(draw_info, ascending=True):
    lst = draw_info.lst
    max_val = max(lst)
    min_val = min(lst)
    range_of_elements = max_val - min_val + 1
    count = [0] * range_of_elements

    # Count each element
    for i in range(len(lst)):
        count[lst[i] - min_val] += 1
        draw_list(draw_info, {i: draw_info.COLORS['RED']}, True)
        yield True

    # Cumulative count
    for i in range(1, len(count)):
        count[i] += count[i - 1]
        draw_list(draw_info, {i: draw_info.COLORS['YELLOW']}, True)
        yield True

    output = [0] * len(lst)

    # Build the output list
    for i in range(len(lst) -1, -1, -1):
        current = lst[i]
        count[current - min_val] -= 1
        output[count[current - min_val]] = current
        draw_list(draw_info, {i: draw_info.COLORS['PURPLE'], count[current - min_val]: draw_info.COLORS['GREEN']}, True)
        yield True

    # Copy the output to lst
    for i in range(len(lst)):
        lst[i] = output[i]
        draw_list(draw_info, {i: draw_info.COLORS['CYAN']}, True)
        yield True

    return lst

def radix_sort(draw_info, ascending=True):
    lst = draw_info.lst
    max_val = max(lst)
    exp = 1  # Exponent to extract each digit

    while max_val // exp > 0:
        count = [0] * 10

        # Store count of occurrences in count[]
        for i in range(len(lst)):
            index = (lst[i] // exp) % 10
            count[index] += 1
            draw_list(draw_info, {i: draw_info.COLORS['RED']}, True)
            yield True

        # Change count[i] so that count[i] contains actual position of this digit in output[]
        for i in range(1, 10):
            count[i] += count[i - 1]
            draw_list(draw_info, {i: draw_info.COLORS['YELLOW']}, True)
            yield True

        # Build the output array
        output = [0] * len(lst)
        for i in range(len(lst) -1, -1, -1):
            index = (lst[i] // exp) % 10
            count[index] -= 1
            output[count[index]] = lst[i]
            draw_list(draw_info, {i: draw_info.COLORS['PURPLE'], count[index]: draw_info.COLORS['GREEN']}, True)
            yield True

        # Copy the output array to lst, so that lst now contains sorted numbers according to current digit
        for i in range(len(lst)):
            lst[i] = output[i]
            draw_list(draw_info, {i: draw_info.COLORS['CYAN']}, True)
            yield True

        exp *= 10

    return lst

def bucket_sort(draw_info, ascending=True):
    lst = draw_info.lst
    num_buckets = 10
    max_val = max(lst)
    min_val = min(lst)
    range_of_elements = (max_val - min_val) / num_buckets if num_buckets else 1

    # Create empty buckets
    buckets = [[] for _ in range(num_buckets)]

    # Put array elements in different buckets
    for i in range(len(lst)):
        if range_of_elements == 0:
            bucket_index = 0
        else:
            bucket_index = int((lst[i] - min_val) / range_of_elements)
            if bucket_index == num_buckets:
                bucket_index -= 1
        buckets[bucket_index].append(lst[i])
        draw_list(draw_info, {i: draw_info.COLORS['RED']}, True)
        yield True

    # Sort individual buckets using built-in sorted for simplicity
    for i in range(num_buckets):
        if ascending:
            buckets[i] = sorted(buckets[i])
        else:
            buckets[i] = sorted(buckets[i], reverse=True)
        draw_list(draw_info, {i: draw_info.COLORS['YELLOW']}, True)
        yield True

    # Concatenate all buckets into lst
    index = 0
    for i in range(num_buckets):
        for num in buckets[i]:
            lst[index] = num
            draw_list(draw_info, {index: draw_info.COLORS['GREEN']}, True)
            yield True
            index += 1

    return lst



# In[ ]:


## Run the main loop


# In[ ]:


def main():
    n = 60
    min_value = 1
    max_value = 100

    lst = random_list_gen(n, min_value, max_value)
    info = WindowInformation(WINDOW_WIDTH, WINDOW_HEIGHT, lst)

    sorting = False
    ascending = True
    
    running = True
    clock = pygame.time.Clock()

    algo = bubble_sort
    algo_name = "Bubble Sort"
    algo_gen = None

    while running:
        clock.tick(60)
    
        if sorting:
            try:
                next(algo_gen)
            except StopIteration:
                sorting = False
        else:
            draw(info, algo_name, ascending)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type != pygame.KEYDOWN:
                continue
            if event.key == pygame.K_r:
                lst = random_list_gen(n, min_value, max_value)
                info.set_list(lst)
                sorting = False
            elif not sorting and event.key == pygame.K_SPACE:
                sorting = True
                algo_gen = algo(info, ascending)
            elif not sorting and event.key == pygame.K_a:
                ascending = True
            elif not sorting and event.key == pygame.K_d:
                ascending = False
            elif not sorting and event.key == pygame.K_i:
                algo = insertion_sort
                algo_name = "Insertion Sort"
            elif not sorting and event.key == pygame.K_b:
                algo = bubble_sort
                algo_name = "Bubble Sort"
            elif not sorting and event.key == pygame.K_m:
                algo = merge_sort
                algo_name = "Merge Sort"
            elif not sorting and event.key == pygame.K_q:
                algo = quick_sort
                algo_name = "Quick Sort"
            elif not sorting and event.key == pygame.K_s:
                algo = selection_sort
                algo_name = "Selection Sort"
            elif not sorting and event.key == pygame.K_h:
                algo = heap_sort
                algo_name = "Heap Sort"
            elif not sorting and event.key == pygame.K_c:
                algo = counting_sort
                algo_name = "Counting Sort"
            elif not sorting and event.key == pygame.K_t:
                algo = radix_sort
                algo_name = "Radix Sort"
            elif not sorting and event.key == pygame.K_u:
                algo = bucket_sort
                algo_name = "Bucket Sort"
                
    pygame.quit()

if __name__ == "__main__":
    main()

