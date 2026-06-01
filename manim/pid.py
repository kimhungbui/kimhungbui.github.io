from manim import *
import numpy as np

class PIDVisualization(Scene):
    def construct(self):
        # 1. Display the Equation
        equation = MathTex(
            "u(t) = ", 
            "K_p e(t)", " + ", 
            "K_i \\int_{0}^{t} e(\\tau) d\\tau", " + ", 
            "K_d \\frac{de(t)}{dt}"
        )
        equation.set_color_by_tex("K_p", RED)
        equation.set_color_by_tex("K_i", GREEN)
        equation.set_color_by_tex("K_d", BLUE)
        
        self.play(Write(equation))
        self.wait(1)
        self.play(equation.animate.to_edge(UP))

        # 2. Create the "Stick" and "Hand" (The Robot Arm)
        target_line = Line(ORIGIN, 3*RIGHT, color=YELLOW, stroke_width=2).shift(DOWN*1)
        target_label = Text("Target Position", font_size=20).next_to(target_line, RIGHT)
        
        joint = Dot(LEFT*2 + DOWN*1)
        arm = Line(joint.get_center(), joint.get_center() + 3*UP, color=WHITE)
        hand = Dot(arm.get_end(), color=GOLD)
        
        arm_group = VGroup(arm, hand)
        
        self.add(target_line, target_label, joint, arm_group)

        # 3. Animate the PID Concepts
        # P: Move toward target
        p_text = Text("Proportional: Push toward target", color=RED, font_size=24).shift(DOWN*2.5)
        self.play(Write(p_text))
        self.play(Rotate(arm_group, angle=-PI/3, about_point=joint.get_center()), run_time=1)
        self.play(FadeOut(p_text))

        # I: Correcting the small gap (Steady-state error)
        i_text = Text("Integral: Fixing the stubborn gap", color=GREEN, font_size=24).shift(DOWN*2.5)
        self.play(Write(i_text))
        self.play(Rotate(arm_group, angle=-PI/7, about_point=joint.get_center()), run_time=1.5)
        self.play(FadeOut(i_text))

        # D: Smoothing the stop
        d_text = Text("Derivative: Dampening for a smooth stop", color=BLUE, font_size=24).shift(DOWN*2.5)
        self.play(Write(d_text))
        self.play(
            arm_group.animate.rotate(angle=-PI/15, about_point=joint.get_center()),
            rate_func=slow_into,
            run_time=2
        )
        self.wait(2)