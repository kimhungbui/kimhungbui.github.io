from manim import *

class JumpGameGreedy(Scene):
    def construct(self):
        nums = [2, 3, 1, 1, 4]
        n = len(nums)

        # Visual elements
        boxes = VGroup()
        nums_text = VGroup()
        labels = VGroup()
        for i in range(n):
            box = Square(side_length=1.2)
            box.set_fill(BLUE, opacity=0.3)
            box_text = Text(str(nums[i]), font_size=32).move_to(box.get_center())
            box_group = VGroup(box, box_text).shift(RIGHT * i * 1.5)
            boxes.add(box_group[0])
            nums_text.add(box_group[1])

            index_label = Text(str(i), font_size=24, color=GRAY)
            index_label.next_to(box_group, DOWN)
            labels.add(index_label)

        array_group = VGroup(boxes, nums_text, labels).move_to(ORIGIN)
        self.play(FadeIn(array_group))
        self.wait(1)

        # Track variables
        jumps = 0
        farthest = 0
        current_end = 0
        jump_text = Text("Jumps: 0", font_size=36).to_edge(UP)
        explain_text = Text("", font_size=28).to_edge(DOWN)

        self.play(Write(jump_text))
        self.play(FadeIn(explain_text))
        self.wait(0.5)

        # Start loop
        for i in range(n - 1):
            # Highlight current position
            highlight = boxes[i].copy().set_fill(GOLD, opacity=0.6)
            self.play(FadeIn(highlight), run_time=0.5)

            # Update explanation text
            self.play(Transform(
                explain_text,
                Text(f"Index {i}: max reach = max({farthest}, {i}+{nums[i]})", font_size=28).to_edge(DOWN)
            ))
            self.wait(1.0)

            # Update farthest
            old_farthest = farthest
            farthest = max(farthest, i + nums[i])

            if farthest != old_farthest:
                start = boxes[i].get_top()
                end = boxes[farthest].get_top()
                arc = ArcBetweenPoints(start, end, angle=-PI / 4, color=WHITE)
                self.play(Create(arc), run_time=0.8)

                self.play(Transform(
                    explain_text,
                    Text(f"New farthest updated to {farthest}", font_size=28).to_edge(DOWN)
                ))
                self.wait(1)

            # Jump trigger
            if i == current_end:
                jumps += 1
                current_end = farthest

                boundary = SurroundingRectangle(boxes[current_end], color=YELLOW)
                self.play(Create(boundary), run_time=0.6)

                new_jump_text = Text(f"Jumps: {jumps}", font_size=36).to_edge(UP)
                self.play(Transform(jump_text, new_jump_text), run_time=0.5)

                self.play(Transform(
                    explain_text,
                    Text(f"Reached boundary. Jump to index {current_end}", font_size=28).to_edge(DOWN)
                ))
                self.wait(1.2)

            self.play(FadeOut(highlight), run_time=0.4)
            self.wait(0.5)

        self.play(Transform(
            explain_text,
            Text(f"Reached the end in {jumps} jumps.", font_size=32, color=GREEN).to_edge(DOWN)
        ))
        self.wait(3)
