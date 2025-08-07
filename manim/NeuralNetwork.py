from manim import *
import random
import json
import os
import numpy as np  

class NeuralNetwork(Scene):
    def construct(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(script_dir, "..", "static", "manim", "config.json")

        with open(config_path) as f:
            config = json.load(f)

        self.labels = ['Input Layer', "Hidden 1", "Hidden 2", "Hidden 3", "Hidden 4", "Output Layer"]
        neuron_list = config['neurons']
        layers = min(config.get('layers', len(neuron_list)), 6)

        visuals = self.create_neural(neuron_list[:layers])

        animations = [Create(v) for v in visuals]
        self.play(*animations, run_time=5)
        self.wait(5)

    def create_nodes(self, x_pos, num_nodes):
        nodes = []
        node_group = VGroup()

        if num_nodes <= 10:
            for i in range(num_nodes):
                opacity = random.uniform(0.3, 1)
                circle = Circle(radius=0.23,
                                stroke_color=WHITE,
                                stroke_width=1,
                                fill_color=GRAY,
                                fill_opacity=opacity)
                label = Text("1", font_size=14)
                label.move_to(circle)
                group = VGroup(circle, label)
                nodes.append(circle)
                node_group.add(group)
        else:
            number_nodes_list = []
            for i in range(10):
                number_nodes_list.append(int(num_nodes / 10))
            index = 0
            for i in range(num_nodes % 10):
                number_nodes_list[index] += 1
                index += 1
            for i in range(10):
                opacity = random.uniform(0, 1)
                text = str(number_nodes_list[i])

                node = Circle(radius=0.23,
                              stroke_color=WHITE,
                              stroke_width=0.7,
                              fill_color=GRAY,
                              fill_opacity=opacity
                              )

                nodes.append(node)
                fill_text = Text(text, font_size=12)
                fill_text.move_to(node)

                group = VGroup(node, fill_text)
                node_group.add(group)
        node_group.arrange(DOWN, buff=0.3)

        # Center vertically
        node_group.move_to(np.array([x_pos, 0, 0]))
        return nodes, node_group

    def create_connections(self, left_nodes, right_nodes):
        lines = VGroup()
        for left in left_nodes:
            for right in right_nodes:
                color = GREEN if random.random() > 0.5 else RED
                line = Line(
                    start=left.get_right(),
                    end=right.get_left(),
                    color=color,
                    stroke_opacity=random.uniform(0.4, 1),
                    stroke_width=1.5
                )
                lines.add(line)
        return lines

    def create_neural(self, neuron_config):
        node_groups = []
        node_visuals = []
        text_render = []
        x_spacing = 2.5

        for i, num_neurons in enumerate(neuron_config):
            x_pos = -((len(neuron_config) - 1) / 2) * x_spacing + i * x_spacing
            nodes, visuals = self.create_nodes(x_pos, num_neurons)

            layer_label = Text(self.labels[i], font_size=18)
            layer_label.next_to(visuals, UP, buff=0.3)
            node_groups.append(nodes)
            node_visuals.append(visuals)
            text_render.append(layer_label)

        connections = []
        for i in range(len(node_groups) - 1):
            conn = self.create_connections(node_groups[i], node_groups[i + 1])
            connections.append(conn)

        all_elements = VGroup(*node_visuals, *connections, *text_render)
        all_elements.shift(DOWN * 0.25)  # Adjust vertical position

        return [all_elements]
