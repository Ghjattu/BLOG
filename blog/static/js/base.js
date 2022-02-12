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
        let menu = document.getElementById('menu');
        if (top !== 0) {
            menu.classList.add('not-at-top');
        } else {
            menu.classList.remove('not-at-top');
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
     * Hamburger Menu
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


    let top = $(window).scrollTop();
    let menu = document.getElementById('menu');
    if (top !== 0) {
        menu.classList.add('not-at-top');
    }
});