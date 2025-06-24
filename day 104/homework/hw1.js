// HTML ელემენტების გადმოტანა
const form = document.getElementById('todo-form')
const input = document.getElementById('todo-input')
const list = document.getElementById('todo-list')
const addBTN = document.querySelector('button')

let itemIndex = 0 // იწყება მენულე li-დან

addBTN.addEventListener('click', function(e) {
    e.preventDefault() // აჩერებს browser-ს გადატვირთვისგან
    itemIndex += 1 // ემატება 1
    const li = document.querySelector('ul li:nth-child(' + itemIndex + ')') // იღებს ახალ li ელემენტს და itemIndex-ის მიხედვით ხვდება რომელი li ელემენტი მიიღოს
    li.style.display = "block" // აღებულ li ელემენტს აჩვენებს
    const text = document.querySelector('ul li:nth-child(' + itemIndex + ') p') // იღებს li-ში არსებულ p ელემენტს
    text.textContent = input.value // p ელემენტი იღებს ტექსტს რას input-ში წერია
    input.value = "" // ასუფთავებს input-ის ტექსტს
})

// შლის მეიმდენე li ელემენტს მერამდენეს x-საც დავაწვებით
document.querySelector('ul li:nth-child(1) .close').addEventListener('click', function() {document.querySelector('ul li:nth-child(1)').style.display = "none"})
document.querySelector('ul li:nth-child(2) .close').addEventListener('click', function() {document.querySelector('ul li:nth-child(2)').style.display = "none"})
document.querySelector('ul li:nth-child(3) .close').addEventListener('click', function() {document.querySelector('ul li:nth-child(3)').style.display = "none"})
document.querySelector('ul li:nth-child(4) .close').addEventListener('click', function() {document.querySelector('ul li:nth-child(4)').style.display = "none"})
document.querySelector('ul li:nth-child(5) .close').addEventListener('click', function() {document.querySelector('ul li:nth-child(5)').style.display = "none"})
document.querySelector('ul li:nth-child(6) .close').addEventListener('click', function() {document.querySelector('ul li:nth-child(6)').style.display = "none"})
document.querySelector('ul li:nth-child(7) .close').addEventListener('click', function() {document.querySelector('ul li:nth-child(7)').style.display = "none"})
document.querySelector('ul li:nth-child(8) .close').addEventListener('click', function() {document.querySelector('ul li:nth-child(8)').style.display = "none"})
document.querySelector('ul li:nth-child(9) .close').addEventListener('click', function() {document.querySelector('ul li:nth-child(9)').style.display = "none"})
document.querySelector('ul li:nth-child(10) .close').addEventListener('click', function() {document.querySelector('ul li:nth-child(10)').style.display = "none"})
document.querySelector('ul li:nth-child(11) .close').addEventListener('click', function() {document.querySelector('ul li:nth-child(11)').style.display = "none"})
document.querySelector('ul li:nth-child(12) .close').addEventListener('click', function() {document.querySelector('ul li:nth-child(12)').style.display = "none"})
document.querySelector('ul li:nth-child(13) .close').addEventListener('click', function() {document.querySelector('ul li:nth-child(13)').style.display = "none"})
document.querySelector('ul li:nth-child(14) .close').addEventListener('click', function() {document.querySelector('ul li:nth-child(14)').style.display = "none"})
document.querySelector('ul li:nth-child(15) .close').addEventListener('click', function() {document.querySelector('ul li:nth-child(15)').style.display = "none"})
document.querySelector('ul li:nth-child(16) .close').addEventListener('click', function() {document.querySelector('ul li:nth-child(16)').style.display = "none"})
document.querySelector('ul li:nth-child(17) .close').addEventListener('click', function() {document.querySelector('ul li:nth-child(17)').style.display = "none"})
document.querySelector('ul li:nth-child(18) .close').addEventListener('click', function() {document.querySelector('ul li:nth-child(18)').style.display = "none"})
document.querySelector('ul li:nth-child(19) .close').addEventListener('click', function() {document.querySelector('ul li:nth-child(19)').style.display = "none"})
document.querySelector('ul li:nth-child(20) .close').addEventListener('click', function() {document.querySelector('ul li:nth-child(20)').style.display = "none"})
