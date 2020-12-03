ctx = connect_seamless()

ctx.self.onsharelist = function (sharelist) {

    var inputElement = document.getElementById("seq1");
    inputElement.addEventListener("change", change_a, false);
    function change_a() {
        ctx["seq1"].set(this.value)
    }
    ctx["seq1"].onchange = function () {
        value = this.value
        document.getElementById("seq1").value = value
    }

    var inputElement = document.getElementById("seq2");
    inputElement.addEventListener("change", change_b, false);
    function change_b() {
        ctx["seq2"].set(this.value)
    }
    ctx["seq2"].onchange = function () {
        value = this.value
        document.getElementById("seq2").value = value
    }

    ctx["alignment"].onchange = function () {
        value = this.value
        document.getElementById("alignment").value = value
    }

    ctx["significance"].onchange = function () {
        value = this.value
        const json = value;
        const obj = JSON.parse(json);

        //document.getElementById("significance").value = value
        document.getElementById("zscore").value = obj.z
        document.getElementById("pvalue").value = obj.p

    }

}
