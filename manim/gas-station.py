from manim import *
import numpy as np

class GasStationGreedyScene(Scene):
    def construct(self):
        gas = [1, 2, 3, 4, 5]
        cost = [3, 4, 5, 1, 2]
        n = len(gas)

        circle_shift = LEFT * 2.5
        stations = []
        radius = 3

        for i in range(n):
            angle = 2 * PI * i / n
            pos = radius * np.array([np.cos(angle), np.sin(angle), 0]) + circle_shift
            station = Circle(radius=0.4, color=BLUE).move_to(pos)
            label = Text(f"{i}", font_size=24).move_to(pos)
            gas_cost_label = Text(f"G:{gas[i]}, C:{cost[i]}", font_size=18).next_to(pos, RIGHT)
            self.add(station, label, gas_cost_label)
            stations.append(pos)

        explanation = VGroup(
            Text("gain = gas[i] - cost[i]", font_size=24),
            Text("curr_tank += gain", font_size=24),
            Text("total_tank += gain", font_size=24),
        ).arrange(DOWN, aligned_edge=LEFT).scale(0.8).to_corner(UP + RIGHT)
        explanation_box = SurroundingRectangle(explanation, color=GRAY)
        self.play(FadeIn(explanation_box), Write(explanation))
        self.wait(1)

        var_table = VGroup(
            Text(f"Current Index: 0", font_size=24),
            Text(f"Gain: 0", font_size=24),
            Text(f"curr_tank: 0", font_size=24),
            Text(f"total_tank: 0", font_size=24),
            Text(f"start_index: 0", font_size=24),
        ).arrange(DOWN, aligned_edge=LEFT).scale(0.8).to_corner(DOWN + RIGHT).shift(LEFT * 0.5)
        for var in var_table:
            self.add(var)

        total_tank = 0
        curr_tank = 0
        start_index = 0
        pointer = Circle(radius=0.5, color=GOLD, stroke_width=4).move_to(stations[0])
        self.play(FadeIn(pointer))
        self.wait(1)

        # Step explanation (top center)
        step_text = Text("Step 1: Traverse all stations once", font_size=28).to_edge(UP)
        self.play(Write(step_text))

        for i in range(n):
            idx = i
            gain = gas[idx] - cost[idx]
            total_tank += gain
            curr_tank += gain

            self.play(
                var_table[0].animate.become(Text(f"Current Index: {idx}", font_size=24).move_to(var_table[0].get_center())),
                var_table[1].animate.become(Text(f"Gain: {gain}", font_size=24).move_to(var_table[1].get_center())),
                var_table[2].animate.become(Text(f"curr_tank: {curr_tank}", font_size=24).move_to(var_table[2].get_center())),
                var_table[3].animate.become(Text(f"total_tank: {total_tank}", font_size=24).move_to(var_table[3].get_center())),
                var_table[4].animate.become(Text(f"start_index: {start_index}", font_size=24).move_to(var_table[4].get_center())),
            )
            self.wait(0.5)

            next_idx = (i + 1) % n
            arrow = Arrow(stations[idx], stations[next_idx], buff=0.4, color=YELLOW)
            self.play(GrowArrow(arrow), pointer.animate.move_to(stations[next_idx]))
            self.wait(0.5)

            if curr_tank < 0:
                # Step 2: Reset start if tank drops
                self.play(step_text.animate.become(Text("Step 2: If curr_tank < 0 → reset", font_size=28).to_edge(UP)))
                curr_tank = 0
                start_index = i + 1

                self.play(
                    var_table[2].animate.become(Text(f"curr_tank: {curr_tank}", font_size=24).move_to(var_table[2].get_center())),
                    var_table[4].animate.become(Text(f"start_index: {start_index}", font_size=24).move_to(var_table[4].get_center())),
                )
                reset_text = Text("Reset Start", color=RED, font_size=32).to_edge(RIGHT)
                reason_text = Text("→ Can't reach next station.\n Discard all before.", font_size=24, color=RED).next_to(reset_text, DOWN)
                self.play(Write(reset_text), Write(reason_text))
                self.wait(1)
                self.play(FadeOut(reset_text), FadeOut(reason_text))

        # Final result
        self.play(step_text.animate.become(Text("Step 3: If total_tank ≥ 0 → solution exists", font_size=28).to_edge(UP)))
        result_text = Text(f"Start at station {start_index}", color=GREEN, font_size=32).next_to(step_text, DOWN)
        fuel_check = Text(f"total_tank = {total_tank} ≥ 0 → valid path", font_size=28, color=BLUE).next_to(result_text, DOWN)

        self.play(Write(result_text), Write(fuel_check))
        self.wait(2)

        # Final summary
        summary = VGroup(
            Text("Greedy Algorithm Summary", font_size=28, color=YELLOW),
            Text("- Traverse all stations once", font_size=24),
            Text("- Reset start if fuel drops below 0", font_size=24),
            Text("- Discard unreachable segments", font_size=24),
            Text("- If total fuel ≥ 0, a solution exists", font_size=24),
        ).arrange(DOWN).scale(0.7).to_corner(RIGHT)
        self.play(FadeIn(summary))
        self.wait(3)
