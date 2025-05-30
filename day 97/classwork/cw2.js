const body = document.getElementById("body")
const nav = document.getElementById("nav")
const container = document.getElementById("container")
const text = document.getElementById("text")
const text2 = document.getElementById("text2")
const text3 = document.getElementById("text3")
const button = document.getElementById("button")

let dark = false

function ლომი() {
    dark = !dark
    if (dark === true) {
        body.style.backgroundColor = "rgb(34, 34, 34)"
        nav.style.backgroundColor = "rgb(0, 0, 0)"
        container.style.backgroundColor = "rgb(0, 0, 0)"
        text.style.color = "rgb(255, 255, 255)"
        text2.style.color = "rgb(255, 255, 255)"
        text3.style.color = "rgb(255, 255, 255)"
        button.style.backgroundColor = "rgb(34, 34, 34)"
        button.style.color = "rgb(255, 255, 255)"
        button.style.borderBottom = "4px solid rgb(57, 57, 57)"
    }
    if (dark === false) {
        body.style.backgroundColor = "rgb(206, 206, 206)"
        nav.style.backgroundColor = "rgb(255, 255, 255)"
        container.style.backgroundColor = "rgb(255, 255, 255)"
        text.style.color = "rgb(0, 0, 0)"
        text2.style.color = "rgb(0, 0, 0)"
        text3.style.color = "rgb(0, 0, 0)"
        button.style.backgroundColor = "rgb(220, 220, 220)"
        button.style.color = "rgb(0, 0, 0)"
        button.style.borderBottom = "4px solid rgb(140, 140, 140)"
    }
}