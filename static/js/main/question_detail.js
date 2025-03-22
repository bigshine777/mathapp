// ドラッグ&ドロップによる回答システム

const answerBox = document.getElementById('answer-box')
const inputField = document.getElementById('answer-input')
const placeholder = answerBox.querySelector('.placeholder')

function allowDrop(event) {
    event.preventDefault()
}

function drag(event) {
    event.dataTransfer.setData('text', event.target.dataset.value)
}

function drop(event) {
    if (!answerBox) return;
    event.preventDefault()
    var data = event.dataTransfer.getData('text')
    if (placeholder) placeholder.remove()

    var p = document.createElement('p')
    p.textContent = data
    p.classList.add('dropped-number')
    answerBox.appendChild(p)

    inputField.value += data
}

// リロードボタン

const reloadBtn = document.getElementById("reload-button");

reloadBtn.addEventListener("click", () => {
    while (answerBox.firstChild) {
        answerBox.removeChild(answerBox.firstChild);
    }
});

// スライドバーによる回答方法

const handle = document.getElementById('sliderHandle')
const sliderContainer = document.getElementById('sliderContainer')

if (handle) {
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

    document.addEventListener("DOMContentLoaded", () => {
        answerInput.value = 0
    })

    function moveHandleToValue(value) {
        handle.style.left = value * stepWidth + 'px'
        answerInput.value = value
        let percent = (value / (maxValue - minValue)) * 100 + '%'
        sliderContainer.style.setProperty('--filled-percent', percent)
    }

}
