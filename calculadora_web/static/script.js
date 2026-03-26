function add(valor){

    let display = document.getElementById("display")

    display.focus()

    let inicio = display.selectionStart
    let fim = display.selectionEnd

    let texto = display.value

    display.value = texto.substring(0, inicio) + valor + texto.substring(fim)

    display.selectionStart = display.selectionEnd = inicio + 1
}



function clearDisplay(){
    document.getElementById("display").value = ""
}

function backspace(){
    let display = document.getElementById("display")
    display.value = display.value.slice(0, -1)
}

function calcular(){

    let display = document.getElementById("display")

    try{

        let resultado = eval(display.value)

        if(!isFinite(resultado)){
            display.value = "Erro"
        }
        else{
            display.value = resultado
        }

    }
    catch{
        display.value = "Erro"
    }
}


document.addEventListener("keydown", function(event){

    let tecla = event.key

    if(!isNaN(tecla)){
        event.preventDefault()
        add(tecla)
    }

    else if(tecla === "+" || tecla === "-" || tecla === "*" || tecla === "/"){
        event.preventDefault()
        add(tecla)
    }

    else if(tecla === "Enter"){
        event.preventDefault()
        calcular()
    }

    else if(tecla === "Backspace"){
        event.preventDefault()
        backspace()
    }

})


function backspace(){

    let display = document.getElementById("display")

    let pos = display.selectionStart

    if(pos > 0){

        display.value =
        display.value.substring(0, pos - 1) +
        display.value.substring(pos)

        display.selectionStart = display.selectionEnd = pos - 1
    }
}

window.onload = function(){
    document.getElementById("display").focus()
}
