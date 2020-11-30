ctx.dock = Transformer()
ctx.dock.language = "docker"
ctx.dock.docker_image = "rpbs/autodock-vina"
await ctx.translation()
ctx.dock.code = "vina --receptor receptor --ligand ligand --center_x 41.03 --center_y 18.98 --center_z 14.03 --cpu 2 --exhaustiveness 8 --size_x 20 --size_y 20 --size_z 20"
ctx.dock.receptor = open("receptor_example.pdbqt").read()
ctx.dock.ligand = open("ligand_example.pdbqt").read()
await ctx.translation()