$(function () {
    /*
     * 根据标签对应文章的数目分配权重以调整字体大小
     */
    function unique(arr) {
        return Array.from(new Set(arr));
    }

    let tags = document.getElementsByClassName('tag');
    let temp = [];
    for(let i = 0; i < tags.length; i++) {
        temp.push(tags[i].dataset.length);
    }
    let tagLength = unique(temp);
    tagLength.sort((a, b) => a - b);

    for(let i = 0; i < tags.length; i++) {
        tags[i].dataset.weight = (tagLength.indexOf(tags[i].dataset.length) + 1).toString();
    }
});