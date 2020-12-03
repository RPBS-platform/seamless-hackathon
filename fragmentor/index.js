
ctx = connect_seamless()
ctx.self.onsharelist = function(sharelist) {
    sharelist.forEach(element => {



        if (element.indexOf(".") != -1) {
            return
        }
        var inputElement = document.getElementById(element)
        if (inputElement === null) {
           inputElement = document.getElementsByName(element)
           inputElement = inputElement[0]
           if (inputElement === null) return
        }

        else if (['l', 't', 'u'].indexOf(element) >= 0) {
            ctx[element].onchange = function() {
                //const v = JSON.parse(this.value)
                const v = this.value
                console.log(element, v)
                inputElement.value = v
                const inputElement2 = document.getElementById(element+"2")
                console.log(element, inputElement2, v)
                if (inputElement2 === null) return
                inputElement2.value = "ok"
            }
            inputElement.onchange = function() {
                v = this.value
                ctx[element].set(v)
                const inputElement2 = document.getElementById(element+"2")
                if (inputElement2 === null) return
                inputElement2.value = v
            }
        }
    })
}
