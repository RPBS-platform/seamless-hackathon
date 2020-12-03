ctx.frag = Transformer()
ctx.frag.language = "docker"
ctx.frag.docker_image = "ubuntu_fragmentor2019"
await ctx.translation()
ctx.frag.t = 4
ctx.frag.code = "/home/opt/Fragmentor2019/lnx64/Fragmentor_lnx64 -i /home/opt/Fragmentor2019/data/BCF_std_train.sdf -t 4 -l 2 -u6"
#ctx.frag.receptor = open("receptor_example.pdbqt").read()
#ctx.frag.ligand = open("ligand_example.pdbqt").read()
await ctx.translation()