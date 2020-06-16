##
#  pizza.py
#  Python
#
#  Created by Thomas Johannesmeyer (thomas@geeky.gent) on 15.05.2020.
#  Copyright (c) 2020 www.geeky.gent. All rights reserved.
#

import sys
from rich.console import Console
from rich.table import Column, Table

def main(argv):
    try:
        pizza_count = 12

        # Grams: 250 small / 300 normal
        pizza_weight = 300

        # 57% is default. 50-70 works
        water_percentage = 57
        if (len(argv) > 1):
            water_percentage = int(argv[1])

        console = Console()

        console.print(":pizza: Large pizza size, {}% water content :pizza:".format(water_percentage))

        if (water_percentage < 50) or (water_percentage > 70):
            console.print("\n:warning: Water percentage should be between 50% and 70% :warning:\n")

        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Count", justify="right")
        table.add_column("Flour", justify="right")
        table.add_column("Water", justify="right")
        table.add_column("Salt", justify="right")
        table.add_column("Yeast (fresh)", justify="right")
        table.add_column("Yeast (dry)*", style="dim", justify="right")
        for idx in range(1, pizza_count+1):

            # Magic
            flour = round((idx * pizza_weight) / (1 + (water_percentage / 100) + 0.03 + 0.002), 1);
            water = round((flour * water_percentage) / 100, 1);
            salt = round(0.03 * flour, 1);
            yeast = round(0.002 * flour, 1);

            # Wanna feed your whole neighbourhood?
            if (yeast <= 12):
                dry_factor = 0.5
            else:
                dry_factor = 0.411764706 # 🤓

            yeast_dried = round(dry_factor * yeast, 1);

            table.add_row(
                "{}".format(idx), "{}g".format(flour), "{}ml".format(water), "{}g".format(salt), "{}g".format(yeast), "{}g".format(yeast_dried))

        console.print(table)
        console.print("* don't use dry yeast, please\n\n")
        console.print("1. Combine 250ml water with 100g flour and yeast first and stirr.\n2. Add the rest of the water, followed by salt and flour to protect the yeast from the salt.\n3. Stirr until combined.\n4. Cover and let sit for 24-48h.")

    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main(sys.argv)

