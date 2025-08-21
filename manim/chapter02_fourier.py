from manim import *

class FourierBasics(Scene):
    def construct(self):
        # Title
        title = Text("Fourier Analysis Made Simple", font_size=48)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))

        # Show the signal as a wavy line
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[-3, 3, 1],
            axis_config={"color": WHITE},
        ).scale(0.8)
        signal_text = Text("Mysterious Signal", font_size=24).next_to(axes, UP)
        self.play(Create(axes), Write(signal_text))

        # Draw multiple sine waves to represent components
        sine1 = axes.plot(lambda x: 0.5*np.sin(2*PI*0.3*x), color=BLUE)
        sine2 = axes.plot(lambda x: 0.3*np.sin(2*PI*0.9*x), color=GREEN)
        sine3 = axes.plot(lambda x: 0.2*np.sin(2*PI*1.5*x), color=YELLOW)

        # Animate the sine waves appearing one by one
        self.play(Create(sine1))
        label1 = Tex("0.3 Hz").next_to(sine1, UP)
        self.play(Write(label1))
        self.wait(1)

        self.play(Create(sine2))
        label2 = Tex("0.9 Hz").next_to(sine2, UP)
        self.play(Write(label2))
        self.wait(1)

        self.play(Create(sine3))
        label3 = Tex("1.5 Hz").next_to(sine3, UP)
        self.play(Write(label3))
        self.wait(1)

        # Combine waves to show the signal is made of multiple frequencies
        combined = axes.plot(lambda x: 0.5*np.sin(2*PI*0.3*x)+0.3*np.sin(2*PI*0.9*x)+0.2*np.sin(2*PI*1.5*x), color=RED)
        combined_text = Text("Combined Signal", font_size=24).next_to(axes, DOWN)
        self.play(Create(combined), Write(combined_text))
        self.wait(1.5)

        # Explain GCD / Fundamental frequency
        explanation = Text(
            "The smallest repeating frequency is 0.3 Hz\nThis is the fundamental frequency!", 
            font_size=28
        ).to_edge(DOWN)
        self.play(Write(explanation))
        self.wait(3)