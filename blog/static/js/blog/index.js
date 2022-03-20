$(function () {
    let anchorLink = document.getElementById('scroll-down');
    let anchorLocation = document.getElementById('anchor');
    anchorLink.addEventListener('click', function (e) {
        if (window.scrollTo) {
            e.preventDefault();
            window.scrollTo({"behavior": "smooth", "top": anchorLocation.offsetTop});
        }
    });


    // 当前页数
    let paginationPage = 1;
    // 总页数
    const paginationPages = Number(document.getElementById('main-articles').dataset.paginationPages);
    if (paginationPage === paginationPages) {
        // 创建新的span节点
        let newSpan = document.createElement('span');
        newSpan.textContent = '没有更多啦...';

        // 获取“点击加载更多”按钮和父节点
        let loadMoreButton = document.getElementById('load-more');
        let parent = loadMoreButton.parentNode;

        // 用新的span节点替换按钮
        parent.replaceChild(newSpan, loadMoreButton);
    }
    // 格式化时间戳
    let timestamps = document.getElementsByClassName('moment');
    for (let i = 0; i < timestamps.length; i++) {
        let timestamp = timestamps[i].textContent;
        timestamps[i].textContent = moment(timestamp).format('YYYY-MM-DD');
    }


    /*
     * 点击加载更多
     */
    let loadMoreButton = document.getElementById('load-more');
    let loadMoreAnimation = document.getElementById('loader');
    loadMoreButton.addEventListener('click', function () {
        // 显示加载动画
        loadMoreButton.style.display = 'none';
        loadMoreAnimation.style.display = 'block';

        $.ajax({
            type: 'GET',
            url: '/load_more',
            dataType: 'html',
            data: {
                // 传参
                page: paginationPage + 1,
            },
            success: function (data) {
                $('#main-articles').append(data);
            }
        });
    });

    /*
     * 主要是为了监听“点击加载更多”完成事件
     */
    const targetNode = document.getElementById('main-articles');
    const config = {childList: true};
    const callback = function (mutationsList) {
        for (let mutation of mutationsList) {
            if (mutation.type === 'childList') {
                // 移除加载动画
                loadMoreButton.style.display = 'inline-block';
                loadMoreAnimation.style.display = 'none';

                paginationPage += 1;

                // 如果当前加载的是最后一页, 则隐藏“点击加载更多”按钮
                if (paginationPage === paginationPages) {
                    // 创建新的span节点
                    let newSpan = document.createElement('span');
                    newSpan.textContent = '没有更多啦...';

                    // 获取“点击加载更多”按钮和父节点
                    let loadMoreButton = document.getElementById('load-more');
                    let parent = loadMoreButton.parentNode;

                    // 用新的span节点替换按钮
                    parent.replaceChild(newSpan, loadMoreButton);
                }

                // 格式化时间戳
                let timestamps = document.getElementsByClassName('moment');
                for (let i = 0; i < timestamps.length; i++) {
                    let timestamp = timestamps[i].textContent;
                    timestamps[i].textContent = moment(timestamp).format('YYYY-MM-DD');
                }
            }
        }
    };
    const observer = new MutationObserver(callback);
    observer.observe(targetNode, config);
});