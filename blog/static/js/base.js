/*
 * Progress Bar
 */
window.onscroll = () => {
    let progressBar = document.getElementById('progress-bar');
    let max = document.body.offsetHeight - window.innerHeight;
    let scrollTop = Math.ceil(document.documentElement.scrollTop);
    progressBar.style.width = (scrollTop * 100 / max) + "%";
}

$(function () {
    console.log('1');
    /*
     * Hamburger Menu
     */
    let toggleButton = document.getElementById('menu-toggle');
    toggleButton.addEventListener('click', function (e) {
        console.log('1');
        e.preventDefault();
        let menu = document.getElementById('menu');
        // let bodyWrapper = document.getElementById('body-wrapper');
        menu.classList.toggle('is-open');
        // bodyWrapper.classList.toggle('is-open');
        // bodyWrapper.style.display = 'block';
        // toggleButton.style.zIndex = 2;
    });
});