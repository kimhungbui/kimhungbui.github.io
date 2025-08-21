from manim import *

class SignalSplit(Scene):
    def construct(self):
        # Title
        title = Text("Original Signal and Components", font_size=40)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))

        # Axes for the signal
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[-3, 3, 1],
            axis_config={"color": WHITE},
        ).scale(0.8)
        signal_label = Text("Original Signal", font_size=24).next_to(axes, UP)
        self.play(Create(axes), Write(signal_label))

        # Original combined signal
        original_signal = axes.plot(
            lambda x: 0.5*np.sin(2*PI*0.3*x) + 0.3*np.sin(2*PI*0.9*x) + 0.2*np.sin(2*PI*1.5*x),
            color=RED
        )
        self.play(Create(original_signal))
        self.wait(2)

        # Explain splitting
        explain = Text("Splitting the signal into components...", font_size=28).next_to(axes, DOWN)
        self.play(Write(explain))
        self.wait(1)

        # Component waves
        comp1 = axes.plot(lambda x: 0.5*np.sin(2*PI*0.3*x), color=BLUE)
        comp2 = axes.plot(lambda x: 0.3*np.sin(2*PI*0.9*x), color=GREEN)
        comp3 = axes.plot(lambda x: 0.2*np.sin(2*PI*1.5*x), color=YELLOW)

        # Animate components appearing one by one
        self.play(Create(comp1), run_time=2)
        self.play(Write(Tex("0.3 Hz").next_to(comp1, UP)))
        self.wait(1)

        self.play(Create(comp2), run_time=2)
        self.play(Write(Tex("0.9 Hz").next_to(comp2, UP)))
        self.wait(1)

        self.play(Create(comp3), run_time=2)
        self.play(Write(Tex("1.5 Hz").next_to(comp3, UP)))
        self.wait(1)

        # Show how combined again
        combined_text = Text("Reconstructed Signal", font_size=24).next_to(axes, DOWN)
        self.play(Write(combined_text))
        self.play(Transform(VGroup(comp1, comp2, comp3), original_signal), run_time=2)
        self.wait(2)

        # Highlight fundamental frequency
        fundamental_text = Text(
            "Fundamental Frequency = 0.3 Hz\n(Repeating pattern!)",
            font_size=28,
        ).to_edge(DOWN)
        self.play(Write(fundamental_text))
        self.wait(3)