fetch('/api/stages/')
    .then((response) => response.json())
    .then((data) => {
        const topLevelStage = data.filter((stage) => stage.parent === null)
        const root = d3.hierarchy(topLevelStage[0], (d) => d.children)

        const nodeSpacingX = 200 // 横の間隔
        const nodeSpacingY = 100 // 縦の間隔

        const treeLayout = d3.tree()
            .nodeSize([nodeSpacingY, nodeSpacingX]) // ノード間隔
            .separation(() => 1)

        treeLayout(root)

        // ツリーの最大深度（横方向の最大距離）
        const maxDepth = d3.max(root.descendants(), (d) => d.depth) || 1
        // const maxBranches = d3.max(root.descendants(), (d) => (d.children ? d.children.length : 0)) || 1;

        function countTotalBranches(node) {
            if (!node.children || node.children.length === 0) return 0;
            const branchCount = node.children.length > 1 ? node.children.length - 1 : 0;
            const childBranchCounts = node.children.map(countTotalBranches);

            return branchCount + d3.max(childBranchCounts, (d) => d);
        }

        const maxBranches = countTotalBranches(root) + 1;

        // ルートを中央寄せするためのオフセット
        const rootOffset = (maxDepth / 2) * (nodeSpacingX + 50)

        // **負の値にならないように修正**
        const dynamicWidth = (maxDepth + 2) * (nodeSpacingX + 80)
        const dynamicHeight = maxBranches * (nodeSpacingY + 15)

        // ルートの位置を中央にする
        root.descendants().forEach((d) => {
            d.y += rootOffset // 全体を右にオフセット
        })

        // スクロール可能にする
        const container = d3.select('#tree-container')
        container.style('overflow-x', 'auto')
            .style('white-space', 'nowrap')
            .style('width', '1000px')
            .style('height', 'min-content')

        const svg = container.append('svg')
            .attr('width', dynamicWidth)
            .attr('height', dynamicHeight)

        // gの位置を調整（中央寄せ）
        const g = svg.append('g').attr('transform', `translate(50, ${dynamicHeight / 2})`)

        // リンク（枝）を描画
        g.selectAll('.link')
            .data(root.links())
            .enter()
            .append('path')
            .attr('class', 'link')
            .attr(
                'd',
                d3.linkHorizontal()
                    .x((d) => d.y)
                    .y((d) => d.x)
            )
            .style('fill', 'none')
            .style('stroke', 'rgb(234, 204, 172)')
            .style('stroke-width', 8)

        // ノードを描画
        const nodes = g.selectAll('.node')
            .data(root.descendants())
            .enter()
            .append('g')
            .attr('class', 'node')
            .attr('transform', (d) => `translate(${d.y},${d.x})`)

        // ノードにボタンを追加
        nodes
            .append('foreignObject')
            .attr('x', -80)
            .attr('y', -30)
            .attr('width', 160)
            .attr('height', 60)
            .append('xhtml:div')
            .html((d) => `<a class="tree-button" href="/stages/${d.data.id}">${d.data.stage_name}</a>`)
    })
