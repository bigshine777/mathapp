const stages_percentage = window.stages_percentage;
const questions_percentage = window.questions_percentage;

const centerTextPlugin = {
    id: 'centerText',
    beforeDraw: (chart) => {
        const { width, height } = chart
        const ctx = chart.ctx
        ctx.save()
        const fontSize = (height / 100).toFixed(2)
        ctx.font = `${fontSize}em sans-serif`
        ctx.textAlign = 'center'
        ctx.textBaseline = 'middle'
        const text = `${chart.config.options.centerText}`
        const textX = width / 2
        const textY = height / 2
        ctx.fillText(text, textX, textY)
        ctx.restore()
    }
}

// ステージ進行度の円グラフ
const stageCtx = document.getElementById('complete-stage-chart').getContext('2d')
new Chart(stageCtx, {
    type: 'doughnut',
    data: {
        datasets: [
            {
                data: [stages_percentage, 100 - stages_percentage],
                backgroundColor: ['rgb(101, 214, 88)', 'rgb(234, 234, 234)'],
                borderWidth: 0
            }
        ]
    },
    options: {
        cutout: '70%',
        centerText: `${stages_percentage}%`
    },
    plugins: [centerTextPlugin]
})

// 問題進行度の円グラフ
const questionCtx = document.getElementById('complete-question-chart').getContext('2d')
new Chart(questionCtx, {
    type: 'doughnut',
    data: {
        datasets: [
            {
                data: [questions_percentage, 100 - questions_percentage],
                backgroundColor: ['rgb(101, 214, 88)', 'rgb(234, 234, 234)'],
                borderWidth: 0
            }
        ]
    },
    options: {
        cutout: '70%',
        centerText: `${questions_percentage}%`
    },
    plugins: [centerTextPlugin]
})