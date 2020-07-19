document.querySelector('.logo').addEventListener('click', function() {
    window.location.href = window.location.origin
});

function blog_add() {
    window.location.href = window.location.origin + '/blog/new'
}

function author_add() {
    window.location.href = window.location.origin + '/author/new'
}