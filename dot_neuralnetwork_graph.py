# -*- coding: utf-8 -*-
import sys
import subprocess
import ast

def parse_layers(layers_str):
    try:
        return ast.literal_eval(layers_str)
    except:
        print(f"Error: Invalid layer format. will use default layers.")
        return [3, 5, 4, 2]

def generate_network_dot(layers, output_file='network.dot', image_file='network.png'):
    layers_str = ["Input"] + ["Hidden"] * (len(layers) - 2) + ["Output"]
    layers_col = ["none"] + ["none"] * (len(layers) - 2) + ["none"]
    layers_fill = ["black"] + ["gray"] * (len(layers) - 2) + ["black"]

    penwidth = 15
    # font and font size
    font = "Comic Sans MS 10"

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("digraph G {\n")
        f.write(f"\tfontname = \"{font}\"\n")
        f.write("\trankdir=LR\n")
        f.write("\tsplines=line\n")
        f.write("\tnodesep=.08;\n")
        f.write("\tranksep=1;\n")
        f.write("\tedge [color=black, arrowsize=.5];\n")
        f.write("\tnode [fixedsize=true,label=\"\",style=filled," + 
                "color=none,fillcolor=gray,shape=circle]\n\n")

        # Clusters
        for i in range(0, len(layers)):
            f.write(f"\tsubgraph cluster_{i} {{\n")
            f.write(f"\t\tcolor={layers_col[i]};\n")
            f.write(f"\t\tnode [style=filled, color=white, penwidth={penwidth}," +
                    f"fillcolor={layers_fill[i]} shape=circle];\n")

            f.write("\t\t")
            for a in range(layers[i]):
                f.write(f"l{i+1}{a} ")
            f.write(";\n")

            f.write(f"\t\tlabel = {layers_str[i]};\n")
            f.write("\t}\n\n")

        # Nodes
        for i in range(1, len(layers)):
            for a in range(layers[i - 1]):
                for b in range(layers[i]):
                    f.write(f"\tl{i}{a} -> l{i+1}{b}\n")

        f.write("}")
        
    print(f"DOT file has been generated: {output_file}")
    # use the dot to generate the png
    try:
        subprocess.run(['dot', '-Tpng', output_file, '-o', image_file], check=True)
        print(f"Image file has been generated: {image_file}")
    except subprocess.CalledProcessError:
        print("Error: Failed to generate image. Make sure Graphviz is installed and 'dot' is in your PATH.")
    except FileNotFoundError:
        print("Error: 'dot' command not found. Make sure Graphviz is installed and 'dot' is in your PATH.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        layers = parse_layers(sys.argv[1])
    else:
        layers = [3, 5, 4, 2]  # default
    generate_network_dot(layers)
