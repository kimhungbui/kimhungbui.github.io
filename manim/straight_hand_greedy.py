from manim import *
from collections import Counter
import heapq

class IsNStraightHandTrueLogic(Scene):
    def construct(self):
        # Input setup
        hand = [1,2,3,6,2,3,4,7,8]
        groupSize = 3

        title = Text("isNStraightHand – True Step-by-Step Logic", font_size=36)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))

        input_text = Text(f"hand = {hand}, groupSize = {groupSize}", font_size=28).next_to(title, DOWN)
        self.play(Write(input_text))
        self.wait(1)

        # Step 1: Initial state
        count = Counter(hand)
        min_heap = list(count.keys())
        heapq.heapify(min_heap)

        # Show counter and heap as text
        heap_label = Text("Heap:", font_size=24).to_edge(LEFT).shift(DOWN * 1.5)
        heap_val = Text(str(min_heap), font_size=24).next_to(heap_label, RIGHT)
        counter_label = Text("Counter:", font_size=24).next_to(heap_val, RIGHT, buff=1.5)
        counter_val = Text(str(dict(count)), font_size=24).next_to(counter_label, RIGHT)
        self.play(Write(heap_label), Write(heap_val), Write(counter_label), Write(counter_val))
        self.wait(1)

        step = 0
        while min_heap:
            step += 1
            first = min_heap[0]

            step_label = Text(f"Step {step}: Start from {first}", font_size=26).to_edge(DOWN)
            self.play(Write(step_label))
            self.wait(0.5)

            for i in range(groupSize):
                current = first + i
                process_label = Text(f"current = {current}", font_size=24, color=YELLOW).next_to(step_label, UP)
                self.play(Write(process_label))

                if count[current] == 0:
                    error = Text(f"{current} not available → return False", color=RED, font_size=26).next_to(process_label, DOWN)
                    self.play(Write(error))
                    self.wait(2)
                    return

                count[current] -= 1

                if count[current] == 0:
                    if current != min_heap[0]:
                        error = Text(f"{current} ≠ min_heap[0] ({min_heap[0]}) → return False", font_size=26, color=RED).next_to(process_label, DOWN)
                        self.play(Write(error))
                        self.wait(2)
                        return
                    heapq.heappop(min_heap)

                # Update heap and counter
                new_heap = Text(str(min_heap), font_size=24).move_to(heap_val)
                new_counter = Text(str(dict(count)), font_size=24).move_to(counter_val)
                self.play(Transform(heap_val, new_heap), Transform(counter_val, new_counter))
                self.wait(0.5)

                self.play(FadeOut(process_label))

            self.play(FadeOut(step_label))

        # Success
        success = Text("All groups formed → return True", font_size=28, color=GREEN).next_to(counter_val, DOWN * 2)
        self.play(Write(success))
        self.wait(2)
