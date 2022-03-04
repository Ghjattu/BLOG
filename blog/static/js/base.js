/*
 * Progress Bar
 */
window.onscroll = () => {
    let progressBar = document.getElementById('progress-bar');
    let max = document.body.offsetHeight - window.innerHeight;
    let scrollTop = Math.ceil(document.documentElement.scrollTop);
    progressBar.style.width = (scrollTop * 100 / max) + "%";
}
window.onload = function () {
    let loading = document.getElementsByClassName('loading')[0];
    loading.style.display = 'none';


    let scroll = function () {
        let top = $(window).scrollTop();
        let menu = document.getElementById('menu'),
            setting = document.getElementById('setting');
        if (top !== 0) {
            menu.classList.add('not-at-top');
            setting.classList.add('not-at-top');
        } else {
            menu.classList.remove('not-at-top');
            setting.classList.remove('not-at-top');
        }
    }

    let raf = window.requestAnimationFrame;
    let $window = $(window);
    let lastScrollTop = $window.scrollTop();

    if (raf) {
        loop();
    }

    function loop() {
        let scrollTop = $window.scrollTop();
        if (lastScrollTop === scrollTop) {
            raf(loop);
        } else {
            lastScrollTop = scrollTop;

            // 如果进行了垂直滚动，执行scroll方法
            scroll();
            raf(loop);
        }
    }
}
$(function () {
    /*
     *  汉堡包菜单
     */
    let toggleButton = document.getElementById('menu-toggle');
    toggleButton.addEventListener('click', function (e) {
        e.preventDefault();
        let menu = document.getElementById('menu');
        menu.classList.toggle('is-open');

        let translateElements = document.getElementsByClassName('translate');
        for (let i = 0; i < translateElements.length; i++) {
            translateElements[i].classList.toggle('is-open');
        }
    });

    /*
     *  页面右下角的设置按钮
     */
    let setting = document.getElementById('setting');
    setting.addEventListener('click', function () {
        // e.preventDefault();
        let tools = document.getElementById('tools');
        tools.classList.toggle('open');
    });

    /*
     *  导航栏中的分类菜单
     */
    let categoryToggleButton = document.getElementById('category-toggle');
    let categorylist = document.getElementById('category-list');
    categoryToggleButton.onmouseover = function () {
        categorylist.classList.add('open');
    }
    categoryToggleButton.onmouseleave = function () {
        categorylist.classList.remove('open');
    }
    categorylist.onmouseover = function () {
        categorylist.classList.add('open');
    }
    categorylist.onmouseleave = function () {
        categorylist.classList.remove('open');
    }

    // 移动端
    let mobileCategoryToggleButton = document.getElementById('mb-category-toggle');
    mobileCategoryToggleButton.addEventListener('click', function (e) {
        e.preventDefault();
        let mobileCategoryList = document.getElementById('mb-category-list');
        mobileCategoryList.classList.toggle('open');
    });

    /*
     *  根据页面刷新时滚动条的位置设置导航栏的背景样式
     */
    let top = $(window).scrollTop();
    let menu = document.getElementById('menu');
    if (top !== 0) {
        menu.classList.add('not-at-top');
        setting.classList.add('not-at-top');
    }
});