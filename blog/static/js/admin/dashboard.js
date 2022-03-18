$(function () {
    let newTagButton = document.getElementsByClassName('btn-new-tag')[0];
    newTagButton.addEventListener('click', function () {
        let newTagTable = document.getElementsByClassName('new-tag-table')[0];
        newTagTable.classList.toggle('open');
    })
})