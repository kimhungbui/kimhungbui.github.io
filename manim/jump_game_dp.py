from manim import *

class JumpGameDPApproach2(Scene):
    def construct(self):
        nums = [2, 3, 1, 1, 4]
        n = len(nums)

        # Visual groups
        boxes = VGroup()
        nums_text = VGroup()
        min_text = VGroup()
        min_steps = [float('inf')] * n  # Start with 'inf' as unvisited
        min_steps[0] = 0

        for i in range(n):
            # Box and number
            box = Square(side_length=1.2)
            box.set_fill(BLUE, opacity=0.3)
            box_text = Text(str(nums[i]), font_size=32).move_to(box.get_center())
            box_group = VGroup(box, box_text).shift(RIGHT * i * 1.5)
            boxes.add(box_group[0])
            nums_text.add(box_group[1])

            # min_step label
            step_str = "0" if i == 0 else "∞"
            step_color = YELLOW if i == 0 else GRAY
            step_text = Text(step_str, font_size=28, color=step_color)
            step_text.next_to(box_group, DOWN)
            min_text.add(step_text)

        full_array = VGroup(boxes, nums_text, min_text).move_to(ORIGIN)
        self.play(FadeIn(full_array))
        self.wait(1)

        # DP loop: Try to update every reachable index
        for i in range(n):
            # Highlight selected box
            highlight = boxes[i].copy().set_fill(GOLD, opacity=0.6)
            self.play(FadeIn(highlight), run_time=0.3)

            for step in range(1, nums[i] + 1):
                target = i + step
                if target < n:
                    proposed = min_steps[i] + 1
                    if proposed < min_steps[target]:
                        min_steps[target] = proposed

                        # Rounded arrow
                        start = boxes[i].get_top()
                        end = boxes[target].get_top()
                        arc = ArcBetweenPoints(start, end, angle=-PI / 4, color=WHITE)
                        self.play(Create(arc), run_time=0.3)

                        # Update min_text[target]
                        new_step_text = Text(str(proposed), font_size=28, color=YELLOW)
                        new_step_text.next_to(boxes[target], DOWN)
                        self.play(Transform(min_text[target], new_step_text), run_time=0.4)

            self.wait(0.3)
            self.play(FadeOut(highlight), run_time=0.2)

        self.wait(2)
