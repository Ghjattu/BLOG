$(function () {
    /*
     * 将markdown生成的目录移到右边
     */
    let toc = document.getElementsByClassName('toc')[0];
    let articleCatalog = document.getElementsByClassName('article-catalog')[0];
    articleCatalog.appendChild(toc);

    /*
     * 为code代码块增加状态栏
     */
    let statusBar = document.getElementsByClassName('status-bar')[0];
    let codes = document.getElementsByTagName('pre');
    let codesParent = codes[0].parentNode;
    for(let i = 0; i < codes.length; i++) {
        let statusBarClone = statusBar.cloneNode(true);
        statusBarClone.classList.remove('deprecated');
        codesParent.insertBefore(statusBarClone, codes[i]);
    }
});