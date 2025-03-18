// ドラッグ&ドロップによる回答システム

function allowDrop(event) {
    event.preventDefault()
}

function drag(event) {
    event.dataTransfer.setData('text', event.target.dataset.value)
}

function drop(event) {
    event.preventDefault()
    var data = event.dataTransfer.getData('text')
    console.log(data)
    var answerBox = document.getElementById('answer-box')
    var inputField = document.getElementById('answer-input')

    var placeholder = answerBox.querySelector('.placeholder')
    if (placeholder) placeholder.remove()

    var span = document.createElement('span')
    span.textContent = data
    span.classList.add('dropped-number')
    answerBox.appendChild(span)

    inputField.value += data
}

// スライドバーによる回答方法

const handle = document.getElementById('sliderHandle')
const sliderContainer = document.getElementById('sliderContainer')

const minValue = 0
const maxValue = 9
let trackWidth = sliderContainer.getBoundingClientRect().width
let stepWidth = trackWidth / (maxValue - minValue)

function updateTrackWidth() {
    trackWidth = sliderContainer.getBoundingClientRect().width
    stepWidth = trackWidth / (maxValue - minValue)
    moveHandleToValue(parseInt(sliderValue.textContent))
}

window.addEventListener('resize', updateTrackWidth) //省略可能

handle.addEventListener('mousedown', (e) => {
    document.addEventListener('mousemove', onDrag)
    document.addEventListener('mouseup', stopDrag)
})

function onDrag(e) {
    moveHandle(e.clientX)
}

function stopDrag() {
    document.removeEventListener('mousemove', onDrag)
    document.removeEventListener('mouseup', stopDrag)
}

sliderContainer.addEventListener('click', (e) => {
    moveHandle(e.clientX)
})

function moveHandle(clientX) {
    let offsetX = clientX - sliderContainer.offsetLeft
    offsetX = Math.max(0, Math.min(offsetX, trackWidth))

    let closestValue = Math.round(offsetX / stepWidth)
    moveHandleToValue(closestValue)
}

const answerInput = document.getElementById('answer-input')

function moveHandleToValue(value) {
    handle.style.left = value * stepWidth + 'px'
    answerInput.value = value
    let percent = (value / (maxValue - minValue)) * 100 + '%'
    sliderContainer.style.setProperty('--filled-percent', percent)
}