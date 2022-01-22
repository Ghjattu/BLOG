/*
 * Progress Bar
 */
window.onscroll = () => {
    let progressBar = document.getElementById('progress-bar');
    let max = document.body.offsetHeight - window.innerHeight;
    let scrollTop = Math.ceil(document.documentElement.scrollTop);
    progressBar.style.width = (scrollTop * 100 / max) + "%";
}
