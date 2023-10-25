import matplotlib.pyplot as plt

def parse_data(file_name, tag):
    with open(file_name, 'r') as f:
        lines = f.readlines()

    if tag not in " ".join(lines):
        return []

    data = []
    start_parsing = False
    skip_lines = 2

    for line in lines:
        stripped_line = line.strip()
        if stripped_line == tag:
            start_parsing = True
            continue
        if start_parsing and skip_lines > 0:
            skip_lines -= 1
            continue
        if start_parsing:
            if not line.split()[0].isdigit():
                break
            data.append(list(map(float, line.split()[1:])))

    return data

def plot_data(file_name, tags, col_y, xlim=None, ylim=None, linewidth=None):
    for tag in tags:
        data = parse_data(file_name, tag.strip())
        if not data:
            print(f"No data found for tag '{tag}'")
            continue
        x = [d[0] for d in data]
        y = [d[col_y-1] for d in data]

        # Print x and y values
        print(f"\nData for tag '{tag}':")
        #print("x values:", x)
        #print("y values:", y)

        plt.plot(x, y, label=tag, linewidth=linewidth if linewidth else 1)
    plt.xlabel("r")
    plt.ylabel("Energy, "r"$\phi$")
    plt.title("Data plots for provided tags")
    plt.legend()
    plt.grid(True)
    
    if xlim:
        plt.xlim(xlim)
    if ylim:
        plt.ylim(ylim)
    
    plt.show()

file_name = input("Enter the filename (default 'table.txt' if left empty): ") or 'table.txt'
tags_input = input("Enter the tags (space-separated for multiple): ")
tags = tags_input.split()
col_y = int(input("Enter the column number for y-axis (2 for energy, 3 for force): "))

# Optional plotting parameters
xlim_input = input("Enter x-axis limits (format: min max) or leave empty: ")
ylim_input = input("Enter y-axis limits (format: min max) or leave empty: ")
linewidth_input = input("Enter line width or leave empty: ")

xlim = tuple(map(float, xlim_input.split())) if xlim_input else None
ylim = tuple(map(float, ylim_input.split())) if ylim_input else None
linewidth = float(linewidth_input) if linewidth_input else 3

plot_data(file_name, tags, col_y, xlim, ylim, linewidth)

