from manim import *

class SignalAndOrbit(Scene):
    def construct(self):
        # Step 1: Introduce the orbit
        planet = Circle(radius=1, color=BLUE)
        station = Dot(color=YELLOW).move_to(planet.get_top())
        orbit = Circle(radius=2.5, color=BLUE_D).shift(DOWN*0.5)

        self.play(FadeIn(planet), FadeIn(orbit))
        self.wait(1)
        self.play(FadeIn(station))

        orbit_text = Text("Orbit of the Station", font_size=24, color=BLUE).next_to(orbit, UP)
        self.play(Write(orbit_text))
        self.wait(1)

        # Step 2: Introduce the signal
        signal_text = Text("Signal repeats every 13.2 s", font_size=24, color=YELLOW).to_edge(UP)
        self.play(Write(signal_text))
        self.wait(1)

        # Step 3: Animate the station moving along orbit
        self.play(MoveAlongPath(station, orbit), run_time=6, rate_func=linear)

        # Step 4: Visualize alignment
        gcd_text = Text("Every 0.3 s, the orbit & signal align!", font_size=28, color=RED).to_edge(DOWN)
        self.play(Write(gcd_text))

        # Step 5: Show two waves to illustrate alignment
        axes = Axes(
            x_range=[0, 14, 1],
            y_range=[-1.5, 1.5, 1],
            x_length=10,
            y_length=3,
            tips=False
        ).to_edge(DOWN)

        self.play(FadeIn(axes))
        
        # Define orbit and signal waves
        orbit_wave = lambda t: np.sin(2 * np.pi * t / 13.2)  # scaled for visualization
        signal_wave = lambda t: np.sin(2 * np.pi * t / 3.0)  # GCD alignment
        
        orbit_graph = axes.plot(orbit_wave, color=BLUE, stroke_width=3)
        signal_graph = axes.plot(signal_wave, color=YELLOW, stroke_width=3)
        self.play(Create(orbit_graph), Create(signal_graph))

        # Step 6: Add simple markers for alignment
        markers = VGroup()
        for x in np.arange(0, 14, 0.3):
            line = DashedLine(start=axes.c2p(x, -1.5), end=axes.c2p(x, 1.5), color=RED)
            markers.add(line)
        self.play(FadeIn(markers))

        # Step 7: Add narration-style text for kids
        explanation = Text(
            "See! Every 0.3 seconds, the yellow and blue waves touch.\n"
            "This is a hidden rhythm in the signal and orbit!", 
            font_size=24, color=WHITE
        ).next_to(axes, UP)
        self.play(Write(explanation))
        self.wait(4)