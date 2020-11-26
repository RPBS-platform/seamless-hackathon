from seamless.highlevel import Context, Cell, Transformer

ctx = Context()

ctx.seq1 = Cell("text")
ctx.seq1.mount("seq1.txt")
ctx.seq1.share(readonly=False)

ctx.seq2 = Cell("text")
ctx.seq2.mount("seq2.txt")
ctx.seq2.share(readonly=False)

ctx.align = Transformer()
ctx.align.language = "docker"
ctx.align.docker_image = "pegi3s/emboss"
ctx.align.seq1 = ctx.seq1
ctx.align.seq2 = ctx.seq2
ctx.align.code.mount("align.bash")

ctx.alignment = ctx.align
ctx.alignment.celltype = "text"
ctx.alignment.mount("alignment.water", "w")

ctx.scramble_code = Cell("text")
ctx.scramble_code.mount("scramble.py")

ctx.scramble1 = Transformer()
ctx.scramble1.seq = ctx.seq1
ctx.scramble1.code = ctx.scramble_code
ctx.scrambled1 = ctx.scramble1
ctx.scrambled1.celltype = "text"
ctx.scrambled1.mount("scrambled1.txt","w")

ctx.scramble2 = Transformer()
ctx.scramble2.seq = ctx.seq2
ctx.scramble2.code = ctx.scramble_code
ctx.scrambled2 = ctx.scramble2
ctx.scrambled2.celltype = "text"
ctx.scrambled2.mount("scrambled2.txt","w")

ctx.align_scrambled = Transformer()
ctx.align_scrambled.language = "docker"
ctx.align_scrambled.docker_image = "pegi3s/emboss"
ctx.align_scrambled.scrambled1 = ctx.scrambled1
ctx.align_scrambled.scrambled2 = ctx.scrambled2
ctx.align_scrambled.code.mount("align_scrambled.bash")

ctx.scrambled_scores = ctx.align_scrambled
ctx.scrambled_scores.celltype = "text"
ctx.scrambled_scores.mount("scrambled_scores.txt", "w")

ctx.analyze_alignment_scores = Transformer()
ctx.analyze_alignment_scores.alignment = ctx.alignment
ctx.analyze_alignment_scores.scrambled_scores = ctx.scrambled_scores
ctx.analyze_alignment_scores.code.mount("analyze_alignment_scores.py")

ctx.significance = ctx.analyze_alignment_scores
ctx.significance.celltype = "plain"
ctx.significance.mount("significance.json", "w")

##########################################
# topology for web interface
##########################################

ctx.seq1.share(readonly=False)
ctx.seq2.share(readonly=False)
ctx.alignment.share()
ctx.significance.share()

ctx.html = Cell("text")
ctx.html.mount("index.html")
ctx.html.mimetype = "html"
ctx.html.share("index.html")

ctx.js = Cell("text")
ctx.js.mount("index.js")
ctx.js.mimetype = "js"
ctx.js.share("index.js")

ctx.client_js = Cell("text")
ctx.client_js.mount("seamless-client.js", mode="r")
ctx.client_js.mimetype = "js"
ctx.client_js.share("seamless-client.js")
