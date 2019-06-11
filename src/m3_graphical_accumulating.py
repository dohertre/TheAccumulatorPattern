"""
This module lets you practice one form of the ACCUMULATOR pattern,
namely, the "IN GRAPHICS" form which features:
  -- DRAWING OBJECTS via ACCUMULATING positions and/or sizes,
     as in:   x = x + pixels

Additionally, it emphasizes that you must
  ** DO A CONCRETE EXAMPLE BY HAND **
before you can implement a solution to the problem in Python.

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Rebekah Doherty.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


# ----------------------------------------------------------------------
# Students: As you work each of these problems, ask yourself:
#   1. Do I need a loop?
#      If so, HOW MANY LOOPS?
#
#   2. Where I need a loop, what needs to happen:
#        -- BEFORE the loop?
#        -- IN the loop?
#        -- AFTER the loop?
# ----------------------------------------------------------------------
def main():
    """ Calls the   TEST   functions in this module. """
    run_test_draw_parallel_lines()
    run_test_draw_lines()


def run_test_draw_parallel_lines():
    """ Tests the   draw_parallel_lines  function. """
    print()
    print('--------------------------------------------------')
    print('Testing the  draw_parallel_lines  function:')
    print('  See the graphics windows that pop up.')
    print('--------------------------------------------------')

    # ------------------------------------------------------------------
    # TWO tests on ONE window.
    # ------------------------------------------------------------------
    title = 'Tests 1 and 2 of DRAW_PARALLEL_LINES:'
    title = title + '  4 long lines, 7 short lines'
    window1 = rg.RoseWindow(600, 350, title)

    # Test 1:
    left_most_point = rg.Point(400, 50)
    draw_parallel_lines(7, left_most_point, 100, window1)

    # Test 2:
    left_most_point = rg.Point(50, 200)
    draw_parallel_lines(4, left_most_point, 300, window1)
    window1.close_on_mouse_click()

    # ------------------------------------------------------------------
    # A third test on ANOTHER window.
    # ------------------------------------------------------------------
    title = 'Test 3 of DRAW_PARALLEL_LINES:  12 very long lines!'
    window2 = rg.RoseWindow(500, 400, title)

    # Test 3:
    left_most_point = rg.Point(20, 20)
    draw_parallel_lines(12, left_most_point, 470, window2)

    window2.close_on_mouse_click()


def draw_parallel_lines(n, point, length, window):
    """
    What comes in: The four arguments are:
      -- A positive integer n.
      -- An rg.Point.
      -- A positive integer length.
      -- An rg.RoseWindow.
    What goes out:  Nothing (i.e., None).
    Side effects:
      See   draw_parallel_lines.pdf   in this project for pictures
        that may help you better understand the following specification:

      Draws  n  rg.Lines parallel to each other,
      all on the given rg.RoseWindow, such that:
        -- The first rg.Line has its left-most end at the given rg.Point.
        -- Each rg.Line is a horizontal line
             (i.e., parallel to the x-axis).
        -- Each rg.Line has the given length.
        -- Each rg.Line is 30 pixels below the previous rg.Line.
      Must  ** render **     but   ** NOT close **   the window.

    Type hints:
      :type n: int
      :type point: rg.Point
      :type length: int
      :type window: rg.RoseWindow
    """
    # ------------------------------------------------------------------
    # DONE: 2. Implement and test this function.
    #          Tests have been written for you (above).
    #
    # CONSIDER using the ACCUMULATOR IN GRAPHICS pattern,
    #             as in   draw_row_of_circles   in m1e,
    #             instead of directly using the loop variable.
    #
    ####################################################################
    # HINT: To figure out the code that computes the necessary
    #       endpoints for each line,
    #          ** FIRST DO A CONCRETE EXAMPLE BY HAND! **
    ####################################################################
    # ------------------------------------------------------------------

    x = point.x
    y = point.y

    for k in range(n):
        point = rg.Point(x, y)
        point2 = rg.Point((x + length), y)
        line = rg.Line(point, point2)

        line.attach_to(window)

        y = y + 30

    window.render()

def run_test_draw_lines():
    """ Tests the   draw_lines  function. """
    print()
    print('--------------------------------------------------')
    print('Testing the  draw_lines  function:')
    print('  See the graphics windows that pop up.')
    print('--------------------------------------------------')

    # TWO tests on ONE window.
    title = 'Tests 1 & 2 of DRAW_LINES:  4 lines, 12 lines!'
    window1 = rg.RoseWindow(350, 400, title)

    draw_lines(4, rg.Point(20, 120), window1)
    draw_lines(12, rg.Point(150, 230), window1)
    window1.close_on_mouse_click()

    # A third test on ANOTHER window.
    window2 = rg.RoseWindow(350, 300, 'Test 3 of DRAW_LINES:  7 lines!')
    draw_lines(7, rg.Point(50, 120), window2)
    window2.close_on_mouse_click()


def draw_lines(n, point, window):
    pX = point.x
    pY = point.y

    point = rg.Point(pX, pY)
    pY2 = -100

    for k in range(n):

        point2 = rg.Point((pX + 100), (pY2))
        line = rg.Line(point, point2)
        line.attach_to(window)
        pY2 = pY2 + (200 / n)

    window.render()

# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
