document.addEventListener("DOMContentLoaded", function () {
    const links = document.querySelectorAll("a[href]:not([target])");
    links.forEach(link => {
        link.setAttribute("target", "_blank");
        link.setAttribute("rel", "nofollow noopener noreferrer");
    });
});