from manim import *
from sympy import isprime

class PrimeFamily2Digit(Scene):
    def construct(self):
        # Display header
        header = Text("2-digit numbers of form *3", font_size=44).to_edge(UP)
        self.play(Write(header))

        # List of all *3 numbers
        base_digit = "3"
        primes = []
        labels = VGroup()
        for i, d in enumerate("123456789"):
            num = int(d + base_digit)
            prime = isprime(num)
            color = GREEN if prime else RED
            label = Text(str(num), font_size=40, color=color).move_to(LEFT * 4 + DOWN * (i - 4) * 0.8)
            labels.add(label)
            if prime:
                primes.append(num)

        self.play(LaggedStart(*[FadeIn(lbl) for lbl in labels], lag_ratio=0.1))
        self.wait(1)

        # Show only primes
        primes_text = Text(f"Primes: {', '.join(map(str, primes))}", font_size=28).next_to(labels, RIGHT, buff=1.5)
        self.play(Write(primes_text))
        self.wait(2)


class PrimeFamily56003(Scene):
    def construct(self):
        base_number = "56003"
        replace_indices = [2, 3]  # Replace 3rd and 4th digit

        # Title
        title = Text("Prime Family from 56003", font_size=40).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Base number digits
        digits = VGroup(*[Text(ch, font_size=60) for ch in base_number])
        for i, d in enumerate(digits):
            d.move_to(RIGHT * (i - 2) * 1.2)
            if i in replace_indices:
                d.set_color(YELLOW)
        self.play(FadeIn(digits))
        self.wait(1)

        # Generate all replacements
        prime_family = []
        for i in range(10):
            new_digits = list(base_number)
            for idx in replace_indices:
                new_digits[idx] = str(i)
            new_num = int("".join(new_digits))
            if isprime(new_num):
                prime_family.append(new_num)

        # Convert list of primes to multiline string (max 4 per line)
        prime_strs = list(map(str, prime_family))
        grouped_lines = [", ".join(prime_strs[i:i+4]) for i in range(0, len(prime_strs), 4)]
        multiline_text = "\n".join(grouped_lines)

        # Display multiline prime family text below base number
        family_text = Text("Prime family:", font_size=32).next_to(digits, DOWN * 2)
        prime_list_text = Text(multiline_text, font_size=28).next_to(family_text, DOWN)

        self.play(Write(family_text))
        self.wait(0.5)
        self.play(Write(prime_list_text))
        self.wait(2)

        # Count
        count_text = Text(f"Total primes: {len(prime_family)}", font_size=32).next_to(prime_list_text, DOWN)
        self.play(Write(count_text))
        self.wait(2)
        
        

class ExplainPrimeFamilyQuestion(Scene):
    def construct(self):
        title = Text("Understanding the 8-Prime Family Problem", font_size=44)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))

        # Step-by-step explanation
        step1 = Text("1. Take a prime number like 56003", font_size=32)
        step2 = Text("2. Replace some digits (e.g., 3rd and 4th) with *", font_size=32)
        step3 = Text("    → 56**3", font_size=32, color=YELLOW)
        step4 = Text("3. Replace * with digits 0–9 to get 10 new numbers", font_size=32)
        step5 = Text("4. Count how many of them are prime numbers", font_size=32)
        step6 = Text("5. We want a case where 8 of those 10 numbers are prime", font_size=32, color=GREEN)

        steps = VGroup(step1, step2, step3, step4, step5, step6).arrange(DOWN, aligned_edge=LEFT).next_to(title, DOWN, buff=0.7)
        self.play(LaggedStart(*[Write(step) for step in steps], lag_ratio=0.2))
        self.wait(2)

        # Clarify what "8-prime family" means
        clarif = Text("Note: It does NOT mean 8-digit primes!", font_size=30, color=RED)
        clarif.next_to(steps, DOWN, buff=0.6)
        self.play(Write(clarif))
        self.wait(2)

        # Show an example
        example_title = Text("Example: 56**3", font_size=36, color=YELLOW).next_to(clarif, DOWN, buff=0.8)
        self.play(Write(example_title))
        self.wait(0.5)

        primes = [56003, 56113, 56333, 56443, 56663, 56773, 56993]  # 7 primes
        prime_texts = VGroup()
        for i, p in enumerate(primes):
            p_text = Text(str(p), font_size=30, color=GREEN)
            p_text.next_to(example_title, DOWN, buff=0.4 + i * 0.5, aligned_edge=LEFT)
            prime_texts.add(p_text)
        self.play(LaggedStart(*[FadeIn(p) for p in prime_texts], lag_ratio=0.1))

        conclusion = Text("We are looking for the SMALLEST such prime with 8 valid results", font_size=32, color=BLUE).next_to(prime_texts, DOWN, buff=0.8)
        self.play(Write(conclusion))
        self.wait(3)



class PrimeFamilySolverExplanation(Scene):
    def construct(self):
        title = Text("How to Solve the 8-Prime Family Problem", font_size=44)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))

        steps = [
            "1. Loop through prime numbers.",
            "2. For each prime, find digits that repeat (e.g., '1', '3').",
            "3. Try all combinations of positions of the repeated digit.",
            "4. Replace those positions with digits 0–9 (same digit each time).",
            "5. Skip numbers with leading zeros.",
            "6. Count how many replacements result in primes.",
            "7. If you find 8 primes, store the smallest one.",
            "8. Return the first such prime you discover."
        ]

        step_texts = VGroup(*[Text(s, font_size=30) for s in steps])
        step_texts.arrange(DOWN, aligned_edge=LEFT).scale(0.95)
        step_texts.next_to(title, DOWN, buff=0.8)

        self.play(LaggedStart(*[Write(t) for t in step_texts], lag_ratio=0.2))
        self.wait(2)

        highlight = SurroundingRectangle(step_texts[6], color=YELLOW)
        self.play(Create(highlight))
        self.wait(2)

        conclusion = Text("The smallest prime in such a family is: 121313", font_size=36, color=BLUE)
        conclusion.next_to(step_texts, DOWN, buff=1)
        self.play(Write(conclusion))
        self.wait(3)


class SymbolicAbstraction(Scene):
    def construct(self):
        title = Text("Symbolic Abstraction of Prime Digit Replacement", font_size=38)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))

        # Step 1: Prime Example
        prime_text = Text("Example Prime: 56003", font_size=32)
        self.play(Write(prime_text))
        self.wait(1)

        # Step 2: Replace 3rd and 4th digit (index 2 and 3)
        pattern_text = Text("Pattern: 56**3", font_size=32, color=YELLOW)
        pattern_text.next_to(prime_text, DOWN, buff=0.6)
        self.play(Write(pattern_text))
        self.wait(1)

        # Step 3: Define symbolic pattern function
        func_def = Tex(r"F(t) = \{ \text{fill } * \text{ with digits 0--9} \}", font_size=36)
        func_def.next_to(pattern_text, DOWN, buff=0.8)
        self.play(Write(func_def))
        self.wait(1.5)

        # Step 4: Generate replacement examples
        example_group = VGroup(
            Text("56003", font_size=30, color=GREEN),
            Text("56113", font_size=30, color=GREEN),
            Text("56333", font_size=30, color=GREEN),
            Text("56443", font_size=30, color=GREEN),
            Text("56663", font_size=30, color=GREEN),
            Text("56773", font_size=30, color=GREEN),
            Text("56993", font_size=30, color=GREEN),
        ).arrange(RIGHT, buff=0.4).next_to(func_def, DOWN, buff=0.8)
        self.play(LaggedStart(*[FadeIn(p) for p in example_group], lag_ratio=0.15))
        self.wait(1.5)

        # Step 5: Show abstraction mask
        mask_def = Tex(r"m = [0, 0, 1, 1, 0]", font_size=36, color=BLUE)
        mask_def.next_to(example_group, DOWN, buff=0.8)
        self.play(Write(mask_def))
        self.wait(1.5)

        constraint = Text("Constraint: positions with 1 must hold the same digit", font_size=28, color=GRAY)
        constraint.next_to(mask_def, DOWN, buff=0.6)
        self.play(FadeIn(constraint))
        self.wait(2)

        # Final Note
        conclusion = Text("Find the smallest p such that |F(p, m) ∩ PRIMES| ≥ 8", font_size=30, color=PURPLE)
        conclusion.next_to(constraint, DOWN, buff=1)
        self.play(Write(conclusion))
        self.wait(3)
