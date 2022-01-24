// document.onreadystatechange = function () {
//     if (document.readyState === 'complete') {
//         console.log('complete');
//     }
// };
window.onload = function () {
    console.log('onload');
    let loading = document.getElementsByClassName('loading')[0];
    loading.style.display = 'none';

    let anchorLink = document.getElementById('scroll-down');
    let anchorLocation = document.getElementById('anchor');
    anchorLink.addEventListener('click', function (e) {
        if (window.scrollTo) {
            e.preventDefault();
            window.scrollTo({"behavior": "smooth", "top": anchorLocation.offsetTop});
        }
    });

    let images = document.getElementsByClassName('bg-image');
    for (let i = 0; i < images.length; i++) {
        // images[i].setAttribute("src", "https://api.ixiaowai.cn/mcapi/mcapi.php");
        if (i % 2 === 0)
            images[i].style.borderRadius = "10px 0 0 10px";
        else
            images[i].style.borderRadius = "0 10px 10px 0";
    }

    Particles.init({
        selector: '.bg-particles',
        // 1201px ~
        maxParticles: 70,
        connectParticles: true,

        responsive: [
            {
                // 800px ~ 1200px
                breakpoint: 1200,
                options: {
                    maxParticles: 60,
                }
            }, {
                // 481px ~ 799px
                breakpoint: 800,
                options: {
                    maxParticles: 50,
                }
            }, {
                // 0 ~ 480px
                breakpoint: 480,
                options: {
                    maxParticles: 0,
                    connectParticles: false,
                }
            }
        ]
    });
};