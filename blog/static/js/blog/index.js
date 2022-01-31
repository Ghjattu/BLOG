// document.onreadystatechange = function () {
//     if (document.readyState === 'complete') {
//         console.log('complete');
//     }
// };
$(function () {
    let anchorLink = document.getElementById('scroll-down');
    let anchorLocation = document.getElementById('anchor');
    anchorLink.addEventListener('click', function (e) {
        if (window.scrollTo) {
            e.preventDefault();
            window.scrollTo({"behavior": "smooth", "top": anchorLocation.offsetTop});
        }
    });
});