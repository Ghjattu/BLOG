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
                    maxParticles: 50,
                    connectParticles: false,
                }
            }
        ]
    });
});